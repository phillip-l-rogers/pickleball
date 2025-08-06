import { useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { login, register as registerUser } from "../api/auth";

export default function RegisterForm() {
  const { register, handleSubmit } = useForm();
  const navigate = useNavigate();
  const [error, setError] = useState("");

  const onSubmit = async (data) => {
    try {
      await registerUser(data);
      const res = await login({
        username: data.username,
        password: data.password,
      });
      localStorage.setItem("authToken", res.data.auth_token);
      setError("");
      navigate("/dashboard"); // 👈 update to your app route
    } catch (err) {
      setError("Registration failed. Try a different username.");
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded-2xl shadow">
      <h2 className="text-2xl font-bold mb-4">Register</h2>
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
            autoComplete="new-password"
          />
        </div>

        <button
          type="submit"
          className="w-full bg-green-600 text-white py-2 px-4 rounded hover:bg-green-700"
        >
          Register
        </button>
      </form>
    </div>
  );
}
