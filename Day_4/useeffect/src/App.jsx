import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Navbar from './components/Navbar'

function App() {
  // State: count is shown on the button.
  const [count, setCount] = useState(0)
  // State: currently unused, but declared here.
  const [first, setFirst] = useState(0)
  // State: increases each time count changes (used for a color value idea).
  const [color, setColor] = useState(0)

  // Flow: when `count` changes, this effect runs.
  // Why: the dependency array [count] tells React to run it only after count updates.
  useEffect(() => {
    alert("Count was changed")
    // Flow: update color so it keeps in sync with count changes.
    setColor(color + 1)
  }, [count])


  return (
    <>
      {/* Navbar is commented out; it would receive a color based on state. */}
      {/* <Navbar color={"navy " + "blue" + color} /> */}
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        {/* Flow: clicking button updates count, which triggers the effect. */}
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
