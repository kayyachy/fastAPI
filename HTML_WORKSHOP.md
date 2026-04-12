# 🛒 HTML Workshop — Bouw een Product Winkel stap voor stap

> **Doel van deze workshop:** Een interactieve webwinkel bouwen met alleen HTML, CSS en vanilla JavaScript. Geen frameworks, geen build-tools — gewoon één bestand.

---

## 📌 Inhoudsopgave

1. [Wat gaan we bouwen?](#1-wat-gaan-we-bouwen)
2. [Vereisten](#2-vereisten)
3. [Project opzetten](#3-project-opzetten)
4. [Stap 1 — HTML skelet](#stap-1--html-skelet)
5. [Stap 2 — CSS reset en body](#stap-2--css-reset-en-body)
6. [Stap 3 — Header](#stap-3--header)
7. [Stap 4 — Layout met CSS Grid](#stap-4--layout-met-css-grid)
8. [Stap 5 — Product toevoegen formulier](#stap-5--product-toevoegen-formulier)
9. [Stap 6 — Producten grid](#stap-6--producten-grid)
10. [Stap 7 — Winkelwagen panel](#stap-7--winkelwagen-panel)
11. [Stap 8 — Klantgegevens formulier](#stap-8--klantgegevens-formulier)
12. [Stap 9 — Toast melding](#stap-9--toast-melding)
13. [Stap 10 — JavaScript: data en hulpfuncties](#stap-10--javascript-data-en-hulpfuncties)
14. [Stap 11 — JavaScript: product toevoegen](#stap-11--javascript-product-toevoegen)
15. [Stap 12 — JavaScript: grid renderen](#stap-12--javascript-grid-renderen)
16. [Stap 13 — JavaScript: winkelwagen renderen](#stap-13--javascript-winkelwagen-renderen)
17. [Stap 14 — JavaScript: checkout](#stap-14--javascript-checkout)
18. [Eindresultaat overzicht](#eindresultaat-overzicht)

---

## 1. Wat gaan we bouwen?

Een interactieve productwinkel met:

- **Eigen producten toevoegen** via een invoerveld
- **Hoeveelheid aanpassen** met +/− knoppen op elke productkaart
- **Winkelwagen** die automatisch bijwerkt
- **Klantgegevens** invullen (naam, telefoonnummer, optioneel vekil)
- **Bestelling plaatsen** die een betalingslink opent
- **Toast meldingen** voor feedback

Alles in één HTML-bestand, geen externe afhankelijkheden.

---

## 2. Vereisten

- Een teksteditor (VS Code)
- Een moderne browser (Chrome, Firefox, Edge)
- Basiskennis HTML en CSS

---

## 3. Project opzetten

Maak een nieuw bestand aan:

```
docs/
└── index.html
```

Open `index.html` in VS Code. Gebruik de Live Server extensie om wijzigingen live te zien:

1. Installeer **Live Server** in VS Code
2. Klik rechtsonder op **Go Live**
3. De pagina herlaadt automatisch bij elke opslag

---

## Stap 1 — HTML skelet

Start met de basisstructuur van elk HTML-document:

```html
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Product Winkel</title>
</head>
<body>

</body>
</html>
```

### Uitleg

- `<!DOCTYPE html>` — vertelt de browser dat dit HTML5 is
- `lang="nl"` — taal instellen op Nederlands (goed voor toegankelijkheid)
- `charset="UTF-8"` — zorgt voor correcte weergave van Nederlandse tekens (é, ë, ij)
- `viewport` meta-tag — zorgt dat de pagina goed schaalt op mobiele apparaten

---

## Stap 2 — CSS reset en body

Voeg een `<style>` tag toe in de `<head>`. Begin met een reset zodat alle browsers hetzelfde startpunt hebben:

```css
<style>
  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Segoe UI', system-ui, sans-serif;
    background: #f0f2f5;
    color: #1a1a2e;
    min-height: 100vh;
  }
</style>
```

### Uitleg

- `box-sizing: border-box` — padding en border worden meegeteld in de breedte van een element
- `margin: 0; padding: 0` — browsers voegen standaard marges toe, die resetten we hier
- `system-ui` — gebruikt het standaard lettertype van het besturingssysteem als fallback

---

## Stap 3 — Header

Voeg in de `<body>` een header toe:

```html
<header>
  <span>🛒</span>
  <h1>Product Winkel</h1>
</header>
```

En de bijbehorende CSS:

```css
header {
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  color: white;
  padding: 1.5rem 2rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: 0 2px 12px rgba(0,0,0,0.3);
}

header h1 { font-size: 1.6rem; font-weight: 700; }
header span { font-size: 1.8rem; }
```

### Uitleg

- `linear-gradient` — verloopkleur van donkerblauw naar nog donkerder blauw
- `display: flex; align-items: center` — zet het emoji-icoon en de h1 naast elkaar, verticaal gecentreerd
- `gap: 1rem` — ruimte tussen het emoji-icoon en de tekst

---

## Stap 4 — Layout met CSS Grid

Voeg een container toe die de pagina opdeelt in twee kolommen: catalogus links, winkelwagen rechts.

```html
<div class="container">

  <!-- Links: catalogus -->
  <div>
    <!-- producten komen hier -->
  </div>

  <!-- Rechts: winkelwagen -->
  <div class="cart-panel">
    <!-- winkelwagen komt hier -->
  </div>

</div>
```

CSS voor de layout:

```css
.container {
  max-width: 1100px;
  margin: 2rem auto;
  padding: 0 1.5rem;
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 2rem;
}

@media (max-width: 768px) {
  .container { grid-template-columns: 1fr; }
}
```

### Uitleg

- `grid-template-columns: 1fr 340px` — de linkerkolom neemt alle resterende ruimte, de rechterkolom is altijd 340px breed
- `margin: 2rem auto` — centreert de container horizontaal
- `@media (max-width: 768px)` — op kleine schermen worden de kolommen gestapeld

Voeg ook de herbruikbare `.card` stijl toe die we voor beide panelen gebruiken:

```css
.card {
  background: white;
  border-radius: 16px;
  padding: 1.8rem;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}

.card h2 {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 1.2rem;
  color: #16213e;
  display: flex;
  align-items: center;
  gap: .5rem;
}
```

---

## Stap 5 — Product toevoegen formulier

Voeg in de linkerkolom een kaart toe met een invoerveld en knop:

```html
<div class="card">
  <h2>➕ Product toevoegen</h2>
  <div class="add-form">
    <input type="text" id="productInput" placeholder="Naam van het product…" maxlength="50" />
    <button class="btn btn-primary" onclick="addProduct()">Toevoegen</button>
  </div>

  <h2>📦 Producten <span id="productCount" style="color:#a0aec0; font-weight:400; font-size:.9rem;">(0)</span></h2>
  <div class="product-grid" id="productGrid">
    <div class="empty-state">
      <span class="empty-icon">📭</span>
      Voeg je eerste product toe via het formulier hierboven.
    </div>
  </div>
</div>
```

CSS voor het formulier en knoppen:

```css
.add-form {
  display: flex;
  gap: .75rem;
  margin-bottom: 1.8rem;
}

.add-form input {
  flex: 1;
  padding: .7rem 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  font-size: .95rem;
  transition: border-color .2s;
  outline: none;
}

.add-form input:focus { border-color: #6c63ff; }

.btn {
  padding: .7rem 1.2rem;
  border: none;
  border-radius: 10px;
  font-size: .95rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform .1s, box-shadow .2s;
}

.btn:active { transform: scale(.97); }

.btn-primary {
  background: #6c63ff;
  color: white;
  box-shadow: 0 4px 12px rgba(108,99,255,.35);
}

.btn-primary:hover { background: #574fd6; }
```

### Uitleg

- `flex: 1` op het input-veld — het invoerveld groeit om alle beschikbare ruimte te vullen
- `outline: none` — verbergt de standaard browser-focusring, we tonen onze eigen via `border-color`
- `transition` — zorgt voor vloeiende animaties bij hover en focus

---

## Stap 6 — Producten grid

CSS voor de productkaarten:

```css
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1rem;
}

.product-item {
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .6rem;
  cursor: pointer;
  transition: border-color .2s, box-shadow .2s, transform .15s;
  background: #fafafa;
  position: relative;
  user-select: none;
}

.product-item:hover {
  border-color: #6c63ff;
  box-shadow: 0 4px 14px rgba(108,99,255,.2);
  transform: translateY(-2px);
}

.product-item.selected {
  border-color: #6c63ff;
  background: #f0eeff;
}

.product-item .checkmark {
  position: absolute;
  top: .5rem;
  right: .6rem;
  font-size: .9rem;
  opacity: 0;
  transition: opacity .2s;
}

.product-item.selected .checkmark { opacity: 1; }

.product-icon { font-size: 2.2rem; }

.product-name {
  font-size: .9rem;
  font-weight: 600;
  text-align: center;
}

.product-price {
  font-size: .85rem;
  color: #6c63ff;
  font-weight: 700;
}
```

CSS voor de hoeveelheidscontrols op elke kaart:

```css
.qty-controls {
  display: flex;
  align-items: center;
  gap: .5rem;
  margin-top: .2rem;
}

.qty-btn {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: 2px solid #6c63ff;
  background: white;
  color: #6c63ff;
  font-size: 1rem;
  cursor: pointer;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background .15s, color .15s;
}

.qty-btn:hover { background: #6c63ff; color: white; }

.qty-value {
  font-size: .95rem;
  font-weight: 700;
  min-width: 20px;
  text-align: center;
}

.empty-state {
  grid-column: 1/-1;
  text-align: center;
  padding: 3rem 1rem;
  color: #a0aec0;
}

.empty-state .empty-icon { font-size: 3rem; display: block; margin-bottom: .8rem; }
```

### Uitleg

- `repeat(auto-fill, minmax(180px, 1fr))` — maakt automatisch zoveel kolommen als passen, minimaal 180px breed
- `position: relative` + `position: absolute` op `.checkmark` — plaatst het vinkje rechtsbovenin de kaart
- `user-select: none` — voorkomt dat tekst geselecteerd wordt bij klikken

---

## Stap 7 — Winkelwagen panel

Voeg in de rechterkolom (`.cart-panel`) de winkelwagen toe:

```html
<div class="cart-panel">
  <div class="card">
    <h2>🧾 Winkelwagen</h2>
    <div class="cart-items" id="cartItems">
      <div class="cart-empty">Geen producten geselecteerd.</div>
    </div>
    <hr class="divider" />
    <div class="total-row">
      <span>Totaal</span>
      <span class="total-amount" id="totalAmount">€ 0,00</span>
    </div>
  </div>
</div>
```

CSS voor de winkelwagen:

```css
.cart-panel { position: sticky; top: 1.5rem; }

.cart-items { margin-top: 1rem; display: flex; flex-direction: column; gap: .6rem; }

.cart-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: .9rem;
  padding: .5rem .6rem;
  background: #f7f7ff;
  border-radius: 8px;
}

.cart-line .line-name { font-weight: 500; }
.cart-line .line-total { font-weight: 700; color: #6c63ff; }

.cart-empty { text-align: center; color: #a0aec0; padding: 1.5rem 0; font-size: .9rem; }

.divider { border: none; border-top: 2px solid #e2e8f0; margin: 1rem 0; }

.total-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.15rem;
  font-weight: 700;
}

.total-amount { color: #6c63ff; font-size: 1.35rem; }
```

### Uitleg

- `position: sticky; top: 1.5rem` — de winkelwagen blijft zichtbaar als je door de catalogus scrolt

---

## Stap 8 — Klantgegevens formulier

Voeg het klantformulier en de bestelknop toe **in** de winkelwagen kaart, onder de totaalrij:

```html
<hr class="divider" />
<h2 style="margin-bottom:.8rem">👤 Jouw gegevens</h2>
<div class="customer-form">
  <div class="form-field">
    <label for="klantNaam">Naam</label>
    <input type="text" id="klantNaam" placeholder="Jouw naam…" maxlength="60" />
  </div>
  <div class="form-field">
    <label for="klantTel">Telefoonnummer</label>
    <input type="tel" id="klantTel" placeholder="06-12345678" maxlength="20" />
  </div>
  <div class="form-field">
    <label for="klantVekil">Vekil <span style="color:#a0aec0; font-weight:400;">(optioneel)</span></label>
    <input type="text" id="klantVekil" placeholder="Naam vekil… (optioneel)" maxlength="60" />
  </div>
</div>

<button class="btn-checkout" id="checkoutBtn" disabled onclick="checkout()">
  Bestelling plaatsen
</button>
```

CSS:

```css
.customer-form { display: flex; flex-direction: column; gap: .7rem; margin-bottom: 1rem; }

.form-field { display: flex; flex-direction: column; gap: .3rem; }

.form-field label { font-size: .8rem; font-weight: 600; color: #4a5568; }

.form-field input {
  padding: .6rem .9rem;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  font-size: .9rem;
  outline: none;
  transition: border-color .2s;
}

.form-field input:focus { border-color: #6c63ff; }
.form-field input.error { border-color: #e53e3e; }

.btn-checkout {
  width: 100%;
  margin-top: 1.2rem;
  padding: .9rem;
  background: linear-gradient(135deg, #6c63ff, #574fd6);
  color: white;
  font-size: 1rem;
  font-weight: 700;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(108,99,255,.4);
  transition: transform .1s, box-shadow .2s;
}

.btn-checkout:hover { box-shadow: 0 6px 20px rgba(108,99,255,.5); }
.btn-checkout:active { transform: scale(.98); }
.btn-checkout:disabled { opacity: .5; cursor: not-allowed; }
```

### Uitleg

- `disabled` attribuut op de knop — de knop is uitgeschakeld totdat er producten in de winkelwagen zitten
- `.error` klasse — wordt via JavaScript toegevoegd als validatie mislukt, kleurt de rand rood

---

## Stap 9 — Toast melding

Voeg vlak voor de sluit-tag van `<body>` een toast element toe:

```html
<div class="toast" id="toast"></div>
```

CSS:

```css
.toast {
  position: fixed;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%) translateY(80px);
  background: #1a1a2e;
  color: white;
  padding: .75rem 1.5rem;
  border-radius: 999px;
  font-size: .9rem;
  font-weight: 500;
  opacity: 0;
  transition: transform .3s ease, opacity .3s ease;
  pointer-events: none;
  z-index: 999;
}

.toast.show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
}
```

### Uitleg

- `position: fixed` — zweeft over de pagina, onafhankelijk van de scroll-positie
- `translateY(80px)` — de toast start 80px onderaan de viewport, buiten beeld
- `.toast.show` — schuift de toast omhoog en maakt hem zichtbaar
- `pointer-events: none` — de toast blokkeert geen klikken op de pagina erachter

---

## Stap 10 — JavaScript: data en hulpfuncties

Voeg een `<script>` tag toe vlak voor `</body>`. Begin met de data en hulpfuncties:

```javascript
const products = [
  { id: 1, name: 'Eten',   icon: '🍽️', qty: 0, price: 1 },
  { id: 2, name: 'Sadaka', icon: '🤲', qty: 0, price: 2 },
  { id: 3, name: 'Zekat',  icon: '💝', qty: 0, price: 3 },
];

let nextId = 4;
const icons = ['📦','🎁','🛍️','🔧','🖨️','📱','🎧','💡','🖱️','📷'];

function randomIcon() {
  return icons[Math.floor(Math.random() * icons.length)];
}

function escHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

let toastTimer;
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 2800);
}
```

### Uitleg

- `PRICE = 1` — prijs per stuk, gemakkelijk aan te passen
- `qty: 0` — elke product start op 0 stuks
- `escHtml()` — **beveiligingsfunctie**: voorkomt XSS door gebruikersinvoer te escapen voor het in de HTML wordt gezet. Gebruik dit altijd bij het renderen van gebruikersinvoer.
- `showToast()` — toont een bericht en verbergt het na 2,8 seconden

---

## Stap 11 — JavaScript: product toevoegen

```javascript
function addProduct() {
  const input = document.getElementById('productInput');
  const name = input.value.trim();

  if (!name) {
    showToast('Vul een productnaam in.');
    return;
  }

  if (products.find(p => p.name.toLowerCase() === name.toLowerCase())) {
    showToast('Dit product bestaat al.');
    return;
  }

  products.push({ id: nextId++, name, icon: randomIcon(), qty: 0, price: 1 });
  input.value = '';
  renderGrid();
  showToast(`"${name}" toegevoegd!`);
}

function changeQty(id, delta) {
  const p = products.find(p => p.id === id);
  if (!p) return;
  p.qty = Math.max(0, p.qty + delta);
  renderGrid();
  renderCart();
}
```

Voeg ook de Enter-toets ondersteuning toe, **na** de `renderGrid()` en `renderCart()` aanroepen onderaan:

```javascript
document.getElementById('productInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') addProduct();
});
```

### Uitleg

- `input.value.trim()` — verwijdert witruimte aan het begin en einde
- `toLowerCase()` vergelijking — voorkomt duplicaten ongeacht hoofdlettergebruik
- `Math.max(0, p.qty + delta)` — hoeveelheid mag nooit negatief worden

---

## Stap 12 — JavaScript: grid renderen

```javascript
function renderGrid() {
  const grid = document.getElementById('productGrid');
  document.getElementById('productCount').textContent = `(${products.length})`;

  if (products.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        <span class="empty-icon">📭</span>
        Voeg je eerste product toe via het formulier hierboven.
      </div>`;
    return;
  }

  grid.innerHTML = products.map(p => `
    <div class="product-item ${p.qty > 0 ? 'selected' : ''}" onclick="changeQty(${p.id}, 1)">
      <span class="checkmark">✅</span>
      <span class="product-icon">${p.icon}</span>
      <span class="product-name">${escHtml(p.name)}</span>
        <span class="product-price">€ ${p.price.toLocaleString('nl-NL', {minimumFractionDigits:2})},- / stuk</span>
      <div class="qty-controls" onclick="event.stopPropagation()">
        <button class="qty-btn" onclick="changeQty(${p.id}, -1)">−</button>
        <span class="qty-value">${p.qty}</span>
        <button class="qty-btn" onclick="changeQty(${p.id}, 1)">+</button>
      </div>
    </div>
  `).join('');
}
```

### Uitleg

- `.map(...).join('')` — zet een array om naar één stuk HTML
- `p.qty > 0 ? 'selected' : ''` — voegt de `selected` klasse toe als er stuks gekozen zijn
- `event.stopPropagation()` op de qty-controls — voorkomt dat een klik op +/− ook de kaart-klik triggert (die ook +1 doet)
- `escHtml(p.name)` — essentieel voor beveiliging, zie Stap 10

---

## Stap 13 — JavaScript: winkelwagen renderen

```javascript
function renderCart() {
  const selected = products.filter(p => p.qty > 0);
  const cartDiv = document.getElementById('cartItems');
  const totalEl = document.getElementById('totalAmount');
  const checkoutBtn = document.getElementById('checkoutBtn');

  if (selected.length === 0) {
    cartDiv.innerHTML = `<div class="cart-empty">Geen producten geselecteerd.</div>`;
    totalEl.textContent = '€ 0,00';
    checkoutBtn.disabled = true;
    return;
  }

  const total = selected.reduce((sum, p) => sum + p.qty * p.price, 0);

  cartDiv.innerHTML = selected.map(p => `
    <div class="cart-line">
      <span class="line-name">${escHtml(p.icon)} ${escHtml(p.name)} × ${p.qty}</span>
      <span class="line-total">€ ${(p.qty * p.price).toLocaleString('nl-NL')},00</span>
    </div>
  `).join('');

  totalEl.textContent = `€ ${total.toLocaleString('nl-NL')},00`;
  checkoutBtn.disabled = false;
}
```

### Uitleg

- `filter(p => p.qty > 0)` — alleen producten met stuks tonen
- `reduce(...)` — berekent het totaalbedrag door alle regels op te tellen
- `checkoutBtn.disabled = false` — activeert de bestelknop zodra er iets in de wagen zit

---

## Stap 14 — JavaScript: checkout

```javascript
function checkout() {
  const naam  = document.getElementById('klantNaam').value.trim();
  const tel   = document.getElementById('klantTel').value.trim();
  const vekil = document.getElementById('klantVekil').value.trim();

  // Validatie
  let valid = true;
  document.getElementById('klantNaam').classList.remove('error');
  document.getElementById('klantTel').classList.remove('error');

  if (!naam) { document.getElementById('klantNaam').classList.add('error'); valid = false; }
  if (!tel)  { document.getElementById('klantTel').classList.add('error');  valid = false; }
  if (!valid) { showToast('Vul je naam en telefoonnummer in.'); return; }

  // Betalingslink opbouwen
  const selected = products.filter(p => p.qty > 0);
  const total = selected.reduce((sum, p) => sum + p.qty * p.price, 0);
  const productList = selected.map(p => `${p.qty}x${p.name}`).join('-');
  const vekilDeel = vekil ? `-Vekil-${vekil}` : '-Vekil-FARKETMEZ';
  const description = `${naam}-${tel}${vekilDeel}-${productList}`;
  const bunqUrl = `https://bunq.me/GEVENDEHAND/${total}/${encodeURIComponent(description).replace(/%20/g, '+').replace(/%2C/g, ',')}`;

  // Reset
  products.forEach(p => p.qty = 0);
  document.getElementById('klantNaam').value = '';
  document.getElementById('klantTel').value = '';
  document.getElementById('klantVekil').value = '';
  renderGrid();
  renderCart();

  window.open(bunqUrl, '_blank');
}
```

### Uitleg

- Valideer eerst, verwerk daarna — toon foutmeldingen voor verwerking begint
- `encodeURIComponent(description)` — maakt de tekst URL-veilig
- Na afloop wordt alles gereset: hoeveelheden op 0, formulier leeg
- `window.open(..., '_blank')` — opent de betalingslink in een nieuw tabblad

---

## Eindresultaat overzicht

De volledige structuur van `index.html`:

```
index.html
├── <head>
│   ├── meta charset, viewport, title
│   └── <style>
│       ├── CSS reset + body
│       ├── header
│       ├── .container (grid layout)
│       ├── .card
│       ├── .add-form + .btn
│       ├── .product-grid + .product-item
│       ├── .qty-controls + .qty-btn
│       ├── .cart-panel + .cart-line
│       ├── .customer-form + .form-field
│       ├── .btn-checkout
│       └── .toast
└── <body>
    ├── <header>
    ├── <div class="container">
    │   ├── Linkerkolom: .card met formulier + productgrid
    │   └── Rechterkolom: .cart-panel met winkelwagen + klantformulier
    ├── <div class="toast">
    └── <script>
        ├── Data: products[], PRICE, icons[]
        ├── randomIcon(), escHtml(), showToast()
        ├── addProduct()
        ├── changeQty()
        ├── renderGrid()
        ├── renderCart()
        ├── checkout()
        ├── keydown listener (Enter)
        └── renderGrid() + renderCart()  ← initiële render
```

### Aandachtspunten

| Onderwerp | Tip |
|-----------|-----|
| Beveiliging | Gebruik altijd `escHtml()` bij het renderen van gebruikersinvoer in innerHTML |
| Toegankelijkheid | Gebruik `<label for="...">` gekoppeld aan `id` op het input |
| Mobiel | Test de layout op een smal scherm, de `@media` query stapelt de kolommen |
| Uitbreiden | Voeg een `price` invoerveld toe aan het formulier om ook de prijs van nieuwe producten in te stellen |
