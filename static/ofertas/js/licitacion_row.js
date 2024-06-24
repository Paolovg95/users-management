const obj = JSON.parse(document.getElementById('items-data').textContent);
for (const [key, value] of Object.entries(obj)) {
  let hiddenRow = document.getElementById(`${key}-row`)
  for (const [ofertante, pricing] of Object.entries(value)) {
    let price = document.getElementById(pricing)
    if (price != null) {
      price.addEventListener("click", function () {
        if (hiddenRow.hidden) {
          hiddenRow.hidden = false
        } else {
          hiddenRow.setAttribute("hidden", true)
        }
      });
    }
  }
}
