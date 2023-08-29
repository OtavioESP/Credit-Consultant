import React from "react";

const Proposal = ({ data }) => {

  const divStyles = {
    width: '80%',
    height: '50px',
    backgroundColor: 'white',
    margin: '20px auto',
    borderTopRightRadius: '15px',
    borderTopLeftRadius: '15px',
    borderBottom: '2px solid #c9c9c9',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingLeft: '10px',
    paddingRight: '10px',
  };

  const nameStyles = {
    fontWeight: 'bold',
    fontSize: '20px'
  };

  const missingNameStyles = {
    fontWeight: 'bold',
    fontSize: '15px'
  }

  const statusStyles = {
    fontWeight: 'bold',
    fontSize: '20px',
    color: data.status.id === 3 ? 'green' : (data.status.id === 2 ? '#a39c31' : 'red'),
  };


  return (
    <div style={divStyles}>
      {data.person ?
        <a style={nameStyles}>{data.person.full_name}</a>
        :
        <a style={missingNameStyles}>pessoa não exibida na proposta</a>
      }
      <b style={statusStyles}>{data.status.name}</b>
    </div>
  );
}

export default Proposal;
