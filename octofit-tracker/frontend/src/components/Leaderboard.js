
import React, { useEffect, useState } from 'react';

const API_URL = 'https://jubilant-goldfish-r49v4pxrg95g3559-8000.app.github.dev/api/leaderboard/';

function Leaderboard() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setEntries(results);
        console.log('Fetched leaderboard:', results);
      });
  }, []);

  return (
    <div className="container mt-4">
      <div className="card shadow-sm">
        <div className="card-body">
          <h2 className="card-title mb-4 text-success">Leaderboard</h2>
          <div className="table-responsive">
            <table className="table table-striped table-bordered align-middle">
              <thead className="table-success">
                <tr>
                  <th>Rank</th>
                  <th>User</th>
                  <th>Team</th>
                  <th>Total Activities</th>
                  <th>Total Duration</th>
                  <th>Total Distance</th>
                  <th>Total Calories</th>
                </tr>
              </thead>
              <tbody>
                {entries.map((e, i) => (
                  <tr key={i}>
                    <td>{e.rank}</td>
                    <td>{e.user}</td>
                    <td>{e.team}</td>
                    <td>{e.total_activities}</td>
                    <td>{e.total_duration}</td>
                    <td>{e.total_distance}</td>
                    <td>{e.total_calories}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
