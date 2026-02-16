
import React, { useEffect, useState } from 'react';

const API_URL = 'https://jubilant-goldfish-r49v4pxrg95g3559-8000.app.github.dev/api/workouts/';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Fetched workouts:', results);
      });
  }, []);

  return (
    <div className="container mt-4">
      <div className="card shadow-sm">
        <div className="card-body">
          <h2 className="card-title mb-4 text-danger">Workouts</h2>
          <div className="table-responsive">
            <table className="table table-striped table-bordered align-middle">
              <thead className="table-danger">
                <tr>
                  <th>Name</th>
                  <th>User</th>
                  <th>Description</th>
                  <th>Exercises</th>
                  <th>Difficulty</th>
                  <th>Duration</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {workouts.map((w, i) => (
                  <tr key={i}>
                    <td>{w.name}</td>
                    <td>{w.user}</td>
                    <td>{w.description}</td>
                    <td>{w.exercises && w.exercises.join(', ')}</td>
                    <td>{w.difficulty}</td>
                    <td>{w.duration}</td>
                    <td>
                      <button className="btn btn-sm btn-outline-info me-2" disabled>View</button>
                      <button className="btn btn-sm btn-outline-secondary" disabled>Edit</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <button className="btn btn-primary mt-3" disabled>Add Workout</button>
        </div>
      </div>
    </div>
  );
}

export default Workouts;
