import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';

const PieCharts = () => {
  const data = [
    { name: 'white', value: 400 },
    { name: 'black', value: 300 },
    { name: 'other', value: 300 },
  ];

  return (
    <div className="flex">
      {[1, 2, 3, 4].map((chartNum) => (
        <div key={chartNum} className="w-1/4 p-4">
          <h3 className="text-center">Chart {chartNum}</h3>
          <ResponsiveContainer width="100%" height={200}>
            <PieChart>
              <Pie
                data={data}
                cx="50%"
                cy="50%"
                innerRadius={60}
                outerRadius={80}
                fill="#8884d8"
                paddingAngle={5}
                dataKey="value"
              >
                {data.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={['#0088FE', '#00C49F', '#FFBB28'][index % 3]} />
                ))}
              </Pie>
            </PieChart>
          </ResponsiveContainer>
        </div>
      ))}
    </div>
  );
};

export default PieCharts;
