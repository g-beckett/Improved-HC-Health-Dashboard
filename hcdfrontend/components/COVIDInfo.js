import { useState, useEffect } from 'react';
import axios from 'axios';
import { useRouter } from 'next/router';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const COVIDInfo = () => {
  const [diseaseCategories, setDiseaseCategories] = useState([]);
  const [diseases, setDiseases] = useState([]);
  const [caseReports, setCaseReports] = useState([]);
  const [hospitalizedReports, setHospitalizedReports] = useState([]);
  const [icuReports, setICUReports] = useState([]);
  const [deathReports, setDeathReports] = useState([]);



  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://hcdbackend.fly.dev/dataportal/_query');
          const { DiseaseCategories, Diseases, CaseReports, HospitalizedReports, ICUReports, DeathReports } = response.data;
          const covidDiseases = Diseases.filter(report => report.diseaseCategory === 'Coronavirus');
          const covidCaseReports = CaseReports.filter(report => report.DiseaseCategory === 'Coronavirus');
          const covidHospitalizedReports = HospitalizedReports.filter(report => report.DiseaseCategory === 'Coronavirus');
          const covidICUReports = ICUReports.filter(report => report.DiseaseCategory === 'Coronavirus');
          const covidDeathReports = DeathReports.filter(report => report.DiseaseCategory === 'Coronavirus');
          
          setDiseaseCategories(DiseaseCategories);
          setDiseases(covidDiseases);
          setCaseReports(covidCaseReports);
          setHospitalizedReports(covidHospitalizedReports);
          setICUReports(covidICUReports);
          setDeathReports(covidDeathReports);
          
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const today = new Date().toLocaleDateString();
  // const today = '10/29/2023 12:00:00 AM';
  const todaysDate = new Date(today);
  const month = (todaysDate.getMonth() + 1).toString().padStart(2, '0');
  const year = todaysDate.getFullYear().toString();
  console.log(month + '/' + year);

  const todaysDeaths = deathReports.find(report => report.AnalyticsDate === today);

  // Filter DeathReports for the specific month
  const deathReportsForSpecificMonthYear = deathReports.filter(report => {
    const reportDate = new Date(report.AnalyticsDate);
    const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0'); //months are zero-based
    const reportYear = reportDate.getFullYear().toString();
    return reportMonth === month && reportYear === year;
  });

  // Calculate the sum of deaths for the entire month
  const monthlyDeaths = deathReportsForSpecificMonthYear.reduce((total, report) => total + report.NumberOfDeaths, 0);


    // Filter CaseReports for the specific month and year
    const filteredCaseReports = caseReports.filter(report => {
      const reportDate = new Date(report.AnalyticsDate);
      const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0'); // Months are zero-based
      const reportYear = reportDate.getFullYear().toString();
      return reportMonth === month && reportYear === year;
    });

    const aggregatedData = {};
    filteredCaseReports.forEach(report => {
      const day = report.AnalyticsDate.split(' ')[0];
      aggregatedData[day] = (aggregatedData[day] || 0) + report.NumberOfNewCases;
      // console.log(aggregatedData[day]);
    });
  
    const chartData = Object.keys(aggregatedData).map(day => ({
      date: day,
      numberOfNewCases: aggregatedData[day],
    }));
  console.log('disease data:' + diseases);

  return (
    <div className="container mx-auto p-4 text-center text-TN-blue">
    {diseases ? (
      <p className="text-3xl font-semibold mb-4">COVID-19 Disease Data <b>WIP</b></p> 
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
          <h3 className="text-xl font-semibold mb-2">Daily Death Count</h3>
            {todaysDeaths ? (
              <p>{todaysDeaths.Deaths} deaths</p>
            ) : (
              <p>No data available for {today}</p>
            )}
        </div>
        {/* Deaths This Month - not finished*/}
        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">Deaths This Month (WIP)</h3>
            {/* {monthlyDeaths ? (
              <p>{monthlyDeaths} deaths</p>
            ) : (
              <p>No data available for {specificMonth}</p>
            )} */}
        </div>
        <div className="bg-gray-200 p-4 rounded">
          <h3 className="text-xl font-semibold mb-2">% Change vs Last Month (WIP)</h3>
          <p>4.5%</p>
        </div>
      </div>
          
      {/* Vertical Bar Chart using recharts */}
      <div className="bg-gray-200 p-4 rounded mt-8">
        <h3 className="text-xl font-semibold mb-4">Number of New Cases This Month</h3>
        {filteredCaseReports.length > 0 ? (
          <ResponsiveContainer width="100%" height={400}>
            <BarChart width={600} height={300} data={chartData.sort((a, b) => new Date(a.date) - new Date(b.date))} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
              <XAxis dataKey="date" tick={{textAnchor: 'middle' }} tickFormatter={(tick) => new Date(tick).toLocaleDateString('en-US', { month: 'numeric', day: 'numeric' })} />
              <YAxis />
              <Tooltip position={{ y: 30 }} itemSorter={(item) => item.value} />
              <Legend />
              <Bar
                dataKey="numberOfNewCases"
                fill="#1B365D"
                stroke="#ffffff"
                strokeWidth={1}
                name="Reported New Cases"
              />
            </BarChart>
          </ResponsiveContainer>
        ) : (
          <p>No data available for {month}/{year}</p>
        )}
      </div>

    </div>
  );
};

export default COVIDInfo;
