import React, { useState } from 'react';
import StyledInput from './Input';
import StyledButton from './Button';
import { makeFinancialProposal } from '../services/services';

function Container() {

  const divStyles = {
    width: '400px',
    height: 'fit-content',
    backgroundColor: 'white',
    borderRadius: '30px',
    boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.5)', // Adjust shadow as needed
    margin: '20px auto', // Adjust margin as needed
  };

  const divFormStyles = {
    padding: '30px',
    display: 'flex',
    flexDirection: 'column',
    gap: '30px',
    alignItems: 'center'

  }


  const [formData, setFormData] = useState({});

  const handleFormChange = (name, value) => {
    setFormData({ ...formData, [name]: value })
  }

  const onFormSave = () => {
    console.log('aa')
    makeFinancialProposal(formData).then(res => console.log(res))
  }


  console.log(formData)

  return (
    <div style={divStyles}>
      <div style={divFormStyles}>
        <StyledInput
          name={"otavio"}
          onChange={handleFormChange}
        />
        <StyledInput
          name={"lesly"}
          onChange={handleFormChange}
        />
        <StyledInput
          name={"teste"}
          onChange={handleFormChange}
        />

        <StyledButton onConfirm={onFormSave}> Clique em mim </StyledButton>
      </div>
    </div>
  );
}

export default Container;
