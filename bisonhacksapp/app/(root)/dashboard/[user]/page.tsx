import users from "@/constants/users";
import Guage from "@/components/ui/guage";

const Page = async ({params, searchParams}: {
    params: Promise<{ user: string }>
    searchParams: Promise<{ [key: string]: string | string[] | undefined }>
  }) => {

  const user = (await params).user;

  const userInfo = users.find((u) => u.name === user);

  return (
    <div>
      <h1>Hello {user}</h1>
      <Guage />
    </div>
  );
}

export default Page;