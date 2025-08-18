import { API_URL, AUTH_URL } from "../config";
import API from "./axios";

// POST /auth/users/
export async function register(data) {
  return API.post(`${AUTH_URL}/users/`, data);
}

// POST /auth/token/login/
export async function login(data) {
  return API.post(`${AUTH_URL}/token/login/`, data);
}

// POST /auth/token/logout/
export async function logout() {
  return API.post(`${AUTH_URL}/token/logout/`);
}

// GET /api/users/me/
export async function getCurrentUser() {
  return API.get(`${API_URL}/users/me/`);
}
