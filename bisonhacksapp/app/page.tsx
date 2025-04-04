'use client';
import { useRouter } from "next/navigation";


const Home = () => {
  const router = useRouter();
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <button onClick={() => router.push("/dashboard")} className="bttn">
        Go to dashboard
      </button>
    </div>
  );
}

export default Home;