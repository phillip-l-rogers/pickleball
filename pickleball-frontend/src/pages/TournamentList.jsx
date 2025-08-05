import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { API_BASE } from './config';

function TournamentList() {
  const [tournaments, setTournaments] = useState([]);

  useEffect(() => {
    axios.get(`${API_BASE}/tournaments/`)
      .then(res => setTournaments(res.data))
      .catch(err => console.error(err));
  }, []);


  return (
    <div className="p-6 max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-3xl font-bold">Tournaments</h2>
        <Link
          to="/tournaments/new"
          className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700 transition"
        >
          + Create Tournament
        </Link>
      </div>

      {tournaments.length === 0 ? (
        <p className="text-gray-600">No tournaments yet. Check back soon!</p>
      ) : (
        <ul className="space-y-4">
          {tournaments.map((t) => (
            <li
              key={t.id}
              className="p-4 border rounded hover:shadow transition flex justify-between items-center"
            >
              <div>
                <h3 className="text-xl font-semibold">{t.name}</h3>
                <p className="text-sm text-gray-600">
                  {t.is_league 
                    ? `League • ${t.start_date} → ${t.end_date} · Every ${t.play_day}` 
                    : `One-day • ${t.start_date}`}
                </p>
              </div>
              <Link
                to={`/tournaments/${t.id}`}
                className="text-indigo-600 hover:underline"
              >
                View
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default TournamentList;
