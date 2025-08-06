import API from "./axios";

// POST /auth/users/
export const register = (data) => API.post("/auth/users/", data);

// POST /auth/token/login/
export const login = (data) => API.post("/auth/token/login/", data);

// POST /auth/token/logout/
export const logout = () => API.post("/auth/token/logout/");

// GET /api/users/me/
export const getCurrentUser = () => API.get("/api/users/me/");
