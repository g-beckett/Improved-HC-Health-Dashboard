import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const PieCharts = ({ chartData , allData }) => {
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
  //new
  const data = chartType === 'yearly' ? chartData : Object.values(aggregatedData);
  const PieCharts = (chartData) => {
    const data = [
      { name: 'white', value: 400 },
      { name: 'black', value: 300 },
      { name: 'other', value: 300 },
    ];
  // Filter CaseReports for the specific month and year
 // const filteredCaseReports = caseReports.filter(report => {
   // const reportDate = new Date(report.AnalyticsDate);
    //const reportMonth = (reportDate.getMonth() + 1).toString().padStart(2, '0'); 
    //const reportYear = reportDate.getFullYear().toString();
    //return report.Disease === month && reportYear === year;
  //});

  //comment above out
    return (
      <div className="flex">
        {['Chlamydia', 'HIV/AIDs', 'Syphilis', 'Gonnorhea'].map((chartNum) => (
          <div key={chartNum} className="w-1/4 p-4">
            <h3 className="text-center"> {chartNum}</h3>
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

  // Aggregate data by month
 
  return (
    <div className="flex">
      {['Chlamydia', 'HIV/AIDs', 'Syphilis', 'Gonnorhea'].map((chartNum) => (
        <div key={chartNum} className="w-1/4 p-4">
          <h3 className="text-center"> {chartNum}</h3>
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
