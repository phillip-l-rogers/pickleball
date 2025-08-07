import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Navbar() {
  const { user, logout } = useAuth();

  return (
    <nav className="flex items-center justify-between px-6 py-4 bg-gray-800 text-white">
      <div className="text-lg font-semibold">
        <Link to="/">🏓 Pickleball</Link>
      </div>
      <div className="space-x-4">
        {user ? (
          <>
            <span>Hello, {user.username}!</span>
            <Link to="/dashboard">Dashboard</Link>
            <button onClick={logout} className="text-red-400 hover:underline">
              Logout
            </button>
          </>
        ) : (
          <>
            <Link to="/login" className="hover:underline">Login</Link>
            <Link to="/register" className="hover:underline">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
}
