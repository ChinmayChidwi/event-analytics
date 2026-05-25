"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import api from "../lib/api";

export default function LoginPage() {

  const router = useRouter();

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");


  const handleLogin = async () => {

    try {

      const formData = new FormData();

      formData.append(
        "username",
        email
      );

      formData.append(
        "password",
        password
      );

      const response = await api.post(
        "/auth/login",
        formData,
        {
          headers: {
            "Content-Type":
              "application/x-www-form-urlencoded"
          }
        }
      );

      localStorage.setItem(
        "token",
        response.data.access_token
      );

      router.push("/dashboard");

    } catch (error) {

      console.error(error);

      alert("Login failed");
    }
  };


  return (

    <div className="flex items-center justify-center h-screen bg-gray-100">

      <div className="bg-white p-10 rounded-lg shadow-lg w-[400px]">

        <h1 className="text-3xl font-bold mb-6 text-center">
          Login
        </h1>

        <input
          className="border p-3 w-full mb-4 rounded"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <input
          className="border p-3 w-full mb-4 rounded"
          placeholder="Password"
          type="password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button
          className="bg-black text-white w-full p-3 rounded hover:bg-gray-800"
          onClick={handleLogin}
        >
          Login
        </button>

      </div>

    </div>
  );
}