from faker import Faker
from datetime import datetime, date
import csv
import math

# Will need to update requirements with faker

fake = Faker(locale='en_us')

"""
For CaseReports

Will create seperate location to load data into new json folder to seperate mock from real.


disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    case_count = models.IntegerField(default=0)
    case_count_epi = models.IntegerField(default=0)
    sex_female_count = models.IntegerField(default=0)
    sex_male_count = models.IntegerField(default=0)
    sex_unknown_count = models.IntegerField(default=0)
    race_white_count = models.IntegerField(default=0)
    race_black_count = models.IntegerField(default=0)
    race_asian_count = models.IntegerField(default=0)
    race_native_american_count = models.IntegerField(default=0)
    race_other_count = models.IntegerField(default=0)
    race_unknown_count = models.IntegerField(default=0)
    ethnicity_hispanic_count = models.IntegerField(default=0)
    ethnicity_non_hispanic_count = models.IntegerField(default=0)
    ethnicity_unknown_count = models.IntegerField(default=0)
    age_0_10_count = models.IntegerField(default=0)
    age_11_20_count = models.IntegerField(default=0)
    age_21_30_count = models.IntegerField(default=0)
    age_31_40_count = models.IntegerField(default=0)
    age_41_50_count = models.IntegerField(default=0)
    age_51_60_count = models.IntegerField(default=0)
    age_61_70_count = models.IntegerField(default=0)
    age_71_80_count = models.IntegerField(default=0)
    age_81_and_up_count = models.IntegerField(default=0)
    age_unknown_count = models.IntegerField(default=0)
    report_start_date = models.DateField()
    report_end_date = models.DateField()
    report_submission_date = models.DateField()

    This is the list that will be generated first
"""


import random
import time
from datetime import timedelta, datetime, date
from random import randint

"""
NOTES

Mock Data Generation

Script Args
1. disease - needs testing
2. start_date (dynamically set end-date to be the date the script was ran or week before for 1 week interval) - DONE
3. date_interval (1 week) - DONE
4. baseline_count - needs testing
5. minimum_count
6. maximum_count - needs testing
7. behavior
    1. uniform
    2. single_outbreak
    3. seasonal_fall
    4. seasonal_spring
"""




class CaseReports:

    def __init__(self, num_reports: int):
        self.num_reports = num_reports
        self.case_reports = []
        self.case_report_date = []
        self.disease_record = {}
        self.case_count = []
        self._on_init()

    def _generate_data(self):

        #print(self.case_report_date)        

        self.case_reports = [1]*self.num_reports
        self.case_report_list = []

        case_start_date = list(map(lambda x: x["case_start_date"], self.case_report_date))
        case_end_date = list(map(lambda x: x["case_end_date"], self.case_report_date))
        case_report_date = list(map(lambda x: x["case_report_date"], self.case_report_date))
        
        for i in range(1, self.num_reports+1):
            disease_record = {}
            disease_record['AnalyticsRecordID'] = i
            # disease
            # category

            # using for loop i 
            
            disease_record['Case Start Date'] = case_start_date[i-1]
            disease_record['Case End Date'] = case_end_date[i-1]
            disease_record['Case Report Date'] = case_report_date[i-1]

            #print(case_report_date)
            disease_record['Case Count'] = fake.random_int(min = 40, max = 120, step = 1)

            self.case_count.append(disease_record['Case Count'])
            #print("test",self.case_count)

            disease_record['Case Count EPI'] = 0

            count = disease_record['Case Count']
            epi = disease_record['Case Count EPI']


            disease_record['Males'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.485)
            disease_record['Females'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * .5)

            males_and_females = disease_record['Males'] + disease_record['Females']
            disease_record['Sex Unknown'] = disease_record['Case Count'] - males_and_females - disease_record['Case Count EPI']

            self.case_report_list.append([
                    disease_record['AnalyticsRecordID'], 
                    disease_record['Case Count'], 
                    disease_record['Case Count EPI'], 
                    disease_record['Males'], 
                    disease_record['Females'], 
                    disease_record['Sex Unknown']])
            
            #disease_record.update(self.generate_mock_case_report_dates())
            disease_record.update(self._add_race(count, epi))
            disease_record.update(self._add_ethnicity(count, epi))
            disease_record.update(self._add_age(count, epi))
            print(disease_record)

        #self.case_report_list.extend(self._add_race(count, epi))

        self.disease_record = disease_record

        return self.disease_record
        #self.case_report_list.extend(self._add_ethnicity(count, epi))
        #self.case_report_list.extend(self._add_age(count, epi))
        
        #print(self.case_report_list)
        
    def _add_race(self, count, epi):
            
            disease_record = {}
            disease_record['Race White Count'] = round((count + epi) * 0.707)
            disease_record['Race Black Count'] = round((count + epi) * 0.184)
            disease_record['Race Asian Count'] = round((count + epi) * 0.023)
            disease_record['Race Native American Count'] = round((count + epi) * 0.006)
            disease_record['Race Other Count'] = round((count + epi) * 0.07)
            all_races = disease_record['Race Asian Count'] + disease_record['Race Black Count'] + disease_record['Race Native American Count'] + disease_record['Race Other Count'] + disease_record['Race White Count']
            unknown_races = (count + epi) - all_races
            disease_record['Race Unknown Count'] = unknown_races

            return disease_record

    def _add_ethnicity(self, count, epi):
        disease_record = {}
        disease_record['Ethnicity Hispanic Count'] = round((count + epi) * 0.068)
        disease_record['Ethnicity Non-Hispanic Count'] = round((count + epi) * 0.922)
        hispanic_and_non_hispanic = disease_record['Ethnicity Hispanic Count'] + disease_record['Ethnicity Non-Hispanic Count']
        ethnicity_unknown = (count + epi) - hispanic_and_non_hispanic
        disease_record['Ethnicity Unknown Count'] = ethnicity_unknown        

        return disease_record
    
    def _add_age(self, count, epi):
        disease_record = {}
        disease_record['Age 0-10 Count'] = round((count + epi) * 0.11)
        disease_record['Age 11-20 Count'] = round((count + epi) * 0.13)
        disease_record['Age 21-30 Count'] = round((count + epi) * 0.13)
        disease_record['Age 31-40 Count'] = round((count + epi) * 0.11)
        disease_record['Age 41-50 Count'] = round((count + epi) * 0.17)
        disease_record['Age 51-60 Count'] = round((count + epi) * 0.14)
        disease_record['Age 61-70 Count'] = round((count + epi) * 0.14)
        disease_record['Age 71-80 Count'] = round((count + epi) * 0.05)
        ages_added_up_to_80 = disease_record['Age 0-10 Count'] + disease_record['Age 11-20 Count'] + disease_record['Age 21-30 Count'] + disease_record['Age 31-40 Count'] + disease_record['Age 41-50 Count'] + disease_record['Age 51-60 Count'] + disease_record['Age 61-70 Count']
        age_is_80_plus = (count + epi) - ages_added_up_to_80
        disease_record['Age 80+ Count'] = age_is_80_plus
        disease_record['Age Unknown Count'] = round((count + epi) * 0)

        return disease_record



    def generate_mock_case_report_dates(self):


        #self.case_reports = [1]*self.num_reports


        # generate report dates automatically then generate data and add the case count data.
        # Don't just generate number of cases. Just do a year by each week.



        num_weeks = self.num_reports
        start_date = date(2023, 1, 1)
        

        end_date = date.fromtimestamp(time.time())
        diff = end_date - start_date
        current_date = start_date
        
        case_reports_date = []

        #Generate Empty Case Reports with only date populated
        for i in range(diff.days + 1):

            new_date = start_date + timedelta(days=i)            
            diff_end = new_date + timedelta(days=i+7)
            #end_of_week_date = 
            case_report = {"case_start_date": new_date,
                           "case_end_date": diff_end}

        while current_date < end_date:
            end_of_week_date = current_date + timedelta(days=6)

            if end_of_week_date > end_date:
                end_of_week_date = end_date
            case_report = {
                "case_start_date": current_date.strftime('%m-%d-%Y'),
                "case_end_date": end_of_week_date.strftime('%m-%d-%Y'),
                "case_report_date": end_of_week_date.strftime('%m-%d-%Y')
                
            }
            #case_report_one_week = {
                #"case_report_date": end_of_week_date.strftime('%m-%d-%Y'),
               # "case_data": self._generate_data() 
           # }
            current_date = end_of_week_date + timedelta(days=1)
            # printing dates
            #print(case_report)
            case_reports_date.append(case_report)
        #print(len(case_reports_date))
        # list of appended case_reports
        
        self.case_report_date = case_reports_date
        #print(self.case_report_date)
        #all_keys = set().union(*(d.keys() for d in self.case_report_date))
        #print(all_keys)


        #print(len(self.case_report_date)) - TESTING
        return self.case_report_date
       


    def generate_disease_counts(self, base_line_count: int, behavior: str, num_cases: int,
                            maximum_count:int, disease:str):

        # base line for starting point then max for highest peak.
        # each data point will be the case reports going up and down over the year/end time.

        #list_of_cases = list(map(lambda x: x['Case Count'], self.case_count))


        case_counts = []

        #initial_count = random.randint(int(base_line_count-base_line_count*.15)), int(base_line_count+base_line_count*.15)

        case_counts = []

        if disease == 'Covid':
            start_num = 40
            end_num = 120
        elif disease == 'Salmonella':
            start_num = 0
            end_num = 2
        match behavior:

            case "uniform": 
                for i in range(num_cases):
                    last_count = case_counts[-1] if case_counts else base_line_count
                    daily_case_count = random.randint(int(last_count - last_count*.05),
                                                    int(last_count + last_count*.05))
                    case_counts.append(daily_case_count)

            case "single_peak":

                for i in range(num_cases):
                    case_counts.append(CaseReports.poly(a=10, b=3, x=i, y=10))

        print("===================================",case_counts)



    def poly(a, b, x, y):

        # mean = np.mean(x) 
        # std = np.std(x) 
        # y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2)) 
        # return y_out 
        # https://www.geeksforgeeks.org/how-to-make-a-bell-curve-in-python/
    
        return y * math.exp(-(x - a)**2 / (2 * b**2))


    def _write_data(self, nameOfCSV):
        print(f"Wrote CSV:{len(self.case_reports)}")
        with open(nameOfCSV, 'w') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=self.disease_record)
            
                # writing headers (field names)
                writer.writeheader(self.disease_record.keys())
            
                # writing data rows
                writer.writerows(self.disease_record.values())

    def _on_init(self):
        self.generate_mock_case_report_dates()
        self.generate_disease_counts(25, 'single peak', len(self.case_report_date), 120, 'Covid')
        self._generate_data()
        #self._write_data()





mock = CaseReports(num_reports=61)


mock.generate_mock_case_report_dates()
#mock._generate_data


# a_param = 10
# b_param = 3
# x_values = list(range(20))
# y_values = [CaseReports.poly(a=a_param, b=b_param, x=x, y=10) for x in x_values]

# print(y_values)



#mock.generate_case_counts(base_line_count = 50, behavior="single_peak", num_cases=10, maximum_count=100)
# test = mock.create_case_report(1)
# print(test)



# if __name__ == "__main__":

#     # generate_case_counts(base_line_count=500, behavior="single_peak", num_cases=50, maximum_count=5000)

#     a = CaseReports(num_reports=1000)




"""
class Mock_Case_Reports:
    def __init__(self, disease_type):
        self.disease_type = disease_type
        self.case_reports = []

    def create_case_report(self, number_of_cases):
        case_report_list = []
        for i in range(1, number_of_cases):
            disease_record = {}
            disease_record['AnalyticsRecordID'] = i
            if self.disease_type == 'Covid-19':
                disease_record['Case Count'] = fake.random_int(min = 40, max = 120, step = 1)
            elif self.disease_type == 'Salmonella':
                
                disease_record['Case Count'] = fake.random.choices([1, 0], weights=[1.096, 98.904])
            # Set to 0 when generating data for behavior
            disease_record['Case Count EPI'] = fake.random.choice([0, 1, 2, 3], weights=[40, 25, 25, 10])
            disease_record['Males'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.485)
            # Generate for one then subtract from case count
            disease_record['Females'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * .5)
            disease_record['Sex Unknown'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) *.015)
            # Seperate function for races, ages, and ethnicity. Return them as a set and update them to the list.
            disease_record['Race White Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.707)
            disease_record['Race Black Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.184)
            disease_record['Race Asian Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.023)
            disease_record['Race Native American Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.006)
            disease_record['Race Other Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.07)
            disease_record['Race Unknown Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.01)
            disease_record['Ethnicity Hispanic Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.068)
            disease_record['Ethnicity Non-Hispanic Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.922)
            disease_record['Ethnicity Unknown Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.01)
            disease_record['Age 0-10 Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.11)
            disease_record['Age 11-20 Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.13)
            disease_record['Age 21-30 Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.13)
            disease_record['Age 31-40 Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.11)
            disease_record['Age 41-50 Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.17)
            disease_record['Age 51-60 Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.14)
            disease_record['Age 61-70 Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.14)
            disease_record['Age 71-80 Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.05)
            disease_record['Age 80+ Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0.01)
            disease_record['Age Unknown Count'] = round((disease_record['Case Count'] + disease_record['Case Count EPI']) * 0)
            # make a parameter and the number of case reports will be based off the date. 1 per day
           # disease_record['Report Start Date'] = datetime.date(2023, m, d)
           # disease_record['Report End Date'] = datetime.date(2023, m, d)

            # Make pattern selectable by uniform, etc. Code by doing match case


            case_report_list.append([
                    disease_record['AnalyticsRecordID'], 
                    disease_record['Case Count'], 
                    disease_record['Case Count EPI'], 
                    disease_record['Males'], 
                    disease_record['Females'], 
                    disease_record['Sex Unknown'], 
                    disease_record['Race White Count'], 
                    disease_record['Race Black Count'],
                    disease_record['Race Asian Count'], 
                    disease_record['Race Native American Count'], 
                    disease_record['Race Other Count'], 
                    disease_record['Race Unknown Count'], 
                    disease_record['Ethnicity Hispanic Count'], 
                    disease_record['Ethnicity Non-Hispanic Count'],
                    disease_record['Ethnicity Unknown Count'], 
                    disease_record['Age 0-10 Count'], 
                    disease_record['Age 11-20 Count'], 
                    disease_record['Age 21-30 Count'], 
                    disease_record['Age 31-40 Count'],
                    disease_record['Age 41-50 Count'], 
                    disease_record['Age 51-60 Count'], 
                    disease_record['Age 61-70 Count'],
                    disease_record['Age 71-80 Count'], 
                    disease_record['Age 80+ Count'], 
                    disease_record['Age Unknown Count'], 
                    disease_record['Report Start Date'], 
                    disease_record['Report End Date']
                ])
        self.case_reports = case_report_list    


    
    





    def writeToCSV(self, nameOfCSV):
            # field names
            fields = ['AnalyticsRecordID', 'Case Count', 'Case Count EPI', 'Males',
                      'Females', 'Sex Unknown', 'Race White Count', 'Race Black Count', 
                      'Race Asian Count', 'Race Native American Count', 'Race Other Count', 
                      'Race Unknown Count', 'Ethnicity Hispanic Count', 'Ethnicity Non-Hispanic Count',
                      'Ethnicity Unknown Count', 'Age 0-10 Count', 'Age 11-20 Count', 'Age 21-30 Count', 
                      'Age 31-40 Count','Age 41-50 Count', 'Age 51-60 Count', 'Age 61-70 Count',
                      'Age 71-80 Count', 'Age 80+ Count', 'Age Unknown Count', 'Report Start Date', 
                      'Report End Date']
 
            # writing to csv file
            with open(nameOfCSV, 'w') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)
            
                # writing headers (field names)
                writer.writeheader()
            
                # writing data rows
                writer.writerows(self.case_reports)
            
            # start = datetime.date(2023, 1, 1)
            # one_year_later = start + timedelta(days=365)
            # day = 1
            # month = 1
            # year = 2023
            # for i in number_of_cases:
            #     multiplier = i * 7
            #     end = date(year, month, day + multiplier)
            

"""

# import datetime
# start = datetime.date(2023, 6, 28)
# end = datetime.date(2023, 7, 5)
# date_of_range = [start + datetime.timedelta(days=delta) for delta in range((end - start).days + 1)]
# print("The range dates are:")
# for res_date in date_of_range:
#       print(res_date)
# print(date_of_range)

# from dateutil import rrule
# from datetime import datetime, timedelta

# day = 1
# month = 1
# year = 2023
# num = 4
# for i in range(num):
#       multiplier = i + 7
#       day += multiplier
#       end = date(year, month, day)
# print("End Date:", end)

# for dt in rrule.rrule(rrule.WEEKLY, dtstart=start, until=one_year_later):
#     print (dt) 


                






