import { useState, useEffect } from 'react';
import axios from 'axios';
import NewCasesChart from '@/components/COVIDCasesChart';
import MonthlyDeathsChart from '@/components/COVIDMonthlyDeathsChart';
import HospitalizationChart from '@/components/COVIDHospitalizationChart';
import ComparisonChart from '@/components/ComparisonChart';
import DatePicker from '@/components/DatePicker';
import { date } from '@/components/utils';
import { ImSpinner2 } from 'react-icons/im';


const foodborne = () => {
  const [caseReports, setCaseReports] = useState([]);
  const [hospitalizedReports, setHospitalizedReports] = useState([]);
  const [deathReports, setDeathReports] = useState([]);



  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://hcdbackend.fly.dev/dataportal/_query');
          const { CaseReports, HospitalizedReports, DeathReports } = response.data;
          const fbCaseReports = CaseReports.filter(report => report.DiseaseCategory === 'Foodborne Illness');
          const fbHospitalizedReports = HospitalizedReports.filter(report => report.DiseaseCategory === 'Foodborne Illness');
          const fbDeathReports = DeathReports.filter(report => report.DiseaseCategory === 'Foodborne Illness');
          
          setCaseReports(fbCaseReports);
          setHospitalizedReports(fbHospitalizedReports);
          setDeathReports(fbDeathReports);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const [today, setSelectedDate] = useState(date);
  // const [today, setSelectedDate] = useState('12/27/23');

  const handleDateChange = (date) => {
    setSelectedDate(date);
  };

  const todaysDate = new Date(today);
  const month = (todaysDate.getMonth() + 1).toString().padStart(2, '0');
  const year = todaysDate.getFullYear().toString();
  const lastYear = (year - 1).toString();

  const todaysCases = caseReports.find(report => {
    const reportDate = new Date(report.AnalyticsDate);
    return reportDate.toLocaleDateString() === todaysDate.toLocaleDateString();
  });
  
  

  // Calculate the sum of deaths for the entire month
  const monthlyDeaths = deathReports.reduce((total, report) => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0');
    const reportYear = reportDate.getFullYear().toString();
    // console.log("Report Date:", reportDate);
    // console.log("Report Month:", reportMonth);
    // console.log("Report Year:", reportYear);
    // console.log("Month:", month);
    // console.log("Year:", year);
    // console.log("Is Same Month:", reportMonth === month);
    // console.log("Is Same Year:", reportYear === year);
    if (reportMonth === month && reportYear === year) {
      // console.log("Adding Deaths:", report.Deaths);
      return total + report.Deaths;
    } else {
      // console.log("Not Adding Deaths"); 
      return total;
    }
  }, 0);

  const monthlyCases = caseReports.reduce((total, report) => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0');
    const reportYear = reportDate.getFullYear().toString();
    // console.log("Report Date:", reportDate);
    // console.log("Report Month:", reportMonth);
    // console.log("Report Year:", reportYear);
    // console.log("Month:", month);
    // console.log("Year:", year);
    // console.log("Is Same Month:", reportMonth === month);
    // console.log("Is Same Year:", reportYear === year);
    if (reportMonth === month && reportYear === year) {
      // console.log("Adding Deaths:", report.Deaths);
      return total + report.NumberOfNewCases;
    } else {
      // console.log("Not Adding Deaths"); 
      return total;
    }
  }, 0);

  const lastYearsMonthlyCases = caseReports.reduce((total, report) => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0');
    const reportYear = reportDate.getFullYear().toString();
    if (reportMonth === month && reportYear === lastYear) {
      // console.log("Adding Deaths:", report.Deaths);
      return total + report.NumberOfNewCases;
    } else {
      // console.log("Not Adding Deaths"); 
      return total;
    }
  }, 0);
  
  // Calculate the sum of deaths for the previous month
  const prevMonthInt = todaysDate.getMonth() === 0 ? 12 : todaysDate.getMonth(); //if current month is January, set previous month to December
  const previousMonth = prevMonthInt.toString().padStart(2, '0');
  const previousYear = previousMonth === 12 ? todaysDate.getFullYear() - 1 : todaysDate.getFullYear(); // Decrement the year only if previous month is December
  const previousMonthsCases = caseReports.reduce((total, report) => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0');
    const reportYear = reportDate.getFullYear().toString();

    // console.log("Report Date:", reportDate);
    // console.log("Report Month:", reportMonth);
    // console.log("Report Year:", reportYear);
    // console.log("Month:", previousMonth.toString());
    // console.log("Year:", previousYear.toString());
    // console.log("Is Same Month:", reportMonth === previousMonth.toString());
    // console.log("Is Same Year:", reportYear === previousYear.toString());
    if (reportMonth === previousMonth.toString() && reportYear === previousYear.toString()) {
      // console.log("Adding Previous Deaths:", report.Deaths);
      return total + report.NumberOfNewCases; 
    } else {
      // console.log("Not Adding Deaths"); 
      return total;
    }
  }, 0);


  // Calculate the percentage change from the previous month to the current month
  const percentageChange = previousMonthsCases !== 0 ? ((monthlyCases - previousMonthsCases) / previousMonthsCases) * 100 : 0;

  // Filter CaseReports for the specific month and year
  const filteredCaseReports = caseReports.filter(report => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0'); 
    const reportYear = reportDate.getFullYear().toString();
    return reportMonth === month && reportYear === year;
  });

  const filteredCaseReportsYear = caseReports.filter(report => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportYear = reportDate.getFullYear().toString();
    return reportYear === year;
  }); //console.log(filteredCaseReportsYear);

  const filteredDeathReports = deathReports.filter(report => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportYear = reportDate.getFullYear().toString();
    return reportYear === year && report.Disease == 'Norovirus';
  });

  return (
    <div className="container mx-auto p-4 text-center text-TN-blue">
    {caseReports ? (
      <div className="text-3xl font-semibold mb-4">Foodborne Illness Data for <DatePicker selectedDate={today} handleDateChange={handleDateChange}/></div> 
       ) : ( 
        <div className="flex items-center justify-center h-fit">
          <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
        </div>
      )}

      <img
        src="foodborne.jpg"
        alt="An image of a Coronavirus Cell"
        className="mx-auto mb-8 width-full flex rounded-md"
        style={{ width: '600px' }}
      />

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">New Cases Today</h3>
            {todaysCases ? (
              <p>{todaysCases.NumberOfNewCases} Cases</p>
            ) : (
              <div className="flex items-center justify-center h-fit">
                <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
              </div>
            )}
        </div>

        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">Deaths This Month</h3>
            {monthlyDeaths ? (
              <p>{monthlyDeaths} Deaths</p>
            ) : (
              <div className="flex items-center justify-center h-fit">
                <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
              </div>
            )}
        </div>

        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">Cases {month}/{year - 1} vs Cases {month}/{year}</h3>
          {monthlyCases && lastYearsMonthlyCases ? (
            <p>{lastYearsMonthlyCases.toLocaleString()} : {monthlyCases.toLocaleString()}</p>
          ) : (
          <div className="flex items-center justify-center h-fit">
            <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
          </div>
          )
        }
        </div>
      </div>
          
      {/* charts */}
      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">Norovirus New Cases for {month}/{year}</h3>
        {filteredCaseReports.length > 0 ? (
          <NewCasesChart 
          chartData={filteredCaseReports.filter(report => {
            return report.Disease == 'Norovirus';
          })} 
          yearData={filteredCaseReportsYear.filter(report => {
            return report.Disease == 'Norovirus';
          })} />
        ) : (
          <div className="flex items-center justify-center h-fit">
            <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
          </div>
        )}
      </div>

      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">Salmonella New Cases for {month}/{year}</h3>
        {filteredCaseReports.length > 0 ? (
          <NewCasesChart 
          chartData={filteredCaseReports.filter(report => {
            return report.Disease == 'Salmonella';
          })} 
          yearData={filteredCaseReportsYear.filter(report => {
            return report.Disease == 'Salmonella';
          })} />
        ) : (
          <div className="flex items-center justify-center h-fit">
            <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
          </div>
        )}
      </div>

      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">Campylobacter New Cases for {month}/{year}</h3>
        {filteredCaseReports.length > 0 ? (
          <NewCasesChart 
          chartData={filteredCaseReports.filter(report => {
            return report.Disease == 'Campylobacter';
          })} 
          yearData={filteredCaseReportsYear.filter(report => {
            return report.Disease == 'Campylobacter';
          })} />
        ) : (
          <div className="flex items-center justify-center h-fit">
            <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
          </div>
        )}
      </div>

      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">Reported Deaths</h3>
        {filteredDeathReports.length > 0 ? (
          <MonthlyDeathsChart chartData={filteredDeathReports} allData={deathReports}/>
        ) : (
          <div className="flex items-center justify-center h-fit">
            <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
          </div>
        )}
      </div>

      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">Foodborne Illness Hospitalization Data</h3>
        {hospitalizedReports.length > 0 ? (
          <HospitalizationChart chartData={hospitalizedReports} today={todaysDate} />
        ) : (
          <div className="flex items-center justify-center h-fit">
            <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
          </div>
        )}
      </div>

      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">Comparison of Yearly Cases</h3>
        {filteredCaseReports.length > 0 ? (
          <ComparisonChart chartData={caseReports} today={todaysDate} />
        ) : (
          <div className="flex items-center justify-center h-fit">
            <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
          </div>
        )}
      </div>

    </div>
  );
};

export default foodborne;
