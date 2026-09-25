const API_BASE = "/api/v1";

export async function getHealth() {
  const res = await fetch(`${API_BASE}/health`);
  if (!res.ok) throw new Error(`Health check failed: ${res.status}`);
  return res.json();
}

export async function getTeam() {
  const res = await fetch(`${API_BASE}/team`);
  if (!res.ok) throw new Error(`Team failed: ${res.status}`);
  return res.json();
}

export async function getStops() {
  const res = await fetch(`${API_BASE}/stops`);
  if (!res.ok) throw new Error(`Loading stops failed: ${res.status}`);
  return res.json();
}
