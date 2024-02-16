import json
import requests

"""
In order to populate our DataPortal with some real data, we can just borrow what the existing COVID-19 page is loading
in.

https://health.hamiltontn.org/en-us/allservices/communicablediseases/coronavirus(covid-19).aspx

NOTE: There is another Dashboard here? That is better? - Access to more data?
https://health.hamiltontn.org/Coronavirus(COVID-19)_archive.aspx

Also a Vaccination Dashboard that has been 404
https://health.hamiltontn.org/AllServices/Coronavirus(COVID-19)/Vaccine/VaccineDataDashboard.aspx

There are 4 graphs on the page which correspond to 4 of our 5 _Report types.

This script mimics the existing data portal requests for the 4 chart types, then writes the data to /case_data.

load_hchd.py handles loading into our DB.
"""

NEW_CASES_URL = "https://secure2.hamiltontn.gov/covid19chartdata/NewCases.aspx/Chart_Data"
HOSPITALIZED_URL = "https://secure2.hamiltontn.gov/covid19chartdata/InpatientsAndPUIs.aspx/Chart_Data"
ICU_URL = "https://secure2.hamiltontn.gov/covid19chartdata/ICUPatients.aspx/Chart_Data"
DEATHS_URL = "https://secure2.hamiltontn.gov/covid19chartdata/Deaths.aspx/Chart_Data"


def get_write_data(url: str):

    payload = {"Criteria": "All", "FromDate": "1/1/1990", "ToDate": "1/1/2100"}

    res = requests.post(url, json=payload).json()

    print(len(res['d']))
    print(res['d'][0])
    print(res['d'][-1])

    write_name = url.rsplit("/", 2)[-2].replace(".aspx", "_data.json")

    with open(f"case_data/{write_name}", "w") as w_file:
        json.dump(res, w_file)


def main():

    get_write_data(NEW_CASES_URL)
    get_write_data(HOSPITALIZED_URL)
    get_write_data(ICU_URL)
    get_write_data(DEATHS_URL)


if __name__ == "__main__":

    main()

