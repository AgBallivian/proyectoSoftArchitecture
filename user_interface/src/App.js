import React, { useState, useEffect } from 'react';

function App() {
  const [model, setModel] = useState('');
  const [hardware, setHardware] = useState('');
  const [optimization, setOptimization] = useState('');
  const [options, setOptions] = useState({ models: [], hardware: [], optimizations: [] });
  const [response, setResponse] = useState('');

  useEffect(() => {
    const fetchOptions = async () => {
      try {
        const res = await fetch('http://localhost:5000/get-options');
        const data = await res.json();
        setOptions(data); // Set options for models, hardware, and optimizations
      } catch (error) {
        console.error("Failed to fetch options:", error);
      }
    };
    fetchOptions();
  }, []);

  const handleModelSelect = async (e) => {
    const selectedModel = e.target.value;
    setModel(selectedModel);
    await fetch('http://localhost:5000/choose-model', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model_data: selectedModel }),
    });
  };

  const handleHardwareSelect = async (e) => {
    const selectedHardware = e.target.value;
    setHardware(selectedHardware);
    await fetch('http://localhost:5000/choose-hardware-simulation', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model_data: selectedHardware }),
    });
  };

  const handleOptimizationSelect = async (e) => {
    const selectedOptimization = e.target.value;
    setOptimization(selectedOptimization);
    await fetch('http://localhost:5000/choose-optimization', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model_data: selectedOptimization }),
    });
  };

  const handleRunSimulation = async () => {
    const res = await fetch('http://localhost:5000/run-simulation', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model_id: model,
        hardware_type: hardware,
        optimization: optimization,
      }),
    });
    const data = await res.json();
    setResponse(data.status || data.error);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Configure and Run Simulation</h1>
      
      <div>
        <label>Select Model: </label>
        <select value={model} onChange={handleModelSelect}>
          <option value="">Choose a model</option>
          {options.models.map((modelOption) => (
            <option key={modelOption} value={modelOption}>
              {modelOption}
            </option>
          ))}
        </select>
      </div>

      <div>
        <label>Select Hardware: </label>
        <select value={hardware} onChange={handleHardwareSelect}>
          <option value="">Choose hardware</option>
          {options.hardware.map((hardwareOption) => (
            <option key={hardwareOption} value={hardwareOption}>
              {hardwareOption}
            </option>
          ))}
        </select>
      </div>

      <div>
        <label>Select Optimization: </label>
        <select value={optimization} onChange={handleOptimizationSelect}>
          <option value="">Choose optimization</option>
          {options.optimizations.map((optimizationOption) => (
            <option key={optimizationOption} value={optimizationOption}>
              {optimizationOption}
            </option>
          ))}
        </select>
      </div>

      <button onClick={handleRunSimulation}>Run Simulation</button>

      {response && <p>Response: {response}</p>}
    </div>
  );
}

export default App;
