export async function GET() {
    const res = await fetch("http://127.0.0.1:5000/doctor"); // Fetch from Python API
    const data = await res.json();

    return Response.json(data);
}


