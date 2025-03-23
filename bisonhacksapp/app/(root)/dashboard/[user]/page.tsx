import Image from 'next/image';

import users from "@/constants/users";
import Guage from "@/components/ui/guage";

const Page = async ({
  params,
  searchParams,
}: {
  params: Promise<{ user: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) => {
  const user = (await params).user;

  const userInfo = users.find((u) => u.name === user);

  return (
    <div>
      <div className="flex justify-between p-6 ">
        <div className="flex items-center gap-2">
          <Image src="/person.png" alt='Image of User' width={20} height={20}/>
          <h1>{user}'s Health Analysis Dashboard</h1>
        </div>
        <div>
          <p>My profile</p>
        </div>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 place-items-center gap-6 p-6">
        <Guage
          name="heart rate"
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
          name="BP_Systolic"
          limits={[120, 129, 139, 150]}
          max={160}
          min={100}
          value={userInfo?.BP_Systolic ?? 100}
          unit="mmHg"
          range_type="inc"
        />
        <Guage
          name="Respiratory_Rate"
          limits={[10, 12, 20, 25]}
          max={30}
          min={5}
          value={userInfo?.Respiratory_Rate ?? 12}
          unit="bpm"
        />
        <Guage
          name="Oxygen_Level"
          limits={[80, 85, 90, 95]}
          max={100}
          min={70}
          value={userInfo?.Oxygen_Level ?? 100}
          unit="mmHg"
          range_type="dec"
        />
      </div>
    </div>
  );
};

export default Page;
