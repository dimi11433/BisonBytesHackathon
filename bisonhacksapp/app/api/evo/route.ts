import { NextRequest, NextResponse } from "next/server";

export async function GET(req: NextRequest, res: NextResponse) {
  const searchParams = req.nextUrl.searchParams;
  const gene = searchParams.get("gene");
  if (!gene || typeof gene !== "string") {
    return res.json();
  }
  const result = await fetch(`http://127.0.0.1:5000/evo/${gene}`); // Fetch from Python API
  const data = await result.json();
  console.log(data);

  return Response.json(data);
}
