import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const NewCasesChart = ({ chartData, yearData }) => {
  const [chartType, setChartType] = useState('monthly');

  const handleToggle = (type) => {
    setChartType(type);
  };

  const data = chartType === 'monthly' ? chartData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate)) : yearData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate));


  return (
    <div>
      <div className='font-semibold'>
        <button className={`mr-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'monthly' ? 'bg-TN-blue' : 'bg-blue-500'}`} onClick={() => handleToggle('monthly')}>Monthly</button>
        <button className={`ml-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'yearly' ? 'bg-TN-blue' : 'bg-blue-500'}`} onClick={() => handleToggle('yearly')}>Yearly</button>
      </div>
      <div className="flex mt-8">
        <div className="w-3/4 bg-gray-200 p-4 rounded">
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
                tick={{ textAnchor: 'middle', fontSize: 14}}
                tickFormatter={(tick) => new Date(tick).toLocaleDateString('en-US', { month: 'numeric', day: 'numeric' })}
              />
              <YAxis />
              <Tooltip position={{y: 30}}/>
              <Legend />
              <Bar dataKey="NumberOfNewCases" fill="#1B365D" stroke="#ffffff" strokeWidth={1} name="Reported New Cases" />
            </BarChart>
          </ResponsiveContainer>
        </div>
        <div className="w-1/4 bg-gray-200 p-2 rounded">
          <ResponsiveContainer width="100%" height={350}>
          <h3 className="text-xl font-semibold">Sex</h3>
            <PieChart>
              <Pie
                data={[
                  { name: 'Male', value: data.reduce((acc, cur) => acc + cur.SexMaleCount, 0) },
                  { name: 'Female', value: data.reduce((acc, cur) => acc + cur.SexFemaleCount, 0) },
                  { name: 'Unknown', value: data.reduce((acc, cur) => acc + cur.SexUnknownCount, 0) }
                ]}
                cx="50%"
                cy="50%"
                outerRadius={100}
                innerRadius={60}
                fill="#8884d8"
                paddingAngle={1}
                label
              >
                {[
                  '#1B365D',
                  '#EE3524',
                  '#FF9933'
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

export default NewCasesChart;
