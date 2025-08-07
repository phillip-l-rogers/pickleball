import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import RequireAuth from "./components/RequireAuth";
import { AuthProvider } from "./context/AuthContext";

// Existing pages
import CreateTournament from "./pages/CreateTournament";
import Home from "./pages/Home";
import TournamentDetail from "./pages/TournamentDetail";
import TournamentList from "./pages/TournamentList";

// New auth forms
import LoginForm from "./components/LoginForm";
import RegisterForm from "./components/RegisterForm";

function App() {
  return (
    <Router>
      <AuthProvider>
        <Navbar />

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/tournaments" element={<TournamentList />} />
          <Route path="/tournaments/:id" element={<TournamentDetail />} />

          {/* Protect tournament creation route */}
          <Route
            path="/tournaments/new"
            element={
              <RequireAuth>
                <CreateTournament />
              </RequireAuth>
            }
          />
        </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;
