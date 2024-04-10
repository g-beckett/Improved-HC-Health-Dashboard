import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const MonthlyDeathChart = ({ chartData , allData }) => {
  const [chartType, setChartType] = useState('yearly');

  const handleToggle = (type) => {
    setChartType(type);
  };

  // Aggregate data by month
  const aggregatedData = {};
  allData.forEach(data => {
    const date = new Date(data.AnalyticsDate);
    const year = date.getFullYear();
    const month = `${(date.getMonth() + 1).toString().padStart(2, '0')}-${year}`;
    if (aggregatedData[month]) {
      aggregatedData[month].Deaths += data.Deaths || 0;
    } else {
      aggregatedData[month] = {
        AnalyticsDate: data.AnalyticsDate,
        Deaths: data.NumberOfNewCases || 0,
      };
      // console.log(aggregatedData[month]);
    }
  });

  const data = chartType === 'yearly' ? chartData : Object.values(aggregatedData);
  return (
    <div>
      <div className='font-semibold'>
        <button className={`mr-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'yearly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('yearly')}>This Year</button>
        <button className={`ml-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'all' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('all')}>All Time</button>
      </div>
      <div className="flex mt-8">
      <div className="w-full bg-gray-200 p-4 rounded">
        {/* <h3 className="text-xl font-semibold mb-4">Monthly Deaths</h3> */}
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            width={600}
            height={300}
            data={data}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
          <XAxis
            dataKey="AnalyticsDate"
            tick={{ textAnchor: 'middle', fontSize: 8 }}
            minTickGap={1}
            tickFormatter={(tick) => {
              if (chartType === 'yearly') {
                return new Date(`${tick}`).toLocaleDateString('en-US', { month: 'numeric', day: 'numeric'});
              } else {
                return new Date(`${tick}`).toLocaleDateString('en-US', { month: 'numeric', year:'numeric' });
              }
            }}/>
            <YAxis tickFormatter={(tick) => tick.toLocaleString()} />
            <Tooltip position={{y: 30}} formatter={(value) => value.toLocaleString()} />
            <Legend />
            <Bar dataKey="Deaths" stackId="a" fill="#123D63" name="Reported Deaths" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
    </div>
  );
};

export default MonthlyDeathChart;
