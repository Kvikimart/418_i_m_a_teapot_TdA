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
