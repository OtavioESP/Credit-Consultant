

import React from "react";
import Container from "../components/Container";

const CreateProposalPage = () => {
  const divStyles = {
    backgroundColor: '#282c34',
    height: '100vh',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: 'calc(10px + 2vmin)',
  };

  const textStyles = {
    color: 'white',
  }

  const containerStyles = {
    display: 'flex',
    flexDirection: 'row',
    gap: '50px'
  }


  return (
    <div style={divStyles}>
      <h1 style={textStyles}> Loans For Good </h1>
      <h6 style={textStyles}> Crédito rápido e fácil! </h6>
      <div style={containerStyles}>
        <Container />
      </div>
    </div>
  )
}
export default CreateProposalPage;
