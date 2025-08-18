import { useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { login } from "../api/auth";

export default function LoginForm() {
  const { register, handleSubmit } = useForm();
  const navigate = useNavigate();
  const [error, setError] = useState("");

  const onSubmit = async (data) => {
    try {
      const response = await login(data);
      localStorage.setItem("authToken", response.data.auth_token);
      setError("");
      navigate("/dashboard"); // 👈 update to your post-login route
    } catch (err) {
      const detail = err?.response?.data;
      if (detail) {
        const messages = Object.entries(detail)
          .flatMap(([field, msgs]) =>
            msgs.map((msg) => `${field}: ${msg}`)
          );
        setError(messages);
      } else {
        setError(["Login failed. Please check your credentials."]);
      }
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded-2xl shadow">
      <h2 className="text-2xl font-bold mb-4">Login</h2>
      {error && <p className="text-red-500 text-sm">{error}</p>}

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        <div>
          <label className="block font-medium">Username</label>
          <input
            {...register("username", { required: true })}
            className="w-full p-2 border rounded"
            autoComplete="username"
          />
        </div>

        <div>
          <label className="block font-medium">Password</label>
          <input
            {...register("password", { required: true })}
            type="password"
            className="w-full p-2 border rounded"
            autoComplete="current-password"
          />
        </div>

        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
        >
          Login
        </button>
      </form>
    </div>
  );
}
