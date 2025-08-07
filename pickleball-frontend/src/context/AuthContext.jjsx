import { createContext, useContext, useEffect, useState } from "react";
import { getCurrentUser, login, logout as logoutApi } from "../api/auth";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [token, setToken] = useState(localStorage.getItem("authToken"));
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(!!token);

  useEffect(() => {
    if (token) {
      getCurrentUser()
        .then((res) => setUser(res.data))
        .catch(() => {
          setUser(null);
          localStorage.removeItem("authToken");
        })
        .finally(() => setLoading(false));
    }
  }, [token]);

  const handleLogin = async (credentials) => {
    const res = await login(credentials);
    const newToken = res.data.auth_token;
    localStorage.setItem("authToken", newToken);
    setToken(newToken);

    const userRes = await getCurrentUser();
    setUser(userRes.data);
  };

  const handleLogout = async () => {
    await logoutApi();
    localStorage.removeItem("authToken");
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, token, login: handleLogin, logout: handleLogout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
