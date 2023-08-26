import React from 'react';

function StyledInput({ name, onChange }) {
  const inputStyles = {
    width: '300px',
    height: '40px',
    borderTop: 'none', // No border on top
    borderLeft: 'none', // No border on left
    borderRight: 'none', // No border on right
    borderBottom: '1px solid gray', // Border only at the bottom
    paddingLeft: '10px',
    outline: 'none', // Remove default focus outline
  };


  return (
    <input
      type="text"
      placeholder={name}
      style={inputStyles}
      onChange={(e) => onChange(name, e.target.value)}
    />
  );
}

export default StyledInput;
