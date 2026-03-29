# FastAPI Copilte

Een eenvoudige FastAPI applicatie met een dummy personentabel van 50 records.

---

## 📋 Vereisten

- Python 3.10+
- pip

---

## 🚀 Installatie & Opstarten

### 1. Clone of open het project

```bash
cd fastapi_copilte
```

### 2. Maak een virtual environment aan en activeer het

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> **Let op (Windows):** Als je een foutmelding krijgt over execution policy, voer dan eerst dit uit:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 3. Installeer de vereiste packages

```bash
pip install -r requirements.txt
```

### 4. Start de server

```bash
uvicorn main:app --reload
```

De server draait nu op **http://127.0.0.1:8000**

---

## 📡 Endpoints

| Method | URL | Beschrijving |
|--------|-----|--------------|
| `GET` | `/` | Welkomstbericht |
| `GET` | `/health` | Health check |
| `GET` | `/personen` | Alle 50 personen ophalen |
| `GET` | `/personen/{id}` | Één persoon ophalen op ID (1–50) |

---

## 📄 Datamodel

Elke persoon heeft de volgende velden:

| Veld | Type | Beschrijving |
|------|------|--------------|
| `id` | int | Uniek ID |
| `naam` | str | Volledige naam |
| `adres` | str | Straatnaam en huisnummer |
| `woonplaats` | str | Stad of gemeente |
| `emailadres` | str | E-mailadres |

---

## 📚 API Documentatie

FastAPI genereert automatisch interactieve documentatie:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## 🗂️ Projectstructuur

```
fastapi_copilte/
├── .venv/              # Virtual environment
├── main.py             # Hoofdapplicatie
├── requirements.txt    # Afhankelijkheden
└── README.md           # Projectdocumentatie
```

---

## 📦 Gebruikte packages

| Package | Versie |
|---------|--------|
| fastapi | 0.135.2 |
| uvicorn | 0.42.0 |
| pydantic | 2.12.5 |
| python-dotenv | 1.2.2 |
