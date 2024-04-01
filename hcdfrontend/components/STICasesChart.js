import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const NewCasesChart = ({ chartData, yearData }) => {
  chartData = chartData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate));
  yearData = yearData.sort((a, b) => new Date(a.AnalyticsDate) - new Date(b.AnalyticsDate));
  console.log(yearData);
  const [chartType, setChartType] = useState('monthly');
  
  const handleToggle = (type) => {
    setChartType(type);
  };
  
//   const getWeekNumber = (date) => {
//     const onejan = new Date(date.getFullYear(), 0, 1);
//     const millisecsInDay = 86400000;
//     const daysOffset = (onejan.getDay() - 1 + 7) % 7;
//     const weekNo = Math.floor(((date - onejan) / millisecsInDay + daysOffset) / 7) + 1;
//     if (weekNo === 53) {
//       return 1; // Adjust week number to 1 for the last week of the year
//     }

//     return weekNo;
// };

  //kept for possible later use
  // const groupByWeek = (data) => {
  //   const groupedData = {};
  //   data.forEach(report => {
  //     const date = new Date(report.AnalyticsDate);
  //     const weekNumber = `Week ${getWeekNumber(date)}`;
  //     if (!groupedData[weekNumber]) {
  //       groupedData[weekNumber] = {
  //         AnalyticsDate: weekNumber,
  //         NumberOfNewCases: 0,
  //         RaceWhiteCount: 0,
  //         RaceBlackCount: 0,
  //         RaceAsianCount: 0,
  //         RaceNativeAmericanCount: 0,
  //         RaceOtherCount: 0,
  //         RaceUnknownCount: 0,
  //         SexMaleCount: 0,
  //         SexFemaleCount: 0,
  //         SexUnknownCount: 0,
  //       };
  //     }
  //     groupedData[weekNumber].NumberOfNewCases += report.NumberOfNewCases || 0;
  //     groupedData[weekNumber].RaceWhiteCount += report.RaceWhiteCount || 0;
  //     groupedData[weekNumber].RaceBlackCount += report.RaceBlackCount || 0;
  //     groupedData[weekNumber].RaceAsianCount += report.RaceAsianCount || 0;
  //     groupedData[weekNumber].RaceNativeAmericanCount += report.RaceNativeAmericanCount || 0;
  //     groupedData[weekNumber].RaceOtherCount += report.RaceOtherCount || 0;
  //     groupedData[weekNumber].RaceUnknownCount += report.RaceUnknownCount || 0;
  //     groupedData[weekNumber].SexMaleCount += report.SexMaleCount || 0;
  //     groupedData[weekNumber].SexFemaleCount += report.SexFemaleCount || 0;
  //     groupedData[weekNumber].SexUnknownCount += report.SexUnknownCount || 0;
  //   });
  //   // console.log(Object.values(groupedData));
  //   return Object.values(groupedData);
  // };


  // Aggregate data by month
  const aggregatedData = {};
  yearData.forEach(data => {
    const date = new Date(data.AnalyticsDate);
    const year = date.getFullYear();
    const month = `${(date.getMonth() + 1).toString().padStart(2, '0')}-${year}`;
    if (aggregatedData[month]) {
      aggregatedData[month].NumberOfNewCases += data.NumberOfNewCases || 0;
      aggregatedData[month].RaceWhiteCount += data.RaceWhiteCount || 0;
      aggregatedData[month].RaceBlackCount += data.RaceBlackCount || 0;
      aggregatedData[month].RaceAsianCount += data.RaceAsianCount || 0;
      aggregatedData[month].RaceNativeAmericanCount += data.RaceNativeAmericanCount || 0;
      aggregatedData[month].RaceOtherCount += data.RaceOtherCount || 0;
      aggregatedData[month].RaceUnknownCount += data.RaceUnknownCount || 0;
      aggregatedData[month].SexMaleCount += data.SexMaleCount || 0;
      aggregatedData[month].SexFemaleCount += data.SexFemaleCount || 0;
      aggregatedData[month].SexUnknownCount += data.SexUnknownCount || 0;
    } else {
      aggregatedData[month] = {
        AnalyticsDate: data.AnalyticsDate,
        NumberOfNewCases: data.NumberOfNewCases || 0,
        RaceWhiteCount: data.RaceWhiteCount || 0,
        RaceBlackCount: data.RaceBlackCount || 0,
        RaceAsianCount: data.RaceAsianCount || 0,
        RaceNativeAmericanCount: data.RaceNativeAmericanCount || 0,
        RaceOtherCount: data.RaceOtherCount || 0,
        RaceUnknownCount: data.RaceUnknownCount || 0,
        SexMaleCount: data.SexMaleCount || 0,
        SexFemaleCount: data.SexFemaleCount || 0,
        SexUnknownCount: data.SexUnknownCount || 0,
      };
      // console.log(aggregatedData[month]);
    }
  });
  const data = chartType === 'monthly' ? chartData : Object.values(aggregatedData);

  return (
    <div>
      <div className='font-semibold'>
        <button className={`mr-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'monthly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('monthly')}>Monthly</button>
        <button className={`ml-4 hover:bg-TN-blue text-white py-2 px-4 rounded ${chartType === 'yearly' ? 'bg-TN-blue' : 'bg-TN-lightblue'}`} onClick={() => handleToggle('yearly')}>Yearly</button>
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
                tick={{ textAnchor: 'middle', fontSize: 10}}
                minTickGap={0}
                tickFormatter={(tick) => {
                  if (chartType === 'monthly') {
                    return new Date(`${tick}`).toLocaleDateString('en-US', { month: 'numeric', day: 'numeric'});
                  } else {
                    return new Date(`${tick}`).toLocaleDateString('en-US', { month: 'long' });
                  }
                }}/>
              <YAxis />
              <Tooltip position={{y: 30}}/>
              <Legend />
              {/* <Bar dataKey="NumberOfNewCases" hide={true} stackId="a" fill="#000000" stroke="#ffffff" strokeWidth={1} name="Reported New Cases" /> */}
              <Bar dataKey="RaceWhiteCount" stackId="a" fill="#123D63" stroke="#ffffff" strokeWidth={1} name="White" />
              <Bar dataKey="RaceBlackCount" stackId="a" fill="#9BC6EC" stroke="#ffffff" strokeWidth={1} name="Black" />
              <Bar dataKey="RaceAsianCount" stackId="a" fill="#73AD70" stroke="#ffffff" strokeWidth={1} name="Asian" />
              <Bar dataKey="RaceNativeAmericanCount" stackId="a" fill="#3333FF" stroke="#ffffff" strokeWidth={1} name="Native American" />
              <Bar dataKey="RaceOtherCount" stackId="a" fill="#F79802" stroke="#ffffff" strokeWidth={1} name="Other" />
              <Bar dataKey="RaceUnknownCount" stackId="a" fill="#800000" stroke="#ffffff" strokeWidth={1} name="Unknown" />
              </BarChart>
          </ResponsiveContainer>
        </div>
        <div className="w-1/4 bg-gray-200 p-2 rounded">

        </div>
      </div>
    </div>
  );
};

export default CasesChart;
