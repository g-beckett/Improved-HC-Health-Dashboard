import React from 'react';
import { useState } from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts';

const PieCharts = ({ chartData }) => {
  const [chartType, setChartType] = useState('yearly');

  const handleToggle = (type) => {
    setChartType(type);
  };

  const diseases = ['Chlamydia', 'HIV/AIDS', 'Syphilis', 'Gonorrhea'];

  // Aggregate demographic data for each disease
  const aggregatedData = diseases.map((disease) => {
    const diseaseData = chartData.filter((report) => report.Disease === disease);
    const aggregatedCounts = {
      RaceWhiteCount: 0,
      RaceBlackCount: 0,
      RaceOtherCount: 0,
    };

    diseaseData.forEach((report) => {
      aggregatedCounts.RaceWhiteCount += report.RaceWhiteCount || 0;
      aggregatedCounts.RaceBlackCount += report.RaceBlackCount || 0;
      aggregatedCounts.RaceOtherCount += report.RaceOtherCount || 0;
    });

    // Calculate total count for each disease
    const totalCount = Object.values(aggregatedCounts).reduce((acc, curr) => acc + curr, 0);

    // Calculate percentages
    const percentageData = {
      RaceWhiteCount: (aggregatedCounts.RaceWhiteCount / totalCount) * 100,
      RaceBlackCount: (aggregatedCounts.RaceBlackCount / totalCount) * 100,
      RaceOtherCount: (aggregatedCounts.RaceOtherCount / totalCount) * 100,
    };

    return {
      name: disease,
      data: percentageData,
    };
  });

  return (
    <div className="flex">
      {aggregatedData.map((item, index) => (
        <div key={index} className="w-1/4 p-4">
          <h3 className="text-center mb-2">{item.name}</h3>
          <ResponsiveContainer width="100%" height={200}>
            <PieChart>
              <Pie
                data={[
                  { name: 'White', value: item.data.RaceWhiteCount || 0 }, 
                  { name: 'Black', value: item.data.RaceBlackCount || 0 },
                  { name: 'Other', value: item.data.RaceOtherCount || 0 }
                ]}
                cx="50%"
                cy="50%"
                outerRadius={60}
                innerRadius={30}
                fill="#8884d8"
                paddingAngle={2}
                label={({ value }) => `${value.toFixed(2)}%`}
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
      ))}
    </div>
  );
};

export default PieCharts;
