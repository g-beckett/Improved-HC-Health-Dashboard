import { useState, useEffect } from 'react';
import axios from 'axios';
import NewCasesChart from '@/components/INFLUENZACasesChart';
import ComparisonChart from '@/components/ComparisonChart';
import DatePicker from '@/components/DatePicker';
import { today } from '@/components/utils';
import { ImSpinner2, ImArrowUp2, ImArrowDown2 } from 'react-icons/im';

const influenza = () => {
  const [diseases, setDiseases] = useState([]);
  const [caseReports, setCaseReports] = useState([]);
  // const [deathReports, setDeathReports] = useState([]);



  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://hcdbackend.fly.dev/dataportal/_query');
          const { Diseases, CaseReports } = response.data;
          const fluDiseases = Diseases.filter(report => report.Disease === 'ILI Uncategorized');
          const fluCaseReports = CaseReports.filter(report => report.Disease === 'ILI Uncategorized');
          // const fluDeathReports = DeathReports.filter(report => report.Disease === 'ILI Uncategorized');
          
          setDiseases(fluDiseases);
          setCaseReports(fluCaseReports);
          // setDeathReports(fluDeathReports);
          
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  // const [today, setSelectedDate] = useState(new Date().toLocaleDateString());
  const [today, setSelectedDate] = useState('12/27/23');

  const handleDateChange = (date) => {
    setSelectedDate(date);
  };

  const todaysDate = new Date(today);
  const month = (todaysDate.getMonth() + 1).toString().padStart(2, '0');
  const year = todaysDate.getFullYear().toString();
  const lastYear = (year - 1).toString();

  // Find the date of the most recent Saturday before or on the current date
  const todayDayOfWeek = todaysDate.getDay(); // 0 for Sunday, 1 for Monday, etc.
  const lastSaturday = new Date(todaysDate); // Clone today's date
  lastSaturday.setDate(todaysDate.getDate() - (todayDayOfWeek + 1) % 7); // Set it to the most recent Saturday

  // Find the report for today or the previous Saturday if a report for today doesn't exist
  var todaysReport = caseReports.find(report => {
      const reportDate = new Date(report.AnalyticsDate);
      // Check if the report date matches today's date
      return reportDate.toDateString() === todaysDate.toDateString();
    });
    
    if (!todaysReport) {
      // Find the report for the last Saturday
      const mostRecentReportDate = new Date(lastSaturday);
      const previousReport = caseReports.find(report => {
        const reportDate = new Date(report.AnalyticsDate);
        // Check if the report date falls within the week of the most recent Saturday
        return reportDate >= mostRecentReportDate && reportDate <= lastSaturday;
      });
      todaysReport = previousReport;
  }

  const monthlyCases = caseReports.reduce((total, report) => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0');
    const reportYear = reportDate.getFullYear().toString();
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
    const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0'); // Months are zero-based
    const reportYear = reportDate.getFullYear().toString();
    return reportMonth === month && reportYear === year;
  });

  const filteredCaseReportsYear = caseReports.filter(report => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportYear = reportDate.getFullYear().toString();
    return reportYear === year;
  }); 

  return (
    <div className="container mx-auto p-4 text-center text-TN-blue">
    {diseases ? (
      <div className="text-3xl font-semibold mb-4">COVID-19 Disease Data for <DatePicker selectedDate={today} handleDateChange={handleDateChange}/></div> 
       ) : ( 
      <div className="flex items-center justify-center h-full">
        <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
      </div>
      )}

      <img
        src="Flu banner.png"
        alt="An image of a Influenza virus"
        className="mx-auto mb-8 width-full flex rounded-md"
        style={{ width: '600px' }}
      />

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">Most Recent Case Report</h3>
            {todaysReport ? (
              <p>{todaysReport.NumberOfNewCases.toLocaleString()} Cases - Reported on {todaysReport.AnalyticsDate.split(' ')[0]}</p>
              ) : (
              <div className="flex items-center justify-center h-fit">
                <ImSpinner2 className="animate-spin h-6 w-6 mr-2 text-gray-500" /> Loading...
              </div>
            )}
        </div>

        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">Cases This Month</h3>
            {monthlyCases ? (
              percentageChange > 0 ? (
                <div className="flex items-center justify-center h-fit">
                  <p>{monthlyCases.toLocaleString()} Cases - </p> <ImArrowUp2 className='h-4 w-4 mr-1 ml-1'/> <p>{percentageChange.toFixed(2)}%</p>
                </div>                
                ) : (
                <div className="flex items-center justify-center h-fit">
                  <p>{monthlyCases.toLocaleString()} Cases - </p> <ImArrowDown2 className='h-4 w-4 mr-1 ml-1'/> <p>{percentageChange.toFixed(2)}%</p>
                </div>            
                )    
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
        <h3 className="text-xl font-semibold mb-4">Reported New Cases</h3>
        {filteredCaseReports.length > 0 ? (
          <NewCasesChart chartData={filteredCaseReports} yearData={filteredCaseReportsYear} allData={caseReports}/>
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

export default influenza;
