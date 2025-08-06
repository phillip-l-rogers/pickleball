import API from "./axios";

export const getTournaments = () => API.get("/api/tournaments/");
export const getTournamentById = (id) => API.get(`/api/tournaments/${id}/`);
export const createTournament = (data) => API.post("/api/tournaments/", data);
