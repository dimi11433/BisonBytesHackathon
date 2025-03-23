'use client';

import { useRouter } from "next/navigation";
import users from "@/constants/users";
import Image from "next/image";
import { useEffect, useState } from "react";

const Page = () => {
  const router = useRouter();
  const [name, setName] = useState("");

  function convertValuesToString(obj: { [key: string]: any }): { [key: string]: string } {
    const result: { [key: string]: string } = {};
  
    for (const key in obj) {
      if (typeof obj[key] === 'number') {
        result[key] = obj[key].toString(); // or String(obj[key])
      } else {
        result[key] = obj[key]; // keep the value unchanged if it's not a number
      }
    }
  
    return result;
  }

  useEffect(() => {
    const fetchServerInfo = async () => {
      const res = await fetch("/api/server-name"); 
      console.log(res);
      const data = await res.json();
      setName(data.name);
    }

    users.forEach(async (userData) => {
      const queryString = new URLSearchParams(convertValuesToString(userData)).toString();
      // console.log(queryString);
      const res = await fetch(`/api/predict?data=${userData}`);
      console.log(res);
      const data = await res.json();
      console.log(data);
      if (data.prediction == "Low") {
        alert(`High risk detected for ${userData.name}`);
      } else if (data.prediction == "Medium") {
        alert(`Medium risk detected for ${userData.name}`);
      }
    }
  );

    fetchServerInfo();
  }, []);

  return (
    <div className="p-6" style={{ backgroundColor: "#16113a" }}>
      {/* Logo and Doctor's Name */}
      <div className="flex flex-col items-center mb-6">
        <Image src="/bisonbytes.jpeg" alt="BisonBytes Logo" width={150} height={150} className="mb-2" />
        <h1 className="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 via-pink-500 to-red-500">
          {name}
        </h1>
      </div>

      {/* Profile Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {users.map((user, index) => (
          <div
            key={index}
            className="bg-gray-800 text-white shadow-xl rounded-2xl p-4 flex flex-col items-center hover:scale-105 transform transition duration-300 cursor-pointer animate-fade-in"
            onClick={() => router.push(`/dashboard/${user.name}`)}
          >
            <h2 className="text-xl font-semibold">{user.name}</h2>
            <p className="text-white-400">Age: {user.Age}</p>
            <p className="text-white-400">Heart Rate: {user.Heartrate} BPM</p>
            <p className="text-white-400">Temp: {user.Temp}</p>
            <button
              className="mt-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg transition duration-300"
              onClick={() => router.push(`/dashboard/${user.name}`)}
            >
              View Profile
            </button>
          </div>
        ))}
      </div>

      {/* Footer */}
      <footer className="bg-gray-800 text-white py-4">
        <div className="flex justify-center space-x-4">
          <a href="#" className="text-blue-400 hover:text-blue-500">Facebook</a>
          <a href="#" className="text-blue-400 hover:text-blue-500">Twitter</a>
          <a href="#" className="text-blue-400 hover:text-blue-500">LinkedIn</a>
        </div>
      </footer>
    </div>
  );
};

export default Page;
