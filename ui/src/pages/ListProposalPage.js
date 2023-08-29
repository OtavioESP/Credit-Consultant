import React, { useEffect, useState } from "react";
import ListProposals from "../components/ListProposals";
import { fetchFinancialProposal } from "../services/services";

const ListProposalPage = () => {
  const [proposals, setProposals] = useState([]);

  const divStyles = {
    backgroundColor: '#282c34',
    height: 'fit-content',
    flexDirection: 'column',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: 'calc(10px + 2vmin)',
  };

  const containerStyles = {
    display: 'flex',
    flexDirection: 'row',
    gap: '50px'
  }

  const textStyles = {
    color: 'white',
  }


  const handleFetchFinancialProposal = () => {
    fetchFinancialProposal().then(res => setProposals(res))

  }

  useEffect(() => {
    handleFetchFinancialProposal();
  }, [])


  return (
    <div style={divStyles}>
      <h1 style={textStyles}> Loans For Good </h1>
      <h6 style={textStyles}> Crédito rápido e fácil! </h6>
      <div style={containerStyles}>
        <ListProposals
          proposals={proposals}
        />
      </div>
    </div>
  )
}
export default ListProposalPage;
