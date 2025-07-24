import { useState } from "react";

function CreateTournament() {
  const [formData, setFormData] = useState({
    name: "",
    start_date: "",
    end_date: "",
    game_day: "",
    location: "",
  });
  const [message, setMessage] = useState("");
  const [isLeague, setIsLeague] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      const response = await fetch("http://localhost:8000/api/tournaments/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setMessage("✅ Tournament created!");
        setFormData({ name: "", start_date: "", end_date: "", game_day: "", location: "" });
      } else {
        setMessage("❌ Error creating tournament.");
      }
    } catch (err) {
      console.error(err);
      setMessage("❌ Network error.");
    }
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Create Tournament</h2>
      {message && <p className="mb-4">{message}</p>}
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          name="name"
          placeholder="Tournament Name"
          value={formData.name}
          onChange={handleChange}
          className="w-full border px-4 py-2 rounded"
          required
        />
        <label className="flex items-center gap-2 mb-4">
          <input
            type="checkbox"
            checked={isLeague}
            onChange={(e) => setIsLeague(e.target.checked)}
          />
          Multi-week league (more than one game day)
        </label>
        <input
          type="date"
          name="start_date"
          value={formData.start_date}
          onChange={handleChange}
          className="w-full border px-4 py-2 rounded"
          required
        />
        {isLeague && (
          <>
            <input
              type="date"
              name="end_date"
              value={formData.end_date}
              onChange={handleChange}
              className="w-full border px-4 py-2 rounded"
              required={isLeague} 
            />
            <select
              name="game_day"
              value={formData.game_day}
              onChange={handleChange}
              className="w-full border px-4 py-2 rounded"
              required={isLeague} 
            >
              <option value="">Select game day</option>
              {["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].map(
                (day) => (
                  <option key={day} value={day}>
                    {day}
                  </option>
                )
              )}
            </select>
          </>
        )}            
        <input
          type="text"
          name="location"
          placeholder="Location (optional)"
          value={formData.location}
          onChange={handleChange}
          className="w-full border px-4 py-2 rounded"
        />
        <button
          type="submit"
          className="bg-indigo-600 text-white px-6 py-2 rounded hover:bg-indigo-700"
        >
          Create
        </button>
      </form>
    </div>
  );
}

export default CreateTournament;
