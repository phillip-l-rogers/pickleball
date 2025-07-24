// src/components/SignupForm.jsx

import axios from "axios";
import { useState } from "react";

function SignupForm({ tournamentId }) {
  const [status, setStatus] = useState(null);

  const handleSignup = async () => {
    try {
      await axios.post("/api/signup/", {
        tournament: tournamentId,
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`
        }
      });
      setStatus("You’ve successfully signed up!");
    } catch (err) {
      console.error(err);
      setStatus("Signup failed.");
    }
  };

  return (
    <div>
      <button
        onClick={handleSignup}
        className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
      >
        Join Tournament
      </button>
      {status && <p className="mt-2 text-sm">{status}</p>}
    </div>
  );
}

export default SignupForm;
