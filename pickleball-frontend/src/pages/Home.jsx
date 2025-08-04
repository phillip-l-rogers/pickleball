import axios from "axios";
import { useEffect, useState } from "react";

function Home() {
  const [tournaments, setTournaments] = useState([]);

  useEffect(() => {
    axios.get("/api/tournaments/")
      .then(res => setTournaments(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Tournaments</h1>
      {tournaments.length === 0 ? (
        <p className="text-gray-600">No tournaments yet. Check back soon!</p>
      ) : (
        <ul className="space-y-2">
          {tournaments.map((t) => (
            <li key={t.id} className="border p-2 rounded">{t.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Home;
