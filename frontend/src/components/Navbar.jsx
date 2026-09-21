function Navbar({ currentPage, setCurrentPage }) {
  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("user");

    window.location.reload();
  };

  return (
    <nav className="navbar">

      <div className="navbar-logo">
        <h2>EnergyAI</h2>
      </div>

      <div className="navbar-links">

        <button
          className={
            currentPage === "dashboard"
              ? "nav-button active"
              : "nav-button"
          }
          onClick={() => setCurrentPage("dashboard")}
        >
          Dashboard
        </button>

        <button
          className={
            currentPage === "prediction"
              ? "nav-button active"
              : "nav-button"
          }
          onClick={() => setCurrentPage("prediction")}
        >
          Prediction
        </button>

        <button
          className={
            currentPage === "history"
              ? "nav-button active"
              : "nav-button"
          }
          onClick={() => setCurrentPage("history")}
        >
          History
        </button>

        <button
          className={
            currentPage === "analytics"
              ? "nav-button active"
              : "nav-button"
          }
          onClick={() => setCurrentPage("analytics")}
        >
          Analytics
        </button>

        <button
          className={
            currentPage === "profile"
              ? "nav-button active"
              : "nav-button"
          }
          onClick={() => setCurrentPage("profile")}
        >
          Profile
        </button>

        <button
          className="logout-button"
          onClick={handleLogout}
        >
          Logout
        </button>

      </div>

    </nav>
  );
}

export default Navbar;