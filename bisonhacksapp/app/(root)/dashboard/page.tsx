'use client';

import { useRouter } from "next/navigation";
import users from "@/constants/users";
import Image from "next/image";

const Page = () => {
  const router = useRouter();

  return (
    <div className="p-6">
      {/* Logo and Doctor's Name */}
      <div className="flex flex-col items-center mb-6">
        <Image src="/bisonbytes.jpeg" alt="BisonBytes Logo" width={100} height={100} className="mb-2" />
        <h1 className="text-2xl font-bold text-gray-800">Dr. Bison</h1>
      </div>
      
      {/* Profile Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {users.map((user, index) => (
          <div
            key={index}
            className="bg-white shadow-lg rounded-2xl p-4 flex flex-col items-center hover:shadow-xl transition cursor-pointer"
            onClick={() => router.push(`/dashboard/${user.name}`)}
          >
            <h2 className="text-xl font-semibold text-gray-700">{user.name}</h2>
            <p className="text-gray-500">Age: {user.Age}</p>
            <button className="mt-2 px-4 py-2 bg-blue-500 text-white rounded-lg" onClick={() => router.push(`/dashboard/${user.name}`)}>View Profile</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Page;
