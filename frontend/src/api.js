const API_URL = "http://localhost:8080/api";

const API_BASE = "/api/v1";

export async function getHealth() {
  const res = await fetch(`${API_BASE}/health`);
  if (!res.ok) throw new Error(`Health check failed: ${res.status}`);
  return res.json();
}
