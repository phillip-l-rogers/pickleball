import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  base: "./", // ✅ Required for relative asset paths on Render
  build: {
    outDir: "dist",
  },
  server: {
    historyApiFallback: true, // ✅ Helps dev server with SPA routes
  },
});
