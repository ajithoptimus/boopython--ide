import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');

  const handleChange = (e) => {
    setCode(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/run', {
        code: code,
      });
      setOutput(response.data.output);
    } catch (error) {
      console.error('There was an error!', error);
    }
  };

  return (
    <div>
      <h1>Code Runner</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={code}
          onChange={handleChange}
          placeholder="Write your code here"
        />
        <button type="submit">Run Code</button>
      </form>
      <div>
        <h2>Output:</h2>
        <pre>{output}</pre>
      </div>
    </div>
  );
}

export default App;
