
import React, { useEffect, useState } from 'react';

const API_URL = 'https://jubilant-goldfish-r49v4pxrg95g3559-8000.app.github.dev/api/activities/';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched activities:', results);
      });
  }, []);

  return (
    <div className="container mt-4">
      <div className="card shadow-sm">
        <div className="card-body">
          <h2 className="card-title mb-4 text-primary">Activities</h2>
          <div className="table-responsive">
            <table className="table table-striped table-bordered align-middle">
              <thead className="table-primary">
                <tr>
                  <th>User</th>
                  <th>Type</th>
                  <th>Duration (min)</th>
                  <th>Distance (km)</th>
                  <th>Calories</th>
                  <th>Date</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {activities.map((a, i) => (
                  <tr key={i}>
                    <td>{a.user}</td>
                    <td>{a.activity_type}</td>
                    <td>{a.duration}</td>
                    <td>{a.distance}</td>
                    <td>{a.calories_burned}</td>
                    <td>{a.date}</td>
                    <td>
                      <button className="btn btn-sm btn-outline-info me-2" disabled>View</button>
                      <button className="btn btn-sm btn-outline-secondary" disabled>Edit</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <button className="btn btn-primary mt-3" disabled>Add Activity</button>
        </div>
      </div>
    </div>
  );
}

export default Activities;
