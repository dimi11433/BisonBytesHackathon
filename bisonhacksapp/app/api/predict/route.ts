import { NextRequest, NextResponse } from "next/server";

export async function GET(req: NextRequest) {
  const url = new URL(req.url);
  const searchParams = url.searchParams.get("data");  // Get all 'data' values
  

  // Build query string: ?data=val1&data=val2&data=val3...
  const queryString = `data=${encodeURIComponent(searchParams ?? '')}`;
  console.log(queryString);

  // Send GET request to Flask API with query string
  const flaskUrl = `http://127.0.0.1:5000/predict?${queryString}`;
  const result = await fetch(flaskUrl);

  const data = await result.json();
  //   console.log(data); // Log the prediction response

  return NextResponse.json(data); // Return Flask's response to frontend
}