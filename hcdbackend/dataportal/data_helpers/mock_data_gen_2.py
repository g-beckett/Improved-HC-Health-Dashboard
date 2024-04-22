import json
import random
from datetime import datetime, timedelta

"""
Script for generating mock data.

Writes JSON files to /mock_data using the real COVID-19 /case_data as a starting point. The real case data was pulled
from the Hamilton County Health Department's systems. - See scrape_hchd.py for that process.

See hard-codes at bottom in main() + comment in to enable. Will do fresh/full imports from scratch for any number
of diseases. You must ensure the desired disease/disease_category have previously been created.

Notes
~ Used real data for COVID-10 (/case_data)
~ Used the COVID-19 reports as a baseline for the others, but modified the case counts
~ Writes JSON to /mock_data. You then need to import this into the database in separate step (load_mock_data.py)
"""


def load_json(file_path: str):
    """
    Helper function for loading JSON
    """

    with open(file_path, "r") as r_file:
        return json.load(r_file)


def write_json(info_json: dict, file_path: str):
    """
    Helper function for writing JSON
    """

    with open(file_path, "w") as w_file:
        json.dump(info_json, w_file)


def random_helper(lower, upper):
    return round(random.uniform(lower, upper), 2)


def apply_demographic_fields(status_report: dict):
    """
    Working off a case or death count, since only those status reports include demographic information, use that to
    populate the demographic fields in a pseudo-realistic, but currently static, way.
    """

    try:
        total_count = status_report['case_count']   # Case Report
    except KeyError:
        total_count = status_report['death_count']  # Death Report

    # Sex
    sex_female_count = int(total_count * random_helper(.40, .50))
    sex_male_count = int(total_count * random_helper(.40, .50))
    sex_unknown_count = total_count - sum([sex_female_count, sex_male_count])

    # Race
    race_white_count = int(total_count * random_helper(.60, .70))
    race_black_count = int(total_count * random_helper(.10, .18))
    race_asian_count = int(total_count * random_helper(0.0, .02))
    race_native_american_count = int(total_count * random_helper(0.0, .01))
    race_other_count = int(total_count * random_helper(0.0, 0.04))
    race_unknown_count = total_count - sum([race_white_count, race_black_count, race_asian_count,
                                            race_native_american_count, race_other_count])

    # Ethnicity
    ethnicity_hispanic_count = int(total_count * random_helper(.03, .05))
    ethnicity_non_hispanic_count = int(total_count * random_helper(.80, .90))
    ethnicity_unknown_count = total_count - sum([ethnicity_hispanic_count, ethnicity_non_hispanic_count])

    # Age
    age_0_10_count = int(total_count * random_helper(0.0, .01))
    age_11_20_count = int(total_count * random_helper(0.0, .02))
    age_21_30_count = int(total_count * random_helper(0.0, .03))
    age_31_40_count = int(total_count * random_helper(0.02, .07))
    age_41_50_count = int(total_count * random_helper(0.05, .10))
    age_51_60_count = int(total_count * random_helper(0.07, .14))
    age_61_70_count = int(total_count * random_helper(0.12, .18))
    age_71_80_count = int(total_count * random_helper(0.14, .19))
    age_81_and_up_count = int(total_count * random_helper(0.16, .22))
    age_unknown_count = total_count - sum([age_0_10_count, age_11_20_count, age_21_30_count, age_31_40_count,
                                           age_41_50_count, age_51_60_count, age_61_70_count, age_71_80_count,
                                           age_81_and_up_count])

    status_report['sex_female_count'] = sex_female_count
    status_report['sex_male_count'] = sex_male_count
    status_report['sex_unknown_count'] = sex_unknown_count

    status_report['race_white_count'] = race_white_count
    status_report['race_black_count'] = race_black_count
    status_report['race_asian_count'] = race_asian_count
    status_report['race_native_american_count'] = race_native_american_count
    status_report['race_other_count'] = race_other_count
    status_report['race_unknown_count'] = race_unknown_count

    status_report['ethnicity_hispanic_count'] = ethnicity_hispanic_count
    status_report['ethnicity_non_hispanic_count'] = ethnicity_non_hispanic_count
    status_report['ethnicity_unknown_count'] = ethnicity_unknown_count

    status_report['age_0_10_count'] = age_0_10_count
    status_report['age_11_20_count'] = age_11_20_count
    status_report['age_21_30_count'] = age_21_30_count
    status_report['age_31_40_count'] = age_31_40_count
    status_report['age_41_50_count'] = age_41_50_count
    status_report['age_51_60_count'] = age_51_60_count
    status_report['age_61_70_count'] = age_61_70_count
    status_report['age_71_80_count'] = age_71_80_count
    status_report['age_81_and_up_count'] = age_81_and_up_count
    status_report['age_unknown_count'] = age_unknown_count

    status_report['sex_present'] = True
    status_report['race_present'] = True
    status_report['ethnicity_present'] = True
    status_report['age_present'] = True


def create_covid_reports():
    """
    Since the COVID-19 data is real, we will create reports from this data first. These reports will then be used as a
    starting point for the other diseases.

    This was done earlier in load_hchd.py.
    """

    submit_date = datetime.now().strftime("%Y-%m-%d")

    # Case Reports
    case_reports = []
    case_report_raw = load_json(file_path="case_data/NewCases_data.json")
    case_report_raw = case_report_raw['d']
    print(f"Creating: {len(case_report_raw)} CaseReports")
    for v in case_report_raw:
        case_count = int(v['NumberOfNewCases'])
        report_date = v['AnalyticsDate']
        report_date = datetime.strptime(report_date, '%m/%d/%Y')
        report_date = report_date.strftime("%Y-%m-%d")

        report = {"disease": "COVID-19",
                  "case_count": case_count,
                  "case_count_epi": 0,
                  "report_start_date": report_date,
                  "report_end_date": report_date,
                  "report_submission_date": submit_date}

        apply_demographic_fields(report)
        case_reports.append(report)

    # Death Reports
    death_reports = []
    death_report_raw = load_json(file_path="case_data/Deaths_data.json")
    death_report_raw = death_report_raw['d']
    print(f"Creating: {len(death_report_raw)} DeathReports")
    for v in death_report_raw:

        try:
            death_count = int(v['Deaths'])
        except ValueError:
            death_count = 0

        report_date = v['AnalyticsDate']
        report_date = datetime.strptime(report_date, '%m/%d/%Y')
        report_start_date = report_date + timedelta(days=-6)
        report_date = report_date.strftime("%Y-%m-%d")
        report_start_date = report_start_date.strftime("%Y-%m-%d")

        report = {"disease": "COVID-19",
                  "death_count": death_count,
                  "report_start_date": report_start_date,
                  "report_end_date": report_date,
                  "report_submission_date": submit_date}

        apply_demographic_fields(report)
        death_reports.append(report)

    # Hospitalized Reports (We need to combine these w/ the ICU Ones)
    hospitalized_reports = []
    hospital_report_data = load_json(file_path="case_data/InpatientsAndPUIs_data.json")
    hospital_report_data = hospital_report_data['d']

    icu_report_data = load_json(file_path="case_data/ICUPatients_data.json")
    icu_report_data = icu_report_data['d']

    # Make an ICU Map on Date/Count, then pull in during next step
    icu_count_map = {}
    for i, v in enumerate(icu_report_data):
        try:
            icu_count = int(v['PatientsInICUInCountyHospitals'])
        except ValueError:
            icu_count = 0
        report_date = v['AnalyticsDate']
        report_date = datetime.strptime(report_date, '%m/%d/%Y')
        report_date = report_date.strftime("%Y-%m-%d")
        icu_count_map[report_date] = icu_count

    print(f"Creating: {len(hospital_report_data)} HospitalizedReports")
    for i, v in enumerate(hospital_report_data):
        inpatient_count = int(v['HospitalizedInpatientsInHamiltonCounty'])
        under_investigation_count = int(v['HospitalizedPeopleUnderInvestigationInHamiltonCounty'])
        report_date = v['AnalyticsDate']
        report_date = datetime.strptime(report_date, '%m/%d/%Y')
        report_date = report_date.strftime("%Y-%m-%d")
        icu_count = icu_count_map[report_date]

        report = {"disease": "COVID-19",
                  "inpatient_count": inpatient_count,
                  "under_investigation_count": under_investigation_count,
                  "icu_count": icu_count,
                  "report_start_date": report_date,
                  "report_end_date": report_date,
                  "report_submission_date": submit_date
                  }

        hospitalized_reports.append(report)

    # Write Locally, we'll import later
    info_json = {"case_reports": case_reports,
                 "death_reports": death_reports,
                 "hospitalized_reports": hospitalized_reports}

    write_json(info_json, "mock_data/COVID-19_mock.json")


def create_other_disease_reports(disease: str, behavior: str, baseline_case_count: int,
                                 baseline_death_count: int, baseline_hospitalized_count: int,
                                 weekly: bool = False):
    """
    We will end up making this more realistic in Sprint 3
    """

    # Start w/ the covid_report, we'll use the same dates and just change case counts
    donor_report = load_json(file_path="mock_data/COVID-19_mock.json")

    # Case Report
    for i, v in enumerate(donor_report['case_reports']):

        v['disease'] = disease

        if behavior == "random_linear":
            if i == 0:
                last_count = baseline_case_count
            else:
                last_count = donor_report['case_reports'][i-1]['case_count']
            case_count = random.randint(int(last_count*.95), int(last_count*1.05))
            v['case_count'] = case_count
            apply_demographic_fields(status_report=v)

        elif behavior == "uniform_baseline":
            case_count = random.randint(int(baseline_case_count * .95), int(baseline_case_count * 1.05))
            v['case_count'] = case_count
            apply_demographic_fields(status_report=v)

        elif behavior == "uniform_baseline_peak_winter":
            case_count = random.randint(int(baseline_case_count * .95), int(baseline_case_count * 1.05))

            report_year = v['report_start_date'].split("-")[0]
            if report_year == '2020':
                case_count = int(case_count*.90)
            if report_year == '2021':
                case_count = int(case_count*.80)
            if report_year == '2022':
                case_count = int(case_count*1.2)
            if report_year == '2023':
                case_count = int(case_count*1.1)

            # Check if a Winter Month
            if v['report_start_date'].split("-")[1] in ['11', '02']:
                case_count *= 2
            if v['report_start_date'].split("-")[1] in ['01']:
                case_count *= 3
            if v['report_start_date'].split("-")[1] in ['12']:
                case_count = int(case_count * 3.5)

            v['case_count'] = case_count
            apply_demographic_fields(status_report=v)

        else:
            pass

    # print([v['case_count'] for v in donor_report['case_reports']])

    # Death Report
    for i, v in enumerate(donor_report['death_reports']):

        v['disease'] = disease

        # Just making this uniform for the moment
        death_count = random.randint(int(baseline_death_count * .95), int(baseline_death_count * 1.05))
        v['death_count'] = death_count
        apply_demographic_fields(status_report=v)

    # print([v['death_count'] for v in donor_report['death_reports']])

    # Hospitalized Report
    for i, v in enumerate(donor_report['hospitalized_reports']):

        v['disease'] = disease

        # Just making this uniform for the moment
        inpatient_count = random.randint(int(baseline_hospitalized_count * .95),
                                         int(baseline_hospitalized_count * 1.05))
        under_investigation_count = int(random.randint(int(baseline_hospitalized_count * .95),
                                                       int(baseline_hospitalized_count * 1.05)) * .20)
        icu_count = int(random.randint(int(baseline_hospitalized_count * .95),
                                       int(baseline_hospitalized_count * 1.05)) * .10)

        v['inpatient_count'] = inpatient_count
        v['under_investigation_count'] = under_investigation_count
        v['icu_count'] = icu_count

    if weekly:
        dr_start_dates = [v['report_start_date'] for v in donor_report['death_reports']]
        dr_end_dates = [v['report_end_date'] for v in donor_report['death_reports']]
        donor_report['case_reports'] = [v for v in donor_report['case_reports'] if v['report_end_date'] in dr_end_dates]
        donor_report['hospitalized_reports'] = [v for v in donor_report['hospitalized_reports'] if v['report_end_date'] in dr_end_dates]
        for i, v in enumerate(donor_report['case_reports']):
            v['report_start_date'] = dr_start_dates[i]
        for i, v in enumerate(donor_report['hospitalized_reports']):
            v['report_start_date'] = dr_start_dates[i]

    # print(len(donor_report['case_reports']))
    # print(len(donor_report['death_reports']))
    # print(len(donor_report['hospitalized_reports']))
    # for v in donor_report['case_reports']:
    #     print(v)

    write_json(donor_report, f"mock_data/{disease}_mock.json")


def main():

    # create_covid_reports()
    #
    # create_other_disease_reports(disease="Salmonella", behavior="uniform_baseline", baseline_case_count=30,
    #                              baseline_death_count=0, baseline_hospitalized_count=3)
    #
    # create_other_disease_reports(disease="Syphilis", behavior="random_linear", baseline_case_count=50,
    #                              baseline_death_count=0, baseline_hospitalized_count=10)
    #
    # create_other_disease_reports(disease="Norovirus", behavior="uniform_baseline", baseline_case_count=10,
    #                              baseline_death_count=1, baseline_hospitalized_count=2)
    #
    # create_other_disease_reports(disease="RSV", behavior="uniform_baseline_peak_winter", baseline_case_count=5,
    #                              baseline_death_count=0, baseline_hospitalized_count=2)
    #
    # create_other_disease_reports(disease="Influenza", behavior="uniform_baseline_peak_winter", baseline_case_count=10,
    #                              baseline_death_count=1, baseline_hospitalized_count=2)
    #
    # create_other_disease_reports(disease="HIV-AIDS", behavior="uniform_baseline", baseline_case_count=10,
    #                              baseline_death_count=1, baseline_hospitalized_count=1)

    # create_other_disease_reports(disease="ILI Uncategorized", behavior="uniform_baseline_peak_winter",
    #                              baseline_case_count=300, baseline_death_count=5, baseline_hospitalized_count=10,
    #                              weekly=True)

    create_other_disease_reports(disease="Campylobacter", behavior="uniform_baseline_peak_winter",
                                 baseline_case_count=40, baseline_death_count=0, baseline_hospitalized_count=13,
                                 weekly=True)


if __name__ == "__main__":

    main()

    # pass







