import { API_URL } from "../config";
import API from "./axios";

// GET /api/tournaments
export async function getTournaments() {
  return API.get(`${API_URL}//`);
}

// GET /api/tournaments/id/
export async function getTournamentById(id) {
  return API.get(`${API_URL}/tournaments/${id}/`);
}

// POST /api/tournaments/
export async function createTournament(data) {
  return API.post(`${API_URL}/tournaments/`, data);
}
