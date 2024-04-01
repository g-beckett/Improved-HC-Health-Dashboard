import json
import requests
from typing import Dict
from datetime import datetime
from random import randint

from copy import deepcopy

"""
Script for "scraping" the data Hamilton County is using for their current Health Dashboard. Outputs to JSON 
in /case_data. This output is then imported directly into our system for COVID-19, and also used as a starting point
for various mock data for other diseases.

In order to populate our DataPortal with some real data, we can just borrow what the existing COVID-19 page is loading
in.

https://health.hamiltontn.org/en-us/allservices/communicablediseases/coronavirus(covid-19).aspx

Also this archived case URL provides additional historical data.
https://health.hamiltontn.org/Coronavirus(COVID-19)_archive.aspx

There are 4 graphs on the page which correspond to our 3 report types. ICU / InpatientsAndPUI end up getting combined
in our system.

This script mimics the existing data portal requests for the 4 chart types, then writes the data to /case_data.

load_mock_data.py handles loading into our DB.
"""

# Endpoints for current Dashboard
NEW_CASES_URL = "https://secure2.hamiltontn.gov/covid19chartdata/NewCases.aspx/Chart_Data"
HOSPITALIZED_URL = "https://secure2.hamiltontn.gov/covid19chartdata/InpatientsAndPUIs.aspx/Chart_Data"
ICU_URL = "https://secure2.hamiltontn.gov/covid19chartdata/ICUPatients.aspx/Chart_Data"
DEATHS_URL = "https://secure2.hamiltontn.gov/covid19chartdata/Deaths.aspx/Chart_Data"

# Endpoint for archived Dashboard
NEW_CASES_ARCHIVE_URL = "https://secure2.hamiltontn.gov/covid19chartdata/NewCases_Archive.aspx/Chart_Data"


def read_json(file_path: str) -> Dict:

    with open(file_path, "r") as r_file:
        return json.load(r_file)


def write_json(json_data: Dict, file_path: str):

    with open(file_path, "w") as w_file:
        json.dump(json_data, w_file)


def get_write_data(url: str):

    payload = {"Criteria": "All", "FromDate": "1/1/1990", "ToDate": "1/1/2100"}

    res = requests.post(url, json=payload).json()

    print(len(res['d']))
    print(res['d'][0])
    print(res['d'][-1])

    res['d'].sort(key=lambda x: datetime.strptime(x['AnalyticsDate'].split(" ", 1)[0].strip(), '%m/%d/%Y'))

    write_name = url.rsplit("/", 2)[-2].replace(".aspx", "_data.json")

    with open(f"case_data/{write_name}", "w") as w_file:
        json.dump(res, w_file)


def get_combine_archived_data():

    payload = {"Criteria": "All", "FromDate": "1/1/1990", "ToDate": "1/1/2100"}

    res = requests.post(NEW_CASES_ARCHIVE_URL, json=payload).json()

    # Combine the archived data with the current
    with open("case_data/NewCases_data.json", "r") as r_file:
        curr_data = json.load(r_file)

    print(len(curr_data['d']))
    print(len(res['d']))

    curr_data['d'] = res['d'] + curr_data['d']

    curr_data['d'].sort(key=lambda x: datetime.strptime(x['AnalyticsDate'].split(" ", 1)[0].strip(), '%m/%d/%Y'))

    with open("case_data/NewCases_data.json", "w") as w_file:
        json.dump(curr_data, w_file)


def sanitize_data():

    death_data = read_json("case_data/Deaths_data.json")
    icu_data = read_json("case_data/ICUPatients_data.json")
    pui_data = read_json("case_data/InpatientsAndPUIs_data.json")
    case_data = read_json("case_data/NewCases_data.json")

    # Remove h/m/s from AnalyticsDate
    for report in [death_data, icu_data, pui_data, case_data]:
        for record in report['d']:
            record['AnalyticsDate'] = record['AnalyticsDate'].split(" ", 1)[0].strip()

    # Check Data Start/Stop - Had sorted earlier
    for report in [death_data, icu_data, pui_data, case_data]:
        print(report['d'][0]['AnalyticsDate'])
        print(report['d'][-1]['AnalyticsDate'])

    allowed_state_date = datetime.strptime('7/1/2020', '%m/%d/%Y')
    allowed_end_date = datetime.strptime('3/9/2024', '%m/%d/%Y')
    # So lets start on 7/1/2020 and end by 3/9/2024 (The last entry in the weekly death reports)
    for report in [death_data, icu_data, pui_data, case_data]:
        safe_records = []
        for record in report['d']:
            record_date = datetime.strptime(record['AnalyticsDate'], '%m/%d/%Y')
            if record_date > allowed_end_date:
                continue
            if record_date < allowed_state_date:
                continue
            safe_records.append(record)
        report['d'] = safe_records

    # Check Data Start/Stop After Clipping Dates
    for report in [death_data, icu_data, pui_data, case_data]:
        print(report['d'][0]['AnalyticsDate'])
        print(report['d'][-1]['AnalyticsDate'])

    # Check for daily missing dates
    for report in [icu_data, pui_data, case_data]:
        print(len(report['d']))

    # So we have ~200 record missing in the daily COVID case data
    date_map = {}
    for v in icu_data['d']:
        date_map[v['AnalyticsDate']] = None
    for v in case_data['d']:
        date_map[v['AnalyticsDate']] = v

    fixed_case_data = []

    for v in date_map:
        if date_map[v]:
            fixed_case_data.append(date_map[v])
        else:
            print("Adding Mock Covid Report")
            donor_record = deepcopy(case_data['d'][0])
            donor_record['AnalyticsDate'] = v
            date_obj = datetime.strptime(v, '%m/%d/%Y')
            if date_obj.weekday() in [5, 6]:
                case_count = 0
            else:
                case_count = str(randint(40, 120))
            donor_record['NumberOfNewCases'] = case_count
            fixed_case_data.append(donor_record)

    case_data['d'] = fixed_case_data

    # Check Data Start/Stop After Clipping Dates
    for report in [death_data, icu_data, pui_data, case_data]:
        print(report['d'][0]['AnalyticsDate'])
        print(report['d'][-1]['AnalyticsDate'])

    # Check for daily missing dates
    for report in [icu_data, pui_data, case_data]:
        print(len(report['d']))

    write_json(death_data, "case_data/Deaths_data.json")
    write_json(icu_data, "case_data/ICUPatients_data.json")
    write_json(pui_data, "case_data/InpatientsAndPUIs_data.json")
    write_json(case_data, "case_data/NewCases_data.json")


def main():

    # Get data from current dashboard
    # get_write_data(NEW_CASES_URL)
    # get_write_data(HOSPITALIZED_URL)
    # get_write_data(ICU_URL)
    # get_write_data(DEATHS_URL)

    # Get archived COVID Case data from archive dashboard
    # get_combine_archived_data()

    # Fill in missing date range in COVID-19 cases and sanitize date ranges (to have equal start/end)
    # sanitize_data()

    pass


if __name__ == "__main__":

    main()

