import React, { useEffect, useState } from 'react'
import logo from './logo.svg';
import './App.css';

function App() {

  const [tasks, setTasks] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  const fetchTask = async () => {
    setIsLoading(true)

    const response = await fetch('http://127.0.0.1:8000/task-list/')
    const data = await response.json()

    setTasks(data)

    setIsLoading(false)
  }

  useEffect(() => {
    fetchTask()
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        {isLoading 
          ? <h1>Loading data...</h1>
          : tasks.map((task) => (
            <p key={task.id}>{task.title}</p>
          ))
        }
      </header>
    </div>
  );
}

export default App;
