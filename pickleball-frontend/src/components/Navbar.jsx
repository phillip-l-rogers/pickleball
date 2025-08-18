import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Navbar() {
  const { user, logout } = useAuth();

  return (
    <nav className="bg-gray-800 text-white px-6 py-4 shadow">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <Link to="/" className="text-2xl font-bold tracking-tight hover:text-green-300 transition">
          🏓 Pickleball
        </Link>

        <div className="flex items-center space-x-4 text-sm">
          {user ? (
            <>
              <span className="text-gray-300">Welcome, <strong>{user.username}</strong></span>
              <Link
                to="/dashboard"
                className="bg-green-600 hover:bg-green-700 px-3 py-1.5 rounded text-white"
              >
                Dashboard
              </Link>
              <button
                onClick={logout}
                className="bg-red-500 hover:bg-red-600 px-3 py-1.5 rounded text-white"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <Link
                to="/login"
                className="bg-blue-600 hover:bg-blue-700 px-3 py-1.5 rounded text-white"
              >
                Login
              </Link>
              <Link
                to="/register"
                className="bg-gray-700 hover:bg-gray-600 px-3 py-1.5 rounded text-white"
              >
                Register
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}
