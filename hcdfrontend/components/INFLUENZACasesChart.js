import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, Brush } from 'recharts';

const NewCasesChart = ({ chartData, yearData, allData }) => {
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
  const data = chartType === 'monthly' 
    ? chartData : chartType === 'yearly' ? Object.values(aggregatedData) : allData;

  return (
    <div>
      <div className='font-semibold'>
        <button className={`mr-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'monthly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('monthly')}>Monthly</button>
        <button className={`mr-2 ml-2 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'yearly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('yearly')}>Yearly</button>
        <button className={`ml-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'all' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('all')}>All Time</button>
      </div>
      <div className="flex mt-8">
        <div className="w-full bg-gray-200 p-4 rounded">
          <ResponsiveContainer width="100%" height={400}>
            <BarChart
              width={650}
              height={300}
              data={data}
              margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              scrollable={true}
            >
              <XAxis
                dataKey="AnalyticsDate"
                tick={{ textAnchor: 'middle', fontSize: 12}}
                minTickGap={0}
                tickFormatter={(tick) => {
                  if (chartType === 'monthly') {
                    return new Date(`${tick}`).toLocaleDateString('en-US', { day: 'numeric'});
                  } else if (chartType === 'yearly') {
                    return new Date(`${tick}`).toLocaleDateString('en-US', { month: 'long' });
                  } else {
                    return new Date(`${tick}`).toLocaleDateString('en-US', { day:'numeric', month: 'numeric' });
                  }
                }}/>
              <YAxis tickFormatter={(tick) => tick.toLocaleString()} />
              <Tooltip formatter={(value) => value.toLocaleString()} position={{y: 30}}/>
              <Legend />
              <Bar dataKey="NumberOfNewCases" stackId="a" fill="#123D63" stroke="#123D63" strokeWidth={1} name="Reported New Cases" />
              {/* <Bar dataKey="RaceWhiteCount" stackId="a" fill="#123D63" stroke="#ffffff" strokeWidth={1} name="White" />
              <Bar dataKey="RaceBlackCount" stackId="a" fill="#9BC6EC" stroke="#ffffff" strokeWidth={1} name="Black" />
              <Bar dataKey="RaceAsianCount" stackId="a" fill="#73AD70" stroke="#ffffff" strokeWidth={1} name="Asian" />
              <Bar dataKey="RaceNativeAmericanCount" stackId="a" fill="#3333FF" stroke="#ffffff" strokeWidth={1} name="Native American" />
              <Bar dataKey="RaceOtherCount" stackId="a" fill="#F79802" stroke="#ffffff" strokeWidth={1} name="Other" />
              <Bar dataKey="RaceUnknownCount" stackId="a" fill="#800000" stroke="#ffffff" strokeWidth={1} name="Unknown" /> */}
              </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default NewCasesChart;
