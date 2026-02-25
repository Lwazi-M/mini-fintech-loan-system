import React, { useState } from 'react';
import './App.css';

function App() {
  // 1. These are our "Sticky Notes" (State)
  // We start them as empty strings ""
  const [formData, setFormData] = useState({
    name: "",
    score: "",
    income: "",
    expenses: ""
  });
  const [result, setResult] = useState(null);

  // 2. This function updates the "Sticky Note" as you type
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // 3. This is the "Submit" action
  const handleSubmit = async (e) => {
    e.preventDefault(); // Stop the page from refreshing
    
    // We send the data to our Python Waiter (API)
    const response = await fetch(`http://127.0.0.1:8000/apply?name=${formData.name}&score=${formData.score}&income=${formData.income}&expenses=${formData.expenses}`, {
      method: 'POST'
    });
    
    const data = await response.json();
    setResult(data); // Save the answer from the bank
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🏦 FinTech Loan Scorer</h1>
        
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <input name="name" placeholder="Full Name" onChange={handleChange} required />
          <input name="score" type="number" placeholder="Credit Score (0-850)" onChange={handleChange} required />
          <input name="income" type="number" placeholder="Monthly Income (R)" onChange={handleChange} required />
          <input name="expenses" type="number" placeholder="Monthly Expenses (R)" onChange={handleChange} required />
          
          <button type="submit" style={{ padding: '10px', backgroundColor: '#0070f3', color: 'white', border: 'none', cursor: 'pointer' }}>
            Check Eligibility
          </button>
        </form>

        {/* 4. Show the result only if we have one */}
        {result && (
          <div style={{ marginTop: '20px', padding: '20px', border: '1px solid white' }}>
            <h3>Result for {result.customer}</h3>
            <p>Score: {result.final_score}</p>
            <h2 style={{ color: result.status === "APPROVED" ? "green" : "red" }}>
              {result.status}
            </h2>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;