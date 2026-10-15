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

async function loadStops() {
  const imageUrlEl = document.getElementById("image_url");
  const idEl = document.getElementById("id");
  const nameEl = document.getElementById("name");
  const xEl = document.getElementById("x");
  const yEl = document.getElementById("y");
  const wheelchairAccessibleEl = document.getElementById("wheelchair_accessible");
  const hasShelterEl = document.getElementById("has_shelter");
  const hasBenchEl = document.getElementById("has_bench");
  const hasTicketMachineEl = document.getElementById("has_ticket_machine");
  const isTransferEl = document.getElementById("is_transfer");
  try {
    const response = await fetch('/api/v1/stops');
    const data = await response.json();
    const stop = Array.isArray(data) ? data[0] : data;
    if (!stop) return;

    if (imageUrlEl && stop.image_url) imageUrlEl.src = stop.image_url;
    if (idEl) idEl.textContent = String(stop.id).padStart(3, '0');
    if (nameEl) nameEl.textContent = stop.name;
    if (xEl) xEl.textContent = stop.x;
    if (yEl) yEl.textContent = stop.y;
    if (wheelchairAccessibleEl) wheelchairAccessibleEl.textContent = String(stop.wheelchair_accessible);
    if (hasShelterEl) hasShelterEl.textContent = String(stop.has_shelter);
    if (hasBenchEl) hasBenchEl.textContent = String(stop.has_bench);
    if (hasTicketMachineEl) hasTicketMachineEl.textContent = String(stop.has_ticket_machine);
    if (isTransferEl) isTransferEl.textContent = String(stop.is_transfer);

  } catch (error) {
    console.error("Error loading bus stop data:", error);
  }
}

loadStops();
