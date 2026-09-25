import { getHealth, getTeam } from "./api.js";

export async function renderHealth(el) {
  try {
    const { status } = await getHealth();
    el.textContent = `Status: ${status.toUpperCase()}`;
  } catch {
    el.textContent = "Status: unavailable";
  }
}

renderHealth(document.getElementById("health"));

async function loadTeam() {
  const nameEl = document.getElementById("team-name");
  const membersEl = document.getElementById("team-members");
  try {
    const { name, members } = await getTeam();
    nameEl.textContent = name;
    membersEl.textContent = members;
  } catch {
    nameEl.textContent = "Team unavailable";
    membersEl.textContent = "";
  }
}

loadTeam();

async function loadStosp() {
  const imageEl = document.getElementById("imageURL");
  const idEl = document.getElementById("id");
  const nameEl = document.getElementById("name");
  const xEl = document.getElementById("x");
  const yEl = document.getElementById("y");
  const wheelEl = document.getElementById("wheelAccessible");
  const shelterEl = document.getElementById("shelter");
  const benchEl = document.getElementById("bench");
  const machineEl = document.getElementById("ticketMachine");
  const transferEl = document.getElementById("transfer");
  try {
    const response = await fetch('/api/v1/stops');
    const data = await response.json();
    if (imageEl && data.imageURL) imageEl.src = data.imageURL;
    if (idEl) idEl.textContent = String(data.id).padStart(3, '0');
    if (nameEl) nameEl.textContent = data.name;
    if (xEl) xEl.textContent = data.x;
    if (yEl) yEl.textContent = data.y;
    if (wheelEl) wheelEl.textContent = data.wheelAccessible;
    if (shelterEl) shelterEl.textContent = data.shelter;
    if (benchEl) benchEl.textContent = data.bench;
    if (machineEl) machineEl.textContent = data.ticketMachine;
    if (transferEl) transferEl.textContent = data.transfer;

  } catch (error) {
    console.error("Error loading bus stop data:", error);
  }
}

loadStops();
