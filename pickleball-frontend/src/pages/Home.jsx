import axios from "axios";
import { useEffect, useState } from "react";

function Home() {
  const [tournaments, setTournaments] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/api/tournaments/")
      .then(res => setTournaments(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Tournaments</h1>
      <ul>
        {tournaments.map(t => (
          <li key={t.id}>{t.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Home;
