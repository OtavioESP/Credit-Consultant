import React from "react";
import { API_HOST } from "../consts";

const Header = () => {
  const headerStyles = {
    width: '100%',
    height: '100px',
    backgroundColor: '#1d232e',
    display: 'flex',
    justifyContent: 'space-evenly',
    alignItems: 'center',
  };

  const linkStyles = {
    color: 'white',
    textDecoration: 'none',
    fontWeight: 'bold',
    fontSize: '30px',
  };

  return (
    <div style={headerStyles}>
      <a href="/listar" style={linkStyles}>
        Propostas
      </a>
      <a href="/" style={linkStyles}>
        Nova proposta
      </a>
      <a href={`${API_HOST}/admin`} style={linkStyles}>
        Admin
      </a>
    </div>
  );
};

export default Header;
