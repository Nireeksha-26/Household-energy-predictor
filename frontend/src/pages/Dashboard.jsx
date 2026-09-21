import { useEffect, useState } from "react";

function Dashboard() {
  const [dashboard, setDashboard] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      const token = localStorage.getItem("access_token");

      if (!token) {
        setError("Please login first.");
        return;
      }

      const response = await fetch(
        "http://127.0.0.1:5000/api/dashboard",
        {
          method: "GET",

          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setError(data.error || "Unable to load dashboard.");
        return;
      }

      setDashboard(data);

    } catch (error) {
      setError(
        "Unable to connect to the backend."
      );
    }
  };

  if (error) {
    return (
      <div className="dashboard-page">
        <div className="error-message">
          {error}
        </div>
      </div>
    );
  }

  if (!dashboard) {
    return (
      <div className="dashboard-page">
        <p>Loading dashboard...</p>
      </div>
    );
  }

  return (
    <div className="dashboard-page">

      {/* Header */}

      <header className="dashboard-header">

        <div>
          <h1>Energy Dashboard</h1>

          <p>
            Monitor and understand your household
            energy consumption.
          </p>
        </div>

        <div className="user-info">
          <span>Welcome back!</span>
        </div>

      </header>


      {/* Summary Cards */}

      <div className="dashboard-cards">

        <div className="dashboard-card">
          <h3>Total Predictions</h3>

          <p className="card-value">
            {dashboard.total_predictions}
          </p>

          <span>Predictions made</span>
        </div>


        <div className="dashboard-card">
          <h3>Average Consumption</h3>

          <p className="card-value">
            {dashboard.average_consumption} kWh
          </p>

          <span>Average predicted usage</span>
        </div>


        <div className="dashboard-card">
          <h3>Highest Consumption</h3>

          <p className="card-value">
            {dashboard.highest_consumption} kWh
          </p>

          <span>Highest predicted usage</span>
        </div>


        <div className="dashboard-card">
          <h3>Lowest Consumption</h3>

          <p className="card-value">
            {dashboard.lowest_consumption} kWh
          </p>

          <span>Lowest predicted usage</span>
        </div>

      </div>


      {/* Energy Status */}

      <div className="status-section">

        <h2>Current Energy Status</h2>

        <div className="status-card">

          <div>
            <p>Status</p>

            <h2>
              {dashboard.energy_status}
            </h2>
          </div>

          <div>
            <p>Latest Prediction</p>

            {dashboard.latest_prediction ? (
              <h2>
                {
                  dashboard.latest_prediction
                    .predicted_consumption
                }{" "}
                kWh
              </h2>
            ) : (
              <h2>No data</h2>
            )}
          </div>

        </div>

      </div>


      {/* Recent Predictions */}

      <div className="recent-section">

        <h2>Recent Predictions</h2>

        {dashboard.recent_records.length === 0 ? (

          <p className="empty-message">
            No prediction records available.
          </p>

        ) : (

          <div className="table-container">

            <table>

              <thead>
                <tr>
                  <th>Date</th>
                  <th>Predicted Consumption</th>
                  <th>Actual Consumption</th>
                </tr>
              </thead>

              <tbody>

                {dashboard.recent_records.map(
                  (record) => (

                    <tr key={record.id}>

                      <td>
                        {record.date}
                      </td>

                      <td>
                        {record.predicted_consumption} kWh
                      </td>

                      <td>
                        {record.actual_consumption
                          ?? "Not available"}
                      </td>

                    </tr>

                  )
                )}

              </tbody>

            </table>

          </div>

        )}

      </div>

    </div>
  );
}

export default Dashboard;