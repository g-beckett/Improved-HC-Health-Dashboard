import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const MonthlyDeathChart = ({ chartData }) => {
  const [chartType, setChartType] = useState('race');

  const handleToggle = (type) => {
    setChartType(type);
  };

  return (
    <div>
      <div className='font-semibold'>
        <button className={`mr-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'grace' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('race')}>Race</button>
        <button className={`ml-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'age' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('age')}>Age</button>
      </div>
      <div className="flex mt-8">
      <div className="w-3/4 bg-gray-200 p-4 rounded">
        {/* <h3 className="text-xl font-semibold mb-4">Monthly Deaths</h3> */}
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            width={600}
            height={300}
            data={chartData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
          <XAxis
            dataKey="AnalyticsDate"
            tick={{ textAnchor: 'middle' }}
            tickFormatter={(tick) => new Date(tick).toLocaleDateString('en-US', { month: 'numeric', day: 'numeric' })}
          />
            <YAxis />
            <Tooltip />
            <Legend />
            {chartType === 'race' ? (
              <>
                <Bar dataKey="RaceWhiteCount" stackId="a" fill="#123D63" stroke="#ffffff" strokeWidth={1} name="White" />
                <Bar dataKey="RaceBlackCount" stackId="b" fill="#9BC6EC" stroke="#ffffff" strokeWidth={1} name="Black" />
                <Bar dataKey="RaceAsianCount" stackId="c" fill="#73AD70" stroke="#ffffff" strokeWidth={1} name="Asian" />
                <Bar dataKey="RaceNativeAmericanCount" stackId="d" fill="#3333FF" stroke="#ffffff" strokeWidth={1} name="Native American" />
                <Bar dataKey="RaceOtherCount" stackId="e" fill="#F79802" stroke="#ffffff" strokeWidth={1} name="Other" />
                <Bar dataKey="RaceUnknownCount" stackId="f" fill="#800000" stroke="#ffffff" strokeWidth={1} name="Unknown" />
              </>
            ) : (
              <>
                <Bar dataKey="Age_0_10_Count" stackId="a" fill="#66CCCC" stroke="#ffffff" strokeWidth={1} name="0-10" />
                <Bar dataKey="Age_11_20_Count" stackId="b" fill="#3399FF" stroke="#ffffff" strokeWidth={1} name="11-20" />
                <Bar dataKey="Age_21_30_Count" stackId="c" fill="#3366FF" stroke="#ffffff" strokeWidth={1} name="21-30" />
                <Bar dataKey="Age_31_40_Count" stackId="d" fill="#3333FF" stroke="#ffffff" strokeWidth={1} name="31-40" />
                <Bar dataKey="Age_41_50_Count" stackId="e" fill="#9933FF" stroke="#ffffff" strokeWidth={1} name="41-50" />
                <Bar dataKey="Age_51_60_Count" stackId="f" fill="#9900FF" stroke="#ffffff" strokeWidth={1} name="51-60" />
                <Bar dataKey="Age_61_70_Count" stackId="g" fill="#6600FF" stroke="#ffffff" strokeWidth={1} name="61-70" />
                <Bar dataKey="Age_71_80_Count" stackId="h" fill="#3300FF" stroke="#ffffff" strokeWidth={1} name="71-80" />
                <Bar dataKey="Age_81_Up_Count" stackId="i" fill="#330099" stroke="#ffffff" strokeWidth={1} name="81+" />
                <Bar dataKey="Age_Unknown_Count" stackId="j" fill="#800000" stroke="#ffffff" strokeWidth={1} name="Unknown" />
              </>
            )}
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div className="w-1/4 bg-gray-200 p-2 rounded">
          <ResponsiveContainer width="100%" height={350}>
          <h3 className="text-xl font-semibold">Ethnicity</h3>
            <PieChart>
              <Pie
                data={[
                  { name: 'Hispanic', value: chartData.reduce((acc, cur) => acc + cur.EthnicityHispanicCount, 0) },
                  { name: 'Not Hispanic', value: chartData.reduce((acc, cur) => acc + cur.EthnicityNonHispanicCount, 0) },
                  { name: 'Unknown Ethnicity', value: chartData.reduce((acc, cur) => acc + cur.EthnicityUnknownCount, 0) }
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

export default MonthlyDeathChart;
