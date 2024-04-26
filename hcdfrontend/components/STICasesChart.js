import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const NewCasesChart = ({ chartData, yearData }) => {
  chartData = chartData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate));
  yearData = yearData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate));

  const [chartType, setChartType] = useState('monthly');

  const handleToggle = (type) => {
    setChartType(type);
  };

  const diseases = ['Chlamydia', 'HIV/AIDS', 'Syphilis', 'Gonorrhea'];
  const colors = ['#123D63', '#800000', '#73AD70', '#3333FF', '#F79802', '#9BC6EC']

  // Aggregate data based on chartType
  const aggregatedData = {};
  if (chartType === 'monthly') {
    chartData.forEach(data => {
      const date = new Date(data.AnalyticsDate);
      const day = date.toLocaleDateString();
      if (!aggregatedData[day]) {
        aggregatedData[day] = {};
        diseases.forEach(disease => {
          aggregatedData[day][`${disease}_Cases`] = 0;
        });
      }
      diseases.forEach(disease => {
        aggregatedData[day][`${disease}_Cases`] += data.Disease === disease ? (data.NumberOfNewCases || 0) : 0;
      });
    });
  } else {
    yearData.forEach(data => {
      const date = new Date(data.AnalyticsDate);
      const year = date.getFullYear();
      const month = `${(date.getMonth() + 1).toString().padStart(2, '0')}/${year}`;
      if (!aggregatedData[month]) {
        aggregatedData[month] = { AnalyticsDate: data.AnalyticsDate };
        diseases.forEach(disease => {
          aggregatedData[month][`${disease}_Cases`] = 0;
        });
      }
      aggregatedData[month][`${data.Disease}_Cases`] = (aggregatedData[month][`${data.Disease}_Cases`] || 0) + (data.NumberOfNewCases || 0);
    });
  }

  // Convert aggregatedData to array format for recharts
  const data = Object.entries(aggregatedData).map(([date, cases]) => ({ date, ...cases }));

  return (
    <div>
      <div className='font-semibold'>
        <button className={`mr-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'monthly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('monthly')}>Past 30 Days</button>
        <button className={`ml-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'yearly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('yearly')}>Monthly</button>
      </div>
      <div className="flex mt-8">
        <div className="w-full bg-gray-200 p-2 rounded">
          <ResponsiveContainer width="100%" height={400}>
            <BarChart
              width={650}
              height={300}
              data={data}
              margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              scrollable={true}
            >
              <XAxis
                dataKey="date"
                tick={{ textAnchor: 'middle', fontSize: 12}}
                minTickGap={0}
                tickFormatter={(tick) => {
                  if (chartType === 'monthly') {
                    return new Date(tick).toLocaleDateString('en-US', { day: 'numeric' });
                  } else {
                    const [month, year] = tick.split('/');
                    return `${new Date(`${month}/01/${year}`).toLocaleDateString('en-US', { month: 'long' })}`;
                  }
                }}
              />
              <YAxis tickFormatter={(tick) => tick.toLocaleString()} />
              <Tooltip formatter={(value) => value.toLocaleString()} position={{ y: 30 }}/>
              <Legend />
              {diseases.map((disease, index) => (
                <Bar key={index} dataKey={`${disease}_Cases`} stackId="a" fill={colors[index]} stroke="#ffffff" strokeWidth={1} name={disease} />
              ))}
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default NewCasesChart;
