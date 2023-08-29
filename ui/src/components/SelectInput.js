import React, { useState } from 'react';

const SelectInput = ({ name, options, onChange }) => {
  const inputStyles = {
    width: '300px',
    height: '40px',
    borderTop: 'none',
    borderLeft: 'none',
    borderRight: 'none',
    borderBottom: '1px solid gray',
    paddingLeft: '10px',
    outline: 'none',
  };

  const [selectedOption, setSelectedOption] = useState('');

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
    onChange(name, event.target.value);
  };

  return (
    <select
      style={inputStyles}
      value={selectedOption}
      onChange={handleOptionChange}
    >
      <option value="">Selecione uma opção</option>
      {
        options.map((option) => (
          <option key={option.id} value={option.id}>
            {option.full_name}
          </option>
        ))
      }
    </select >
  )
}

export default SelectInput;
