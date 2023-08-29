import React, { useEffect, useState } from 'react';
import Input from './Input';
import Button from './Button';
import { createFinancialProposal, fetchFields, fetchPersons } from '../services/services';
import SelectInput from './SelectInput';
import { toast } from 'react-toastify';

const Container = () => {

  const divStyles = {
    width: '400px',
    height: 'fit-content',
    backgroundColor: 'white',
    borderRadius: '30px',
    boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.5)',
    margin: '20px auto',
  };

  const divFormStyles = {
    padding: '30px',
    display: 'flex',
    flexDirection: 'column',
    gap: '30px',
    alignItems: 'center'
  };


  const [formData, setFormData] = useState({});
  const [formFields, setFormFields] = useState([{}])
  const [persons, setPersons] = useState([{}])

  const handleFormChange = (name, value) => {
    setFormData({ ...formData, [name]: value })
  }

  const onFormSave = () => {
    createFinancialProposal(formData).then(res => toast.success(res.msg))
  }

  const handleFetchFields = () => {
    fetchFields().then(res => setFormFields(res))
  }

  const handleFetchPersons = () => {
    fetchPersons().then(res => setPersons(res))
  }

  useEffect(() => {
    handleFetchFields();
    handleFetchPersons();
  }, [])


  return (
    <div style={divStyles}>
      <div style={divFormStyles}>
        <h3 style={{ color: 'black' }}> Crie sua proposta </h3>
        <SelectInput
          name={'person'}
          options={persons}
          onChange={handleFormChange}
        />
        {formFields.map(field => (
          <Input
            key={field.id}
            name={field.name}
            type={field.type}
            onChange={handleFormChange}
            enabled={field.enabled}
          />
        ))}
        <Button onConfirm={onFormSave}> Criar proposta </Button>
      </div>
    </div>
  );
}

export default Container;
