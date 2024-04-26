import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const STIChart = ({ chartData, allData }) => {
  const [chartType, setChartType] = useState('yearly');

  const handleToggle = (type) => {
    setChartType(type);
  };

  const aggregateData = (data, type) => {
    if (type === 'yearly') {
      const currentDate = new Date();
      const pastYearDate = new Date(currentDate.getFullYear() - 1, currentDate.getMonth(), currentDate.getDate());

      return data.filter(item => new Date(item.AnalyticsDate) >= pastYearDate);
    } else if (type === 'all') {
      // Return all data without filtering
      return data;
    }
    return data;
  };

  const data = chartType === 'monthly'
    ? chartData
    : chartType === 'yearly'
      ? aggregateData(chartData, 'yearly')
      : aggregateData(allData, 'all');

  return (
    <div>
      <div className='font-semibold'>
        <button
          className={`mr-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'yearly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`}
          onClick={() => handleToggle('yearly')}
        >
          This Year
        </button>
        <button
          className={`ml-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'all' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`}
          onClick={() => handleToggle('all')}
        >
          All Time
        </button>
      </div>
      <div className="flex mt-8">
        <div className="w-full bg-gray-200 p-4 rounded">
          <ResponsiveContainer width="100%" height={400}>
            <BarChart
              width={600}
              height={300}
              data={data}
              margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
            >
              <XAxis
                dataKey="AnalyticsDate"
                tick={{ textAnchor: 'middle', fontSize: 9 }}
                minTickGap={1}
                tickFormatter={(tick) => {
                  if (chartType === 'yearly') {
                    return new Date(`${tick}`).toLocaleDateString('en-US', { month: 'numeric', day: 'numeric' });
                  } else {
                    return new Date(`${tick}`).toLocaleDateString('en-US', { month: 'numeric', year: 'numeric' });
                  }
                }}
              />
              <YAxis tickFormatter={(tick) => tick.toLocaleString()} />
              <Tooltip position={{ y: 30 }} formatter={(value) => value.toLocaleString()} />
              <Legend />
              <Bar dataKey="HIVCases" stackId="a" fill="#123D63" name="HIV/Aids" />
              <Bar dataKey="SyphiilisCases" stackId="a" fill="#73AD70" name="Syphilis" />
              <Bar dataKey="GonnorheaCases" stackId="a" fill="#9BC6EC" name="Gonnorhea" />
              <Bar dataKey="ChlamydiaCases" stackId="ada" fill="#F79802" name="Chlamydia" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default STIChart;
