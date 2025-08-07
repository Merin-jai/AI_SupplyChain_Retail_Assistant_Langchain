// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

import React, { useState } from "react";
import { runSupplyChainAssistant } from "./api/supplyChainApi";

function App() {
  const [output, setOutput] = useState(null);

  const handleRun = async () => {
    const inputData = { sku_id: "A123", store_id: "Store01" };
    const result = await runSupplyChainAssistant(inputData);
    setOutput(result);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>AI Supply Chain Assistant</h1>
      <button onClick={handleRun}>Run Demand Forecast</button>
      {output && <pre>{JSON.stringify(output, null, 2)}</pre>}
    </div>
  );
}

export default App;

