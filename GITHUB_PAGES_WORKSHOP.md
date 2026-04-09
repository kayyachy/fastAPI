# 🌐 GitHub Pages Workshop — Statische webpagina deployen

> **Doel:** Een HTML-webpagina aanmaken en gratis hosten via GitHub Pages.

---

## 📌 Inhoudsopgave

1. [Wat is GitHub Pages?](#1-wat-is-github-pages)
2. [Vereisten](#2-vereisten)
3. [Stap 1 — Projectmap aanmaken](#3-stap-1--projectmap-aanmaken)
4. [Stap 2 — HTML-bestand aanmaken](#4-stap-2--html-bestand-aanmaken)
5. [Stap 3 — Git repository initialiseren](#5-stap-3--git-repository-initialiseren)
6. [Stap 4 — Pushen naar GitHub](#6-stap-4--pushen-naar-github)
7. [Stap 5 — GitHub Pages activeren](#7-stap-5--github-pages-activeren)
8. [Stap 6 — Wijzigingen deployen](#8-stap-6--wijzigingen-deployen)
9. [Projectstructuur](#9-projectstructuur)
10. [Veelgestelde vragen](#10-veelgestelde-vragen)

---

## 1. Wat is GitHub Pages?

GitHub Pages is een **gratis hostingservice van GitHub** waarmee je statische websites (HTML, CSS, JavaScript) publiceert rechtstreeks vanuit een repository.

| Eigenschap | Details |
|---|---|
| Kosten | Gratis |
| URL formaat | `https://<gebruikersnaam>.github.io/<repository>/` |
| Ondersteunde bestanden | HTML, CSS, JavaScript, afbeeldingen |
| Vereiste | Publieke GitHub repository |

---

## 2. Vereisten

- Een [GitHub account](https://github.com)
- [Git](https://git-scm.com/downloads) geïnstalleerd
- Een teksteditor (bijv. VS Code)

Controleer of Git geïnstalleerd is:

```bash
git --version
```

---

## 3. Stap 1 — Projectmap aanmaken

Maak een map `docs/` aan in je project. GitHub Pages leest standaard uit deze map.

```bash
mkdir docs
```

---

## 4. Stap 2 — HTML-bestand aanmaken

Maak het bestand `docs/index.html` aan. Dit is de startpagina die GitHub Pages toont.

**Minimaal voorbeeld:**

```html
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Mijn Pagina</title>
</head>
<body>
  <h1>Hallo wereld!</h1>
  <p>Dit is mijn GitHub Pages website.</p>
</body>
</html>
```

Sla het op als `docs/index.html`.

> ✅ De bestandsnaam **moet** `index.html` zijn — dit is de standaard startpagina.

---

## 5. Stap 3 — Git repository initialiseren

### Nieuw project (nog geen Git):

```bash
cd jouw-projectmap
git init
git add .
git commit -m "eerste commit"
```

### Bestaand project (al Git aanwezig):

Sla stap 1 t/m 3 over en ga direct naar stap 4.

---

## 6. Stap 4 — Pushen naar GitHub

### Repository aanmaken op GitHub:

1. Ga naar [github.com/new](https://github.com/new)
2. Geef de repository een naam (bijv. `mijn-website`)
3. Kies **Public**
4. Klik **Create repository**

### Code pushen:

```bash
git remote add origin https://github.com/<jouw-gebruikersnaam>/<repository-naam>.git
git branch -M main
git push -u origin main
```

**Of als de remote al bestaat:**

```bash
git add docs/
git commit -m "feat: webpagina toegevoegd"
git push
```

---

## 7. Stap 5 — GitHub Pages activeren

1. Ga naar je repository op GitHub
2. Klik op **Settings** (tandwiel-icoon)
3. Scroll naar **Pages** in het linker menu
4. Stel in bij **Source**:
   - Branch: `main` (of jouw branch naam)
   - Map: `/docs`
5. Klik **Save**

Na ~1 minuut is je pagina live op:

```
https://<jouw-gebruikersnaam>.github.io/<repository-naam>/
```

> ⚠️ **Let op:** De repository moet **Public** zijn voor gratis GitHub Pages.

---

## 8. Stap 6 — Wijzigingen deployen

Elke keer als je wijzigingen pusht naar de geconfigureerde branch, deployt GitHub Pages **automatisch**.

```bash
# Bestand aanpassen, dan:
git add docs/index.html
git commit -m "update: pagina bijgewerkt"
git push
```

Wacht ~1-2 minuten en ververs de pagina.

### Harde refresh (cache wissen):

| Systeem | Sneltoets |
|---|---|
| Windows | `Ctrl + Shift + R` |
| Mac | `Cmd + Shift + R` |

---

## 9. Projectstructuur

```
jouw-project/
├── docs/                  ← GitHub Pages leest hieruit
│   ├── index.html         ← Startpagina (verplicht)
│   └── _config.yml        ← Optionele Jekyll configuratie
├── README.md
└── ...overige bestanden
```

### Optioneel — `docs/_config.yml`:

```yaml
title: Mijn Website
description: Korte beschrijving van de pagina.
```

---

## 10. Veelgestelde vragen

**Q: Mijn pagina laadt nog de oude versie.**  
A: Doe een harde refresh: `Ctrl + Shift + R` (Windows) of `Cmd + Shift + R` (Mac).

**Q: Ik zie een 404-fout.**  
A: Controleer of het bestand exact `docs/index.html` heet en of GitHub Pages is geactiveerd in Settings → Pages.

**Q: Hoe lang duurt het voordat de pagina live is?**  
A: Meestal 1–2 minuten na elke push.

**Q: Kan ik meerdere pagina's maken?**  
A: Ja, maak extra HTML-bestanden in de `docs/` map, bijv. `docs/contact.html`. Bereikbaar via `.../contact.html`.

**Q: Hoe vind ik mijn URL?**  
A: Ga naar Settings → Pages. De URL staat bovenaan de pagina.

---

## 🎉 Gefeliciteerd!

Je website is live op GitHub Pages. Elke `git push` zorgt voor een automatische deploy — geen server nodig!

---

## 📦 Gebruikte tools

| Tool | Beschrijving |
|---|---|
| Git | Versiebeheer |
| GitHub | Code platform & hosting |
| GitHub Pages | Gratis statische website hosting |
| HTML/CSS/JS | Webtechnologieën voor de pagina |
