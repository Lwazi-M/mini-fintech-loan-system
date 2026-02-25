import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    name: "",
    score: "",
    income: "",
    expenses: ""
  });
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    setError(null); // Clear errors when user types
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    
    try {
      // Sending data to our FastAPI "Waiter"
      const response = await fetch(`http://127.0.0.1:8000/apply?name=${formData.name}&score=${formData.score}&income=${formData.income}&expenses=${formData.expenses}`, {
        method: 'POST'
      });
      
      const data = await response.json();

      if (!response.ok) {
        // This catches our "Safety Checks" from the backend
        throw new Error(data.detail || "Something went wrong");
      }

      setResult(data);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🏦 Investec Loan Scorer</h1>
        
        <form onSubmit={handleSubmit}>
          <input name="name" placeholder="Full Name" onChange={handleChange} required />
          <input name="score" type="number" placeholder="Credit Score (0-850)" onChange={handleChange} required />
          <input name="income" type="number" placeholder="Monthly Income (R)" onChange={handleChange} required />
          <input name="expenses" type="number" placeholder="Monthly Expenses (R)" onChange={handleChange} required />
          
          <button type="submit">Check Eligibility</button>
        </form>

        {/* Error Message Display */}
        {error && <p style={{ color: '#ff3860', marginTop: '10px' }}>⚠️ {error}</p>}

        {/* 📊 THE RISK GAUGE */}
        {result && (
          <div className="result-card" style={{ borderLeftColor: result.status === "APPROVED" ? "#00d1b2" : "#ff3860" }}>
            <h3>Result for {result.customer}</h3>
            
            <div className="gauge-container" style={{ background: '#444', height: '12px', width: '100%', borderRadius: '6px', margin: '15px 0' }}>
              <div className="gauge-fill" style={{ 
                background: result.status === "APPROVED" ? "#00d1b2" : "#ff3860", 
                height: '100%', 
                width: `${result.final_score}%`, 
                borderRadius: '6px',
                transition: 'width 1.5s ease-in-out' 
              }}></div>
            </div>
            
            <p>Financial Health Score: <strong>{result.final_score}/100</strong></p>
            <h2 style={{ color: result.status === "APPROVED" ? "#00d1b2" : "#ff3860" }}>
              {result.status}
            </h2>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;