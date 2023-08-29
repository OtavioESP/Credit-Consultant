import React from 'react';

const Input = ({ name, type, onChange, enabled }) => {
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


  return (
    <>
      {enabled ?
        <input
          placeholder={name}
          style={inputStyles}
          type={type}
          onChange={(e) => onChange(name, e.target.value)
          }
        />
        :
        ''
      }
    </>
  )
}

export default Input;
