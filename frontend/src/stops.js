import { getStops } from "./api.js";

const STOP_COLUMNS = 12;

function yesNo(value) {
  return value ? "✓" : "–";
}

function formatLines(value) {
  return value ? value.split(";").join(", ") : "–";
}

function cell(content) {
  const td = document.createElement("td");
  if (content instanceof Node) td.append(content);
  else td.textContent = content;
  return td;
}

function stopRow(stop) {
  const tr = document.createElement("tr");

  let photo = "–";
  if (stop.image_url) {
    photo = document.createElement("img");
    photo.src = stop.image_url;
    photo.alt = stop.name;
    photo.className = "stop-thumb";
    photo.loading = "lazy";
  }

  tr.append(
    cell(photo),
    cell(String(stop.id).padStart(3, "0")),
    cell(stop.name),
    cell(formatLines(stop.lines)),
    cell(stop.is_transfer ? formatLines(stop.transfer_lines) : "–"),
    cell(String(stop.x)),
    cell(String(stop.y)),
    cell(yesNo(stop.wheelchair_accessible)),
    cell(yesNo(stop.has_shelter)),
    cell(yesNo(stop.has_bench)),
    cell(yesNo(stop.has_ticket_machine)),
    cell(yesNo(stop.has_display)),
  );
  return tr;
}

function messageRow(text) {
  const tr = document.createElement("tr");
  const td = cell(text);
  td.colSpan = STOP_COLUMNS;
  tr.append(td);
  return tr;
}

async function loadStops() {
  const body = document.getElementById("stops-body");
  if (!body) return;

  try {
    const stops = await getStops();
    body.replaceChildren(
      ...(stops.length ? stops.map(stopRow) : [messageRow("No stops found.")]),
    );
  } catch (error) {
    console.error("Error loading bus stop data:", error);
    body.replaceChildren(messageRow("Could not load stops."));
  }
}

loadStops();
