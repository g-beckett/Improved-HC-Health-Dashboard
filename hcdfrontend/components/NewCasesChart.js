import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const NewCasesChart = ({ chartData, yearData }) => {
  const [chartType, setChartType] = useState('monthly');

  const handleToggle = (type) => {
    setChartType(type);
  };

  return (
    <div>
      <div className='font-semibold'>
        <button className='mr-4 text-md' onClick={() => handleToggle('monthly')}>Monthly</button>
        <button className='ml-4 text-md' onClick={() => handleToggle('yearly')}>Yearly</button>
      </div>
      <div className="bg-gray-200 p-4 rounded mt-8">
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            width={650}
            height={300}
            data={chartType === 'monthly' ? chartData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate)) : yearData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate))}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
            scrollable={true}
          >
          <XAxis
            dataKey="AnalyticsDate"
            tick={{ textAnchor: 'middle', fontSize: 14}}
            tickFormatter={(tick) => new Date(tick).toLocaleDateString('en-US', { month: 'numeric', day: 'numeric' })}
          />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="NumberOfNewCases" fill="#1B365D" stroke="#ffffff" strokeWidth={1} name="Reported New Cases" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default NewCasesChart;
