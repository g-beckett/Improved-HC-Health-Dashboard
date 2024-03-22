import { useState, useEffect } from 'react';
import axios from 'axios';
import NewCasesChart from '@/components/COVIDCasesChart';
import MonthlyDeathsChart from '@/components/COVIDMonthlyDeathsChart';
import HospitalizationChart from '@/components/COVIDHospitalizationChart';

const covid = () => {
  const [diseaseCategories, setDiseaseCategories] = useState([]);
  const [diseases, setDiseases] = useState([]);
  const [caseReports, setCaseReports] = useState([]);
  const [hospitalizedReports, setHospitalizedReports] = useState([]);
  const [deathReports, setDeathReports] = useState([]);



  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://hcdbackend.fly.dev/dataportal/_query');
          const { DiseaseCategories, Diseases, CaseReports, HospitalizedReports, DeathReports } = response.data;
          const covidDiseases = Diseases.filter(report => report.diseaseCategory === 'Coronavirus');
          const covidCaseReports = CaseReports.filter(report => report.DiseaseCategory === 'Coronavirus');
          const covidHospitalizedReports = HospitalizedReports.filter(report => report.DiseaseCategory === 'Coronavirus');
          const covidDeathReports = DeathReports.filter(report => report.DiseaseCategory === 'Coronavirus');
          
          setDiseaseCategories(DiseaseCategories);
          setDiseases(covidDiseases);
          setCaseReports(covidCaseReports);
          setHospitalizedReports(covidHospitalizedReports);
          setDeathReports(covidDeathReports);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  // const today = new Date().toLocaleDateString();
  const today = '12/22/2023 12:00:00 AM';
  const todaysDate = new Date(today);
  const month = (todaysDate.getMonth() + 1).toString().padStart(2, '0');
  const year = todaysDate.getFullYear().toString();

  const todaysCases = caseReports.find(report => report.AnalyticsDate === today);

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
    const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0'); 
    const reportYear = reportDate.getFullYear().toString();
    return reportMonth === month && reportYear === year;
  });

  return (
    <div className="container mx-auto p-4 text-center text-TN-blue">
    {diseases ? (
      <p className="text-3xl font-semibold mb-4">COVID-19 Disease Data for {today.split(' ')[0]}</p> 
       ) : ( 
        <h2 className="text-3xl font-semibold mb-4">Loading...</h2>
      )}

      <img
        src="hc_map.png"
        alt="Map of TN with Hamilton County Highlighted in Red"
        className="mx-auto mb-8 width-full flex"
        style={{ width: '800px', height: '200px' }}
      />

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">New Cases Today</h3>
            {todaysCases ? (
              <p>{todaysCases.NumberOfNewCases} Cases</p>
            ) : (
              <p>No data available for {today}</p>
            )}
        </div>

        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">Deaths This Month</h3>
            {monthlyDeaths ? (
              <p>{monthlyDeaths} Deaths</p>
            ) : (
              <p>No data available for {month}</p>
            )}
        </div>

        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">% Change in New Cases vs Last Month</h3>
            {Math.sign(percentageChange) === 1 ? (
              <p>+{percentageChange.toFixed(2)}%</p>
              ) : (
              <p>-{Math.abs(percentageChange.toFixed(2))}%</p>
            )}
        </div>
      </div>
          
      {/* charts */}
      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">Reported New Cases for {month}/{year}</h3>
        {filteredCaseReports.length > 0 ? (
          <NewCasesChart chartData={filteredCaseReports} yearData={filteredCaseReportsYear} />
        ) : (
          <p>No data available for {month}/{year}</p>
        )}
      </div>

      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">Reported Deaths This Month</h3>
        {filteredDeathReports.length > 0 ? (
          <MonthlyDeathsChart chartData={filteredDeathReports} />
        ) : (
          <p>No data available for {month}/{year}</p>
        )}
      </div>

      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">COVID-19 Hospitalization Data</h3>
        {hospitalizedReports.length > 0 ? (
          <HospitalizationChart chartData={hospitalizedReports} today={todaysDate} />
        ) : (
          <p>No data available for {month}/{year}</p>
        )}
      </div>

    </div>
  );
};

export default covid;
