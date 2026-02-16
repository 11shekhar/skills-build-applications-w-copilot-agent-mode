
import React, { useEffect, useState } from 'react';

const API_URL = 'https://jubilant-goldfish-r49v4pxrg95g3559-8000.app.github.dev/api/teams/';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched teams:', results);
      });
  }, []);

  return (
    <div className="container mt-4">
      <div className="card shadow-sm">
        <div className="card-body">
          <h2 className="card-title mb-4 text-info">Teams</h2>
          <div className="table-responsive">
            <table className="table table-striped table-bordered align-middle">
              <thead className="table-info">
                <tr>
                  <th>Name</th>
                  <th>Description</th>
                  <th>Members</th>
                  <th>Created</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {teams.map((t, i) => (
                  <tr key={i}>
                    <td>{t.name}</td>
                    <td>{t.description}</td>
                    <td>{t.members && t.members.length}</td>
                    <td>{t.created_at}</td>
                    <td>
                      <button className="btn btn-sm btn-outline-info me-2" disabled>View</button>
                      <button className="btn btn-sm btn-outline-secondary" disabled>Edit</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <button className="btn btn-primary mt-3" disabled>Add Team</button>
        </div>
      </div>
    </div>
  );
}

export default Teams;
