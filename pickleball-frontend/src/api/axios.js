import axios from "axios";
import { BASE_URL } from "../config";

const API = axios.create({
  baseURL: BASE_URL,
  withCredentials: false, // tokens will be in headers, not cookies
});

API.interceptors.request.use((config) => {
  const token = localStorage.getItem("authToken");
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

export default API;
