import { useState } from "react";

function Prediction() {
  const [formData, setFormData] = useState({
    temperature: "",
    humidity: "",
    occupants: "",
    ac_hours: "",
    refrigerator_hours: "",
    washing_machine_hours: "",
    tv_hours: "",
    lighting_hours: "",
    computer_hours: "",
    other_appliance_hours: "",
    previous_consumption: "",
    hour: "",
    day_of_week: "",
    month: ""
  });

  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");
    setResult(null);
    setLoading(true);

    try {
      const token = localStorage.getItem("access_token");

      if (!token) {
        setError("Please login first.");
        setLoading(false);
        return;
      }

      // Convert form values from strings to numbers
      const requestData = {
        temperature: Number(formData.temperature),
        humidity: Number(formData.humidity),
        occupants: Number(formData.occupants),
        ac_hours: Number(formData.ac_hours),
        refrigerator_hours: Number(
          formData.refrigerator_hours
        ),
        washing_machine_hours: Number(
          formData.washing_machine_hours
        ),
        tv_hours: Number(formData.tv_hours),
        lighting_hours: Number(formData.lighting_hours),
        computer_hours: Number(formData.computer_hours),
        other_appliance_hours: Number(
          formData.other_appliance_hours
        ),
        previous_consumption: Number(
          formData.previous_consumption
        ),
        hour: Number(formData.hour),
        day_of_week: Number(formData.day_of_week),
        month: Number(formData.month)
      };

      const response = await fetch(
        "http://127.0.0.1:5000/api/predict",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
          },

          body: JSON.stringify(requestData)
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setError(
          data.error || "Prediction failed."
        );
        setLoading(false);
        return;
      }

      setResult(data);

    } catch (error) {

      setError(
        "Unable to connect to the backend. Make sure Flask is running."
      );

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="prediction-page">

      <div className="prediction-header">

        <h1>Energy Consumption Prediction</h1>

        <p>
          Enter your household information to predict
          energy consumption.
        </p>

      </div>


      {error && (
        <div className="error-message prediction-error">
          {error}
        </div>
      )}


      <form
        className="prediction-form"
        onSubmit={handleSubmit}
      >

        {/* Environmental Information */}

        <div className="form-section">

          <h2>Environmental Information</h2>

          <div className="form-grid">

            <div className="form-group">
              <label>
                Temperature (°C)
              </label>

              <input
                type="number"
                name="temperature"
                value={formData.temperature}
                onChange={handleChange}
                placeholder="Example: 30"
                step="0.1"
                required
              />
            </div>


            <div className="form-group">
              <label>
                Humidity (%)
              </label>

              <input
                type="number"
                name="humidity"
                value={formData.humidity}
                onChange={handleChange}
                placeholder="Example: 65"
                step="0.1"
                required
              />
            </div>

          </div>

        </div>


        {/* Household Information */}

        <div className="form-section">

          <h2>Household Information</h2>

          <div className="form-grid">

            <div className="form-group">
              <label>
                Number of Occupants
              </label>

              <input
                type="number"
                name="occupants"
                value={formData.occupants}
                onChange={handleChange}
                placeholder="Example: 4"
                min="0"
                required
              />
            </div>

          </div>

        </div>


        {/* Appliance Usage */}

        <div className="form-section">

          <h2>Appliance Usage</h2>

          <p className="section-description">
            Enter approximate usage hours per day.
          </p>

          <div className="form-grid">

            <div className="form-group">
              <label>AC Hours</label>

              <input
                type="number"
                name="ac_hours"
                value={formData.ac_hours}
                onChange={handleChange}
                placeholder="0 - 24"
                min="0"
                max="24"
                step="0.1"
                required
              />
            </div>


            <div className="form-group">
              <label>Refrigerator Hours</label>

              <input
                type="number"
                name="refrigerator_hours"
                value={formData.refrigerator_hours}
                onChange={handleChange}
                placeholder="0 - 24"
                min="0"
                max="24"
                step="0.1"
                required
              />
            </div>


            <div className="form-group">
              <label>Washing Machine Hours</label>

              <input
                type="number"
                name="washing_machine_hours"
                value={formData.washing_machine_hours}
                onChange={handleChange}
                placeholder="0 - 24"
                min="0"
                max="24"
                step="0.1"
                required
              />
            </div>


            <div className="form-group">
              <label>TV Hours</label>

              <input
                type="number"
                name="tv_hours"
                value={formData.tv_hours}
                onChange={handleChange}
                placeholder="0 - 24"
                min="0"
                max="24"
                step="0.1"
                required
              />
            </div>


            <div className="form-group">
              <label>Lighting Hours</label>

              <input
                type="number"
                name="lighting_hours"
                value={formData.lighting_hours}
                onChange={handleChange}
                placeholder="0 - 24"
                min="0"
                max="24"
                step="0.1"
                required
              />
            </div>


            <div className="form-group">
              <label>Computer Hours</label>

              <input
                type="number"
                name="computer_hours"
                value={formData.computer_hours}
                onChange={handleChange}
                placeholder="0 - 24"
                min="0"
                max="24"
                step="0.1"
                required
              />
            </div>


            <div className="form-group">
              <label>Other Appliance Hours</label>

              <input
                type="number"
                name="other_appliance_hours"
                value={formData.other_appliance_hours}
                onChange={handleChange}
                placeholder="0 - 24"
                min="0"
                max="24"
                step="0.1"
                required
              />
            </div>

          </div>

        </div>


        {/* Previous Consumption */}

        <div className="form-section">

          <h2>Previous Consumption</h2>

          <div className="form-grid">

            <div className="form-group">

              <label>
                Previous Consumption (kWh)
              </label>

              <input
                type="number"
                name="previous_consumption"
                value={formData.previous_consumption}
                onChange={handleChange}
                placeholder="Example: 8.2"
                min="0"
                step="0.1"
                required
              />

            </div>

          </div>

        </div>


        {/* Time Information */}

        <div className="form-section">

          <h2>Time Information</h2>

          <div className="form-grid">

            <div className="form-group">

              <label>
                Hour
              </label>

              <input
                type="number"
                name="hour"
                value={formData.hour}
                onChange={handleChange}
                placeholder="0 - 23"
                min="0"
                max="23"
                required
              />

            </div>


            <div className="form-group">

              <label>
                Day of Week
              </label>

              <select
                name="day_of_week"
                value={formData.day_of_week}
                onChange={handleChange}
                required
              >

                <option value="">
                  Select day
                </option>

                <option value="0">
                  Monday
                </option>

                <option value="1">
                  Tuesday
                </option>

                <option value="2">
                  Wednesday
                </option>

                <option value="3">
                  Thursday
                </option>

                <option value="4">
                  Friday
                </option>

                <option value="5">
                  Saturday
                </option>

                <option value="6">
                  Sunday
                </option>

              </select>

            </div>


            <div className="form-group">

              <label>
                Month
              </label>

              <select
                name="month"
                value={formData.month}
                onChange={handleChange}
                required
              >

                <option value="">
                  Select month
                </option>

                <option value="1">January</option>
                <option value="2">February</option>
                <option value="3">March</option>
                <option value="4">April</option>
                <option value="5">May</option>
                <option value="6">June</option>
                <option value="7">July</option>
                <option value="8">August</option>
                <option value="9">September</option>
                <option value="10">October</option>
                <option value="11">November</option>
                <option value="12">December</option>

              </select>

            </div>

          </div>

        </div>


        <button
          type="submit"
          className="prediction-button"
          disabled={loading}
        >
          {loading
            ? "Predicting..."
            : "Predict Energy Consumption"}
        </button>

      </form>


      {/* Result */}

      {result && (

        <div className="prediction-result">

          <h2>Prediction Result</h2>

          <div className="result-value">

            {result.predicted_energy_consumption}

            <span> kWh</span>

          </div>

          <div className="result-category">

            Energy Status:

            <strong>
              {" "}
              {result.category}
            </strong>

          </div>


          <div className="recommendations">

            <h3>Energy-Saving Recommendations</h3>

            {result.recommendations.map(
              (recommendation, index) => (

                <div
                  className="recommendation"
                  key={index}
                >
                  {recommendation}
                </div>

              )
            )}

          </div>

        </div>

      )}

    </div>
  );
}

export default Prediction;