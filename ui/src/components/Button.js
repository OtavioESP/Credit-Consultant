import React from 'react';

function StyledButton({ onConfirm, children }) {
  const buttonStyles = {
    width: '150px',
    height: '40px',
    backgroundColor: '#359edb',
    color: 'white',
    borderRadius: '20px',
    border: 'none',
    boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.5)',
    cursor: 'pointer',
  };

  return (
    <button style={buttonStyles} onClick={() => onConfirm()}>{children}</button>
  );
}

export default StyledButton;
