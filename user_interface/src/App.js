import React, { useState } from 'react';

function App() {
  const [modelData, setModelData] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch('http://localhost:5000/upload-model', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ model_data: modelData }),
      });

      const data = await res.json();
      setResponse(data.status || data.error);
    } catch (error) {
      setResponse('Error: Could not connect to the API');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Upload Model</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Model Data:
          <input
            type="text"
            value={modelData}
            onChange={(e) => setModelData(e.target.value)}
            required
          />
        </label>
        <button type="submit">Upload</button>
      </form>
      {response && <p>Response: {response}</p>}
    </div>
  );
}

export default App;
