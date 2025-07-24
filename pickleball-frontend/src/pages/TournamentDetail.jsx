import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function TournamentDetail() {
  const { id } = useParams(); // ID from route
  const [tournament, setTournament] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`/api/tournaments/${id}/`).then((res) => {
      setTournament(res.data);
      setLoading(false);
    });
  }, [id]);

  if (loading) return <div className="p-6">Loading tournament...</div>;
  if (!tournament) return <div className="p-6">Tournament not found.</div>;

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h2 className="text-3xl font-bold mb-2">{tournament.name}</h2>
      <p className="text-gray-600 mb-4">{tournament.description}</p>
      <p className="mb-2">
        📅 {tournament.start_date} to {tournament.end_date} — every{" "}
        {tournament.play_day}
      </p>
      {isSignedUp ? (
        <button onClick={handleCancel} className="btn btn-outline">
          Cancel Signup
        </button>
      ) : (
        <button onClick={handleSignup} className="btn btn-primary">
          Sign Up
        </button>
      )}
      <div className="mt-6">
        <h3 className="text-xl font-semibold mb-2">Players</h3>
        <ul className="list-disc list-inside">
          {tournament.players?.length > 0 ? (
            tournament.players.map((p) => <li key={p.id}>{p.name}</li>)
          ) : (
            <li>No players signed up yet.</li>
          )}
        </ul>
      </div>
    </div>
  );
}

export default TournamentDetail;
