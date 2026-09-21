import { useEffect, useState } from "react";

function History() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const token = localStorage.getItem("access_token");

      if (!token) {
        setError("Please login first.");
        setLoading(false);
        return;
      }

      const response = await fetch(
        "http://127.0.0.1:5000/api/history",
        {
          method: "GET",

          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setError(
          data.error || "Unable to load history."
        );
        setLoading(false);
        return;
      }

      setHistory(data.history);

    } catch (error) {
      setError(
        "Unable to connect to the backend."
      );
    } finally {
      setLoading(false);
    }
  };


  const deleteRecord = async (recordId) => {

    const confirmDelete = window.confirm(
      "Are you sure you want to delete this prediction?"
    );

    if (!confirmDelete) {
      return;
    }

    try {

      const token =
        localStorage.getItem("access_token");

      const response = await fetch(
        `http://127.0.0.1:5000/api/history/${recordId}`,
        {
          method: "DELETE",

          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setError(
          data.error || "Unable to delete record."
        );
        return;
      }

      // Remove deleted record from the screen
      setHistory(
        history.filter(
          (record) => record.id !== recordId
        )
      );

    } catch (error) {

      setError(
        "Unable to connect to the backend."
      );

    }
  };


  if (loading) {
    return (
      <div className="history-page">
        <p>Loading history...</p>
      </div>
    );
  }


  return (
    <div className="history-page">

      <div className="history-header">

        <h1>Energy History</h1>

        <p>
          View your previous household energy predictions.
        </p>

      </div>


      {error && (
        <div className="error-message history-error">
          {error}
        </div>
      )}


      {history.length === 0 ? (

        <div className="history-empty">

          <h2>No Prediction History</h2>

          <p>
            You haven't made any energy predictions yet.
          </p>

        </div>

      ) : (

        <div className="history-table-container">

          <table className="history-table">

            <thead>

              <tr>

                <th>Date</th>

                <th>Temperature</th>

                <th>Occupants</th>

                <th>AC Hours</th>

                <th>Previous Consumption</th>

                <th>Predicted Consumption</th>

                <th>Status</th>

                <th>Action</th>

              </tr>

            </thead>


            <tbody>

              {history.map((record) => {

                let status;

                if (
                  record.predicted_consumption < 12
                ) {
                  status = "Low";
                } else if (
                  record.predicted_consumption < 20
                ) {
                  status = "Moderate";
                } else {
                  status = "High";
                }

                return (

                  <tr key={record.id}>

                    <td>
                      {record.date}
                    </td>

                    <td>
                      {record.temperature} °C
                    </td>

                    <td>
                      {record.occupants}
                    </td>

                    <td>
                      {record.ac_hours}
                    </td>

                    <td>
                      {record.previous_consumption} kWh
                    </td>

                    <td>
                      <strong>
                        {record.predicted_consumption} kWh
                      </strong>
                    </td>

                    <td>
                      <span className="status-badge">
                        {status}
                      </span>
                    </td>

                    <td>

                      <button
                        className="delete-button"
                        onClick={() =>
                          deleteRecord(record.id)
                        }
                      >
                        Delete
                      </button>

                    </td>

                  </tr>

                );
              })}

            </tbody>

          </table>

        </div>

      )}

    </div>
  );
}

export default History;