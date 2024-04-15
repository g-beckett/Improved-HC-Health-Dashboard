import React from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

const Datepicker = ({ selectedDate, handleDateChange }) => {
  return (
    <div className="flex items-center justify-center mt-2">
      <DatePicker
        selected={selectedDate}
        onChange={date => handleDateChange(date)}
        dateFormat="MM/dd/yyyy"
        className='rounded-md text-center'
      />
    </div>
  );
};

export default Datepicker;
