'use client';
import { useRouter } from "next/navigation";


const Page = () => {
  const router = useRouter();
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <button onClick={() => router.push("/dashboard/Jeff")} className="bttn">
        Go to user
      </button>
    </div>
  );
}

export default Page;