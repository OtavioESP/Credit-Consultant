import './App.css';
import Container from './components/Container';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1> Ola </h1>
        <div style={{ display: 'flex', flexDirection: 'row', gap: '50px' }}>
          <Container />
        </div>
      </header>
    </div>
  );
}

export default App;
