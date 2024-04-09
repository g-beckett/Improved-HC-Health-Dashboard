  import React, { useState } from 'react';
  import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

  const ComparisonChart = ({ chartData }) => {
    chartData = chartData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate));
    // Extract years from the chart data
    const years = Array.from(new Set(chartData.map(data => new Date(data.AnalyticsDate).getFullYear())));

    // Aggregate data by month
    const aggregatedData = {};
    chartData.forEach(data => {
      const date = new Date(data.AnalyticsDate);
      const year = date.getFullYear();
      const month = date.getMonth() + 1; // Month index starts from 0
      if (aggregatedData[month]) {
        if (aggregatedData[month][year]) {
          aggregatedData[month][year].push(data);
        } else {
          aggregatedData[month][year] = [data];
        }
      } else {
        aggregatedData[month] = { [year]: [data] };
      }
    });

    // Generate data array for each month containing the total number of new cases
    const monthlyChartData = [];
    for (let month = 1; month <= 12; month++) {
      const monthData = { name: month };
      years.forEach(year => {
        if (aggregatedData[month] && aggregatedData[month][year]) {
          const totalNewCases = aggregatedData[month][year].reduce((acc, cur) => acc + cur.NumberOfNewCases, 0);
          monthData[year] = totalNewCases;
        } else {
          monthData[year] = null;
        }
      });
      monthlyChartData.push(monthData);
    }

    const lineColors = ['#123D63', '#800000', '#73AD70', '#3333FF', '#F79802', '#9BC6EC']

    return (
      <div>
        <div className="bg-gray-200 p-4 rounded mt-8">
          <ResponsiveContainer width="100%" height={600}>
            <LineChart
              data={monthlyChartData}
              margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              scrollable={true}
            >
              <XAxis
                dataKey="name"
                tick={{ textAnchor: 'middle', fontSize: 14 }}
                tickFormatter={(month) => new Date(2022, month - 1).toLocaleString('en-US', { month: 'long' })}
              />
              <YAxis tickFormatter={(tick) => tick.toLocaleString()} />
              <Tooltip formatter={(value) => value.toLocaleString()} position={{ y: 30 }} labelFormatter={(value) => new Date(2022, value - 1).toLocaleString('en-US', { month: 'long' })} />
              <Legend />
              {years.map((year, index) => (
                <Line
                  key={index}
                  dataKey={year}
                  type="monotone"
                  stroke={lineColors[index % lineColors.length]}
                  strokeWidth={3}
                  name={`Cases (${year})`}
                />
              ))}
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    );
  };

  export default ComparisonChart;
