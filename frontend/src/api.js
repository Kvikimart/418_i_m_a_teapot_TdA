const API_URL = "http://localhost:8080/api";

async function health() {
  const res = await fetch(`${API_URL}/v1/health`);
  if (!res.ok) throw new Error(`Health check failed: ${res.status}`);
  return res.json();
}
