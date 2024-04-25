import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';


const NewCasesChart = ({ chartData, yearData }) => {
  chartData = chartData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate));
  yearData = yearData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate));
  console.log(yearData);
  const [chartType, setChartType] = useState('monthly');
  
  const handleToggle = (type) => {
    setChartType(type);
  };

  // Aggregate data by month
  const aggregatedData = {};
  yearData.forEach(data => {
    const date = new Date(data.AnalyticsDate);
    const year = date.getFullYear();
    const month = `${(date.getMonth() + 1).toString().padStart(2, '0')}-${year}`;
    if (aggregatedData[month]) {
      aggregatedData[month].NumberOfNewCases += data.NumberOfNewCases || 0;
      aggregatedData[month].RaceWhiteCount += data.RaceWhiteCount || 0;
      aggregatedData[month].RaceBlackCount += data.RaceBlackCount || 0;
      aggregatedData[month].RaceAsianCount += data.RaceAsianCount || 0;
      aggregatedData[month].RaceNativeAmericanCount += data.RaceNativeAmericanCount || 0;
      aggregatedData[month].RaceOtherCount += data.RaceOtherCount || 0;
      aggregatedData[month].RaceUnknownCount += data.RaceUnknownCount || 0;
      aggregatedData[month].SexMaleCount += data.SexMaleCount || 0;
      aggregatedData[month].SexFemaleCount += data.SexFemaleCount || 0;
      aggregatedData[month].SexUnknownCount += data.SexUnknownCount || 0;
    } else {
      aggregatedData[month] = {
        AnalyticsDate: data.AnalyticsDate,
        NumberOfNewCases: data.NumberOfNewCases || 0,
        RaceWhiteCount: data.RaceWhiteCount || 0,
        RaceBlackCount: data.RaceBlackCount || 0,
        RaceAsianCount: data.RaceAsianCount || 0,
        RaceNativeAmericanCount: data.RaceNativeAmericanCount || 0,
        RaceOtherCount: data.RaceOtherCount || 0,
        RaceUnknownCount: data.RaceUnknownCount || 0,
        SexMaleCount: data.SexMaleCount || 0,
        SexFemaleCount: data.SexFemaleCount || 0,
        SexUnknownCount: data.SexUnknownCount || 0,
      };
      // console.log(aggregatedData[month]);
    }
  });

  const data = chartType === 'monthly' ? chartData : Object.values(aggregatedData);
  
  // Calculate total count for each category
  const totalMale = data.reduce((acc, cur) => acc + cur.SexMaleCount, 0);
  const totalFemale = data.reduce((acc, cur) => acc + cur.SexFemaleCount, 0);
  const totalUnknown = data.reduce((acc, cur) => acc + cur.SexUnknownCount, 0);

  // Calculate percentage values for each category
  const percentageMale = totalMale === 0 ? 0 : (totalMale / (totalMale + totalFemale + totalUnknown)) * 100;
  const percentageFemale = totalFemale === 0 ? 0 : (totalFemale / (totalMale + totalFemale + totalUnknown)) * 100;
  const percentageUnknown = totalUnknown === 0 ? 0 : (totalUnknown / (totalMale + totalFemale + totalUnknown)) * 100;

  return (
    <div>
      <div className='font-semibold'>
        <button className={`mr-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'monthly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('monthly')}>Past 30 Days</button>
        <button className={`ml-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'yearly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('yearly')}>Monthly</button>
      </div>
      <div className="flex mt-8">
      <div className="w-1/4 bg-gray-200 p-2 rounded">
          <ResponsiveContainer width="100%" height={350}>
          <h3 className="text-xl font-semibold">Sex</h3>
            <PieChart>
              <Pie
                data={[
                  { name: 'HIV/Aids', value: percentageMale },
                  { name: 'Syphilis', value: percentageFemale },
                  { name: 'Gonorrhea', value: percentageUnknown }
                  { name: 'Chlamydia', value: percentageUnknown }
                ]}
                cx="50%"
                cy="50%"
                outerRadius={90}
                innerRadius={50}
                fill="#8884d8"
                paddingAngle={1}
                label={({ value }) => `${(value).toFixed(2)}%`}
              >
                {[
                  '#123D63',
                  '#9BC6EC',
                  '#F79802'
                ].map((color, index) => (
                  <Cell key={index} fill={color} />
                ))}
              </Pie>
              <Legend />
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default STIPieChart;
