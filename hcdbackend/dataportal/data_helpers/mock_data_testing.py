import random
import time
from datetime import timedelta, datetime, date
from random import randint

"""
NOTES

Mock Data Generation

Script Args
1. disease
2. start_date (dynamically set end-date to be the date the script was ran or week before for 1 week interval)
3. date_interval (1 day)
4. baseline_count
5. minimum_count
6. maximum_count
7. behavior
    1. uniform
    2. single_outbreak
    3. seasonal_fall
    4. seasonal_spring
"""


def generate_mock_data():

    start_date = date(2023, 1, 1)
    end_date = date.fromtimestamp(time.time())
    diff = end_date - start_date

    case_reports = []

    # Generate Empty Case Reports with only date populated
    for i in range(diff.days + 1):

        new_date = start_date + timedelta(days=i)
        case_report = {"case_date": new_date,
                       "case_count": 0}

        case_reports.append(case_report)

    print(case_reports)


def generate_case_counts(base_line_count: int, behavior: str, num_cases: int,
                         maximum_count:int ):

    case_counts = []

    initial_count = random.randint(int(base_line_count-base_line_count*.15),
                                   int(base_line_count+base_line_count*.15))

    case_counts = []

    match behavior:

        case "uniform":
            for i in range(num_cases):
                last_count = case_counts[-1]
                daily_case_count = random.randint(int(last_count - last_count*.05),
                                                  int(last_count + last_count*.05))
                case_counts.append(daily_case_count)

        case "single_peak":

            for i in range(num_cases):
                case_counts.append(poly(a=10, b=-.3, x=i, y=10))

    print(case_counts)



def poly(a, b, x, y):

    return a*(x*x) + b*x + y


class CaseReports:

    def __init__(self, num_reports: int):
        self.num_reports = num_reports
        self.case_reports = []
        self._on_init()

    def _generate_data(self):
        self.case_reports = [1]*self.num_reports

    def _write_data(self):
        print(f"Wrote CSV:{len(self.case_reports)}")

    def _on_init(self):
        self._generate_data()
        self._write_data()


if __name__ == "__main__":

    # generate_case_counts(base_line_count=500, behavior="single_peak", num_cases=50, maximum_count=5000)

    a = CaseReports(num_reports=1000)


