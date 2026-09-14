function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

  const table = document.createElement("table");
  table.innerHTML = `
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Price</th>
        <th>Actions</th>
      </tr>
    </thead>`;

  const tbody = document.createElement("tbody");

  for (const p of products) {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${p.id}</td>
      <td>${escapeHtml(p.name)}</td>
      <td>${p.cost}</td>
      <td class="actions"></td>`;

    const actions = tr.querySelector(".actions")

  table.appendChild(tbody);
  container.replaceChildren(table);
}
