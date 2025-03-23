'use client';

import { useRouter } from "next/navigation";
import users from "@/constants/users";
import Image from "next/image";

const Page = () => {
  const router = useRouter();

  return (
    <div className="p-6 bg-gradient-to-r from-blue-100 via-green-100 to-pink-100">
      {/* Logo and Doctor's Name */}
      <div className="flex flex-col items-center mb-6">
        <Image src="/bisonbytes.jpeg" alt="BisonBytes Logo" width={150} height={150} className="mb-2" />
        <h1 className="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 via-pink-500 to-red-500">
          Dr. Bison
        </h1>
      </div>

      {/* Profile Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {users.map((user, index) => (
          <div
            key={index}
            className="bg-white shadow-xl rounded-2xl p-4 flex flex-col items-center hover:scale-105 transform transition duration-300 cursor-pointer animate-fade-in"
            onClick={() => router.push(`/dashboard/${user.name}`)}
          >
            <h2 className="text-xl font-semibold text-gray-700">{user.name}</h2>
            <p className="text-gray-500">Age: {user.Age}</p>
            <p className="text-gray-500">Heart Rate: {user.Heartrate} BPM</p>
            <p className="text-gray-500">Temp: {user.Temp}</p>
            <button className="mt-2 px-4 py-2 bg-blue-500 text-white rounded-lg" onClick={() => router.push(`/dashboard/${user.name}`)}>View Profile</button>
          </div>
        ))}
      </div>

      {/* Footer */}
      <footer className="bg-gray-800 text-white py-4">
        <div className="flex justify-center space-x-4">
          <a href="#" className="text-blue-400">Facebook</a>
          <a href="#" className="text-blue-400">Twitter</a>
          <a href="#" className="text-blue-400">LinkedIn</a>
        </div>
      </footer>
    </div>
  );
};

export default Page;
