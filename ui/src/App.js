import './App.css';
import CreateProposalPage from './pages/CreateProposalPage';
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import ListProposalPage from './pages/ListProposalPage';
import Header from './components/Header';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route index element={<CreateProposalPage />} />
        <Route path="listar" element={<ListProposalPage />} />
      </Routes>
      <ToastContainer />
    </BrowserRouter>
  );
}

export default App;
