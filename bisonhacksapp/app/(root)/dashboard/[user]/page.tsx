import Image from "next/image";
import Link from "next/link";

import users from "@/constants/users";
import Guage from "@/components/ui/guage";
import LabTestResults from "@/constants/testResults";

const Page = async ({
  params,
  searchParams,
}: {
  params: Promise<{ user: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) => {
  const user = (await params).user;

  const userInfo = users.find((u) => u.name === user);

  const isBloodSuagrGood =
    (userInfo?.Blood_Sugar ?? 90) < 90 && (userInfo?.Blood_Sugar ?? 90) > 70;

  return (
    <div className="flex flex-col h-screen w-screen">
      <div className="flex justify-between p-6 ">
        <div className="flex items-center gap-2">
          <Image src="/person.png" alt="Image of User" width={20} height={20} />
          <h1>{user}'s Health Analysis Dashboard</h1>
        </div>
        <div>
          <p>My profile</p>
        </div>
      </div>
      <div className="flex flex-row">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 place-items-center gap-6 w-[40vw] p-4 mx-4 h-max hover-container">
          <Guage
            name="Heart Rate"
            limits={[50, 65, 81, 98]}
            max={130}
            min={20}
            value={userInfo?.Heartrate ?? 60}
            unit="bpm"
          />
          <Guage
            name="Temperature"
            limits={[95, 97, 98.6, 100.4]}
            max={105}
            min={91}
            value={userInfo?.Temp ?? 97}
            unit="ºF"
          />
          <Guage
            name="Blood Pressure"
            limits={[120, 129, 139, 150]}
            max={160}
            min={100}
            value={userInfo?.BP_Systolic ?? 100}
            unit="mmHg"
            range_type="inc"
          />
          <Guage
            name="Respiratory Rate"
            limits={[10, 12, 20, 25]}
            max={30}
            min={5}
            value={userInfo?.Respiratory_Rate ?? 12}
            unit="bpm"
          />
          <Guage
            name="Oxygen Level"
            limits={[80, 85, 90, 95]}
            max={100}
            min={70}
            value={userInfo?.Oxygen_Level ?? 100}
            unit="mmHg"
            range_type="dec"
          />
          <div className="hover-container p-5 flex flex-col shadow-xl rounded-2xl bg-[#16113a]">
            {/* <h2 className="text-xl font-semibold text-gray-700">Blood Sugar Level</h2> */}
            <p className="font-bold">
              Blood Sugar Level: {userInfo?.Blood_Sugar}
            </p>
            <p>
              Status:{" "}
              <span
                className={
                  isBloodSuagrGood
                    ? "text-green-600 font-bold"
                    : "text-red-600 font-bold"
                }
              >
                {isBloodSuagrGood ? "Good" : "Bad"}
              </span>
            </p>
            <button className="mt-2 px-4 py-2 bg-blue-500 text-white rounded-lg">
              Edit
            </button>
          </div>
        </div>

        {/* Start here */}
        <div className="flex flex-col items-center space-y-4">
          {/* First Container */}
          <div className="hover-container w-64 h-32 flex flex-col justify-center items-center w-full">
            <p className="text-lg font-medium text-center">Age: {userInfo?.Age}</p>
            <p className="text-lg font-medium text-center">Weight: {userInfo?.Weight}</p>
            <p className="text-lg font-medium text-center">BMI: {userInfo?.BMI}</p>
          </div>

          {/* Second and Third Containers (Side by Side) */}
          <div className="flex space-x-4 flex-grow">
            {/* Second Container */}
            <div className="hover-container w-64 h-40 flex flex-col justify-center items-center h-full">
              <p className="text-lg font-medium text-center">Sleep: {userInfo?.Sleep_Duration}</p>
              <p className="text-lg font-medium text-center">Sleep Quantity: {userInfo?.Sleep_Quantity}</p>
              <p className="text-lg font-medium text-center">Water: {userInfo?.Water_Intake} L</p>
            </div>

            {/* Third Container */}
            <div className="hover-container w-64 h-40 flex flex-col justify-center items-center h-full">
              <p className="text-lg font-medium text-center">Sleep Consistency: {userInfo?.Sleep_Consistency}</p>
              <p className="text-lg font-medium text-center">Steps: {userInfo?.Steps}</p>
              <p className="text-lg font-medium text-center">Active Training Hours: {userInfo?.Strength_Training} hrs</p>
            </div>
          </div>
        </div>



        {/* End here */}

        <div className="flex flex-col gap-4 m-4 w-100">
          <div className="hover-container flex-grow p-4 flex flex-col justify-between items-center">
            <h2 className="text-xl font-bold">Lab Test Results</h2>
            <table className="table-auto border-collapse w-full">
              <thead>
                <tr className="border-b">
                  <th className="px-4 py-2">Lab Test</th>
                  <th className="px-4 py-2">Result</th>
                  <th className="px-4 py-2">Normal Range</th>
                </tr>
              </thead>
              <tbody>
                {LabTestResults.slice(0, 5).map((result, index) => (
                  <tr key={index} className="border-b">
                    <td className="px-4 py-2">{result["Lab Test"]}</td>
                    <td className="px-4 py-2">{result.Result}</td>
                    <td className="px-4 py-2">{result["Normal Range"]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            <div className="align-items-start w-full">
              <Link href={""} className="text-blue-500">
                View More
              </Link>
            </div>
          </div>
          <div className="hover-container flex-grow">Evo-2 Results</div>
          <div className="hover-container flex-grow">Analysis</div>
        </div>
      </div>
    </div>
  );
};

export default Page;
