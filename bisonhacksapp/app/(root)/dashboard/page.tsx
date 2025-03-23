'use client';

import { useRouter } from "next/navigation";
import users from "@/constants/users";

const Page = () => {
  const router = useRouter();

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
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
  );
};

export default Page;