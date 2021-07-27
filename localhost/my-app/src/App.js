import React, {useState,useEffect} from 'react';
import './App.css';

function App() {
  const[initialData, setinitialData]=useState([{}]);

  useEffect(() => {
    fetch('/api').then(
      response => response.json()
      ).then(data => setinitialData(data))
    console.log(initialData.CurrentTime)
  });
  return (
    <div className="App">
      <h1>{initialData.Sensor1}</h1>
      <h1>{initialData.Sensor2}</h1>
      <h1>{initialData.CurrentTime}</h1>
    </div>
  );
}

export default App;
