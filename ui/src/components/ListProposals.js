import React from "react";
import Proposal from "./Proposal";

const ListProposals = ({ proposals }) => {
  const divStyles = {
    width: '600px',
    height: 'fit-content',
    backgroundColor: 'white',
    borderRadius: '30px',
    boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.5)',
    margin: '20px auto',
    alignItems: 'center',
    display: 'flex',
    flexDirection: 'column',
    textAlign: 'center',
  };

  const TitleStyles = {
    color: 'black',
  };

  return (
    <div style={divStyles}>
      <h3 style={TitleStyles}> Listagem de propostas </h3>
      {proposals ?
        proposals.map((pro) => <Proposal data={pro} />)
        :
        <a style={{ color: 'black', fontSize: '20px' }}>
          Ainda não existem propostas a serem listadas.
        </a>
      }
    </div>
  );
}

export default ListProposals;
