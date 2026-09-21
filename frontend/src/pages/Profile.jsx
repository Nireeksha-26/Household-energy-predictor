import { useEffect, useState } from "react";


function Profile() {

  const [profile, setProfile] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");


  useEffect(() => {

    fetchProfile();

  }, []);


  const fetchProfile = async () => {

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
        "http://127.0.0.1:5000/api/profile",
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
          "Unable to load profile."
        );

        setLoading(false);

        return;
      }


      setProfile(data);

    } catch (error) {

      setError(
        "Unable to connect to the backend."
      );

    } finally {

      setLoading(false);

    }
  };


  if (loading) {

    return (
      <div className="profile-page">

        <p>
          Loading profile...
        </p>

      </div>
    );
  }


  if (error) {

    return (
      <div className="profile-page">

        <div className="error-message">
          {error}
        </div>

      </div>
    );
  }


  return (

    <div className="profile-page">

      <div className="profile-header">

        <h1>
          My Profile
        </h1>

        <p>
          View your EnergyAI account information.
        </p>

      </div>


      <div className="profile-card">

        <div className="profile-avatar">

          {profile.name
            .charAt(0)
            .toUpperCase()}

        </div>


        <h2>
          {profile.name}
        </h2>


        <p className="profile-email">
          {profile.email}
        </p>


        <div className="profile-details">

          <div className="profile-detail">

            <span>
              Name
            </span>

            <strong>
              {profile.name}
            </strong>

          </div>


          <div className="profile-detail">

            <span>
              Email
            </span>

            <strong>
              {profile.email}
            </strong>

          </div>


          <div className="profile-detail">

            <span>
              Account ID
            </span>

            <strong>
              {profile.id}
            </strong>

          </div>

        </div>

      </div>

    </div>
  );
}


export default Profile;