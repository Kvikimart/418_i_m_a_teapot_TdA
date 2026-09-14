import { getHealth } from "./api.js";

export async function renderHealth(el) {
  try {
    const { status } = await getHealth();
    el.textContent = `Status: ${status.toUpperCase()}`;
  } catch {
    el.textContent = "Status: unavailable";
  }
}

renderHealth(document.getElementById("health"));
