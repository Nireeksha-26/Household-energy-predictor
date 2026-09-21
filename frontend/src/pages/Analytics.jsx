import { useEffect, useState } from "react";

import {
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer
} from "recharts";


function Analytics() {

  const [history, setHistory] = useState([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");


  useEffect(() => {

    fetchHistory();

  }, []);


  const fetchHistory = async () => {

    try {

      const token =
        localStorage.getItem("access_token");

      if (!token) {

        setError(
          "Please login first."
        );

        setLoading(false);

        return;
      }


      const response = await fetch(
        "http://127.0.0.1:5000/api/history",
        {
          method: "GET",

          headers: {
            Authorization:
              `Bearer ${token}`
          }
        }
      );


      const data =
        await response.json();


      if (!response.ok) {

        setError(
          data.error ||
          "Unable to load analytics."
        );

        setLoading(false);

        return;
      }


      setHistory(
        data.history
      );

    } catch (error) {

      setError(
        "Unable to connect to the backend."
      );

    } finally {

      setLoading(false);

    }
  };


  /*
   * Prepare consumption chart data
   */

  const consumptionData =
    [...history]
      .reverse()
      .map((record, index) => ({
        prediction:
          `Prediction ${index + 1}`,

        consumption:
          record.predicted_consumption
      }));


  /*
   * Prepare appliance usage data
   */

  const applianceTotals = {

    AC: 0,

    Refrigerator: 0,

    WashingMachine: 0,

    TV: 0,

    Lighting: 0,

    Computer: 0,

    Other: 0

  };


  history.forEach((record) => {

    applianceTotals.AC +=
      record.ac_hours;

    applianceTotals.Refrigerator +=
      record.refrigerator_hours;

    applianceTotals.WashingMachine +=
      record.washing_machine_hours;

    applianceTotals.TV +=
      record.tv_hours;

    applianceTotals.Lighting +=
      record.lighting_hours;

    applianceTotals.Computer +=
      record.computer_hours;

    applianceTotals.Other +=
      record.other_appliance_hours;

  });


  const applianceData = [

    {
      appliance: "AC",
      hours:
        Number(
          applianceTotals.AC.toFixed(2)
        )
    },

    {
      appliance: "Refrigerator",
      hours:
        Number(
          applianceTotals.Refrigerator.toFixed(2)
        )
    },

    {
      appliance: "Washing Machine",
      hours:
        Number(
          applianceTotals.WashingMachine.toFixed(2)
        )
    },

    {
      appliance: "TV",
      hours:
        Number(
          applianceTotals.TV.toFixed(2)
        )
    },

    {
      appliance: "Lighting",
      hours:
        Number(
          applianceTotals.Lighting.toFixed(2)
        )
    },

    {
      appliance: "Computer",
      hours:
        Number(
          applianceTotals.Computer.toFixed(2)
        )
    },

    {
      appliance: "Other",
      hours:
        Number(
          applianceTotals.Other.toFixed(2)
        )
    }

  ];


  if (loading) {

    return (
      <div className="analytics-page">

        <p>
          Loading analytics...
        </p>

      </div>
    );
  }


  if (error) {

    return (
      <div className="analytics-page">

        <div className="error-message">
          {error}
        </div>

      </div>
    );
  }


  if (history.length === 0) {

    return (
      <div className="analytics-page">

        <div className="analytics-header">

          <h1>
            Energy Analytics
          </h1>

          <p>
            Analyze your household energy usage.
          </p>

        </div>


        <div className="analytics-empty">

          <h2>
            Not Enough Data
          </h2>

          <p>
            Make some energy predictions to see
            analytics and charts here.
          </p>

        </div>

      </div>
    );
  }


  return (

    <div className="analytics-page">

      <div className="analytics-header">

        <h1>
          Energy Analytics
        </h1>

        <p>
          Analyze your household energy consumption
          using your prediction history.
        </p>

      </div>


      {/* Consumption Chart */}

      <div className="chart-card">

        <h2>
          Energy Consumption Trend
        </h2>

        <p className="chart-description">
          Predicted energy consumption across
          your recorded predictions.
        </p>


        <div className="chart-container">

          <ResponsiveContainer
            width="100%"
            height={350}
          >

            <LineChart
              data={consumptionData}
            >

              <CartesianGrid
                strokeDasharray="3 3"
              />

              <XAxis
                dataKey="prediction"
              />

              <YAxis />

              <Tooltip />

              <Legend />

              <Line
                type="monotone"
                dataKey="consumption"
                name="Consumption (kWh)"
                strokeWidth={2}
              />

            </LineChart>

          </ResponsiveContainer>

        </div>

      </div>


      {/* Appliance Chart */}

      <div className="chart-card">

        <h2>
          Appliance Usage
        </h2>

        <p className="chart-description">
          Total recorded usage hours by appliance.
        </p>


        <div className="chart-container">

          <ResponsiveContainer
            width="100%"
            height={350}
          >

            <BarChart
              data={applianceData}
            >

              <CartesianGrid
                strokeDasharray="3 3"
              />

              <XAxis
                dataKey="appliance"
              />

              <YAxis />

              <Tooltip />

              <Legend />

              <Bar
                dataKey="hours"
                name="Usage Hours"
              />

            </BarChart>

          </ResponsiveContainer>

        </div>

      </div>


      {/* Data Summary */}

      <div className="analytics-summary">

        <div className="summary-card">

          <h3>
            Total Predictions
          </h3>

          <p>
            {history.length}
          </p>

        </div>


        <div className="summary-card">

          <h3>
            Average Predicted Usage
          </h3>

          <p>

            {
              (
                history.reduce(
                  (total, record) =>
                    total +
                    record.predicted_consumption,
                  0
                ) / history.length
              ).toFixed(2)
            }

            {" "}kWh

          </p>

        </div>


        <div className="summary-card">

          <h3>
            Highest Prediction
          </h3>

          <p>

            {
              Math.max(
                ...history.map(
                  (record) =>
                    record.predicted_consumption
                )
              ).toFixed(2)
            }

            {" "}kWh

          </p>

        </div>

      </div>

    </div>
  );
}


export default Analytics;