import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const COVIDHospitalizationChart = ({ chartData, today }) => {
  chartData = chartData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate));
  // extract years from the chart data
  const years = Array.from(new Set(chartData.map(data => new Date(data.AnalyticsDate).getFullYear())));
  
  const [currentYearIndex, setCurrentYearIndex] = useState(years.findIndex(year => year === today.getFullYear()));
  const currentYear = years[currentYearIndex];

  const handlePrevYear = () => {
    setCurrentYearIndex((prevIndex) => prevIndex === 0 ? years.length - 1 : prevIndex - 1);
  };

  const handleNextYear = () => {
    setCurrentYearIndex((prevIndex) => (prevIndex + 1) % years.length);
  };

  // Aggregate data by month
  const aggregatedData = {};
  console.log(chartData);
  chartData.forEach(data => {
    const date = new Date(data.AnalyticsDate);
    const year = date.getFullYear();
    const month = `${(date.getMonth() + 1).toString().padStart(2, '0')}-${year}`;
    if (aggregatedData[month]) {
      aggregatedData[month].HospitalizedInpatientsInHamiltonCounty += data.HospitalizedInpatientsInHamiltonCounty || 0;
      aggregatedData[month].HospitalizedPeopleUnderInvestigationInHamiltonCounty += data.HospitalizedPeopleUnderInvestigationInHamiltonCounty || 0;
      aggregatedData[month].HospitalizedICUInHamiltonCounty += data.HospitalizedICUInHamiltonCounty || 0;
    } else {
      aggregatedData[month] = {
        AnalyticsDate: date.toLocaleDateString(),
        HospitalizedInpatientsInHamiltonCounty: data.HospitalizedInpatientsInHamiltonCounty || 0,
        HospitalizedPeopleUnderInvestigationInHamiltonCounty: data.HospitalizedPeopleUnderInvestigationInHamiltonCounty || 0,
        HospitalizedICUInHamiltonCounty: data.HospitalizedICUInHamiltonCounty || 0,
      };
    }
    // console.log(aggregatedData[month]);
  });

  // Convert aggregated data object to an array of objects
  const groupedChartData = Object.values(aggregatedData);

  return (
    <div>
      <div className="flex justify-center items-center mb-4">
        <button className="mr-4 bg-TN-lightblue hover:bg-TN-blue text-white font-bold py-2 px-4 rounded" onClick={handlePrevYear}>&lt;</button>
        <h2 className="text-xl font-semibold">{currentYear}</h2>
        <button className="ml-4 bg-TN-lightblue hover:bg-TN-blue text-white font-bold py-2 px-4 rounded" onClick={handleNextYear}>&gt;</button>
      </div>
      <div className="bg-gray-200 p-4 rounded mt-8">
        <ResponsiveContainer width="100%" height={400}>
            <BarChart
              width={650}
              height={300}
              data={groupedChartData.filter(data => new Date(data.AnalyticsDate).getFullYear() === currentYear)}
              margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              scrollable={true}
            >
            <XAxis
              dataKey="AnalyticsDate"
              tick={{ textAnchor: 'middle', fontSize: 14}}
              tickFormatter={(tick) => new Date(tick).toLocaleDateString('en-US', { month: 'long'})}
            />
            <YAxis />
            <Tooltip position= {{ y: 30}} labelFormatter={(label) => new Date(label).toLocaleDateString('en-US', { month: 'long', year: 'numeric' })} />
            <Legend />
            <Bar dataKey="HospitalizedInpatientsInHamiltonCounty" fill="#9BC6EC" stroke="#A0AEC0" strokeWidth={1} name="Inpatients" />
            <Bar dataKey="HospitalizedPeopleUnderInvestigationInHamiltonCounty" fill="#123D63" stroke="#A0AEC0" strokeWidth={1} name="People under Investigation" />
            <Bar dataKey="HospitalizedICUInHamiltonCounty" fill="#F79802" stroke="#A0AEC0" strokeWidth={1} name="ICU Patients" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default COVIDHospitalizationChart;
