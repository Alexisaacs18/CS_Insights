import './App.css';
import { useState, useEffect } from 'react';

function App() {

  const url = "http://127.0.0.1:5000"

  const [insights, setInsights] = useState([])

  useEffect(() => {
    fetch(`${url}/insights`, {
      method: "GET",
      headers: {"Content-Type": "application/json"}
    })
    .then(res => res.json())
    .then(data => setInsights(data))
  }, [])

  console.log(insights)

  const columns = [
    {key: "lights", title: "lights"},
    {key: "category", title: "category"},
    {key: "notes", title: "notes"},
    {key: "cur_response", title: "cur_response"},
    {key: "prev_response", title: "prev_response"},
    {key: "organization_id", title: "organization_id"},
    {key: "credit_limit", title: "credit_limit"},
    {key: "approval_date", title: "approval_date"},
    {key: "current_balance", title: "current_balance"},
    {key: "name", title: "name"},
    {key: "current_month", title: "current_month"},
    {key: "last_month", title: "last_month"},
    {key: "two_months_ago", title: "two_months_ago"},
    {key: "three_months_ago", title: "three_months_ago"},
    {key: "one_year_ago", title: "one_year_ago"},
  ]

  return (
    <div className="App">
      <h1>CS Insights</h1>
      <table>
      <thead>
        <tr>
          {columns.map((column) => (
            <th key={column.key}>{column.title}</th>
          ))}
        </tr>
      </thead>
      <tbody>
      {insights.map((row) => (
          <tr key={row.id}>
            {columns.map((column) => (
              <td key={column.key}>{row[column.key]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
    </div>
  );
}

export default App;
