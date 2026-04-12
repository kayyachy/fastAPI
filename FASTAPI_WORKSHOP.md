# 🚀 FastAPI Workshop — Bouw een Personen-API stap voor stap

> **Doel van deze workshop:** Een werkende REST API bouwen met FastAPI en Pydantic, met volledige CRUD-functionaliteit voor een personenlijst. Aan het einde schrijven we ook geautomatiseerde tests.

---

## 📌 Inhoudsopgave

1. [Wat gaan we bouwen?](#1-wat-gaan-we-bouwen)
2. [Vereisten](#2-vereisten)
3. [Project opzetten](#3-project-opzetten)
4. [Stap 1 — Eerste FastAPI app](#stap-1--eerste-fastapi-app)
5. [Stap 2 — Data modellen met Pydantic](#stap-2--data-modellen-met-pydantic)
6. [Stap 3 — In-memory dataset](#stap-3--in-memory-dataset)
7. [Stap 4 — GET alle personen](#stap-4--get-alle-personen)
8. [Stap 5 — GET één persoon op ID](#stap-5--get-één-persoon-op-id)
9. [Stap 6 — POST persoon toevoegen](#stap-6--post-persoon-toevoegen)
10. [Stap 7 — PUT persoon bewerken](#stap-7--put-persoon-bewerken)
11. [Stap 8 — DELETE persoon verwijderen](#stap-8--delete-persoon-verwijderen)
12. [Stap 9 — Tests schrijven](#stap-9--tests-schrijven)
13. [Eindresultaat overzicht](#eindresultaat-overzicht)

---

## 1. Wat gaan we bouwen?

Een REST API met de volgende endpoints:

| Methode | Pad | Beschrijving |
|---------|-----|--------------|
| GET | `/` | Welkomstbericht |
| GET | `/health` | Status check |
| GET | `/personen` | Alle personen ophalen |
| GET | `/personen/{id}` | Één persoon ophalen |
| POST | `/personen` | Persoon toevoegen |
| PUT | `/personen/{id}` | Persoon bewerken |
| DELETE | `/personen/{id}` | Persoon verwijderen |

De data wordt in het geheugen opgeslagen (geen database).

---

## 2. Vereisten

- Python 3.10 of hoger
- pip
- Basiskennis Python

Controleer je Python versie:

```bash
python --version
```

---

## 3. Project opzetten

### Virtual environment aanmaken en activeren

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> **Let op (Windows):** Krijg je een foutmelding over execution policy? Voer dan eerst dit uit:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Packages installeren

```bash
pip install fastapi uvicorn pydantic pytest httpx
```

Of via het meegeleverde bestand:

```bash
pip install -r requirements.txt
```

---

## Stap 1 — Eerste FastAPI app

Maak het bestand `main.py` aan en voeg de basisstructuur toe:

```python
from fastapi import FastAPI

app = FastAPI(title="FastAPI Workshop", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Welkom bij FastAPI Copilte!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
```

### Server starten

```bash
uvicorn main:app --reload
```

De server draait nu op **http://127.0.0.1:8000**

### Testen in de browser

- **Welkomstbericht:** http://127.0.0.1:8000/
- **Health check:** http://127.0.0.1:8000/health
- **Automatische API docs:** http://127.0.0.1:8000/docs

> **Tip:** De `/docs` pagina wordt automatisch gegenereerd door FastAPI. Hier kun je alle endpoints live uitproberen.

---

## Stap 2 — Data modellen met Pydantic

Voeg bovenaan `main.py` de imports en modellen toe:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
```

Voeg daarna de twee modellen toe, **boven** de `app = FastAPI(...)` regel:

```python
class Persoon(BaseModel):
    id: int
    naam: str
    adres: str
    woonplaats: str
    emailadres: str


class PersoonUpdate(BaseModel):
    naam: Optional[str] = None
    adres: Optional[str] = None
    woonplaats: Optional[str] = None
    emailadres: Optional[str] = None
```

### Uitleg

- `Persoon` — het volledige model, alle velden zijn verplicht.
- `PersoonUpdate` — gebruikt voor PUT-requests; alle velden zijn optioneel zodat je een gedeeltelijke update kunt doen.
- `Optional[str] = None` — het veld mag ontbreken in de request body.

---

## Stap 3 — In-memory dataset

Voeg na de modellen een lijst toe als tijdelijke "database":

```python
PERSONEN: List[Persoon] = [
    Persoon(id=1,  naam="Mohammed Al-Rashid", adres="Keizersgracht 12",   woonplaats="Amsterdam",  emailadres="m.alrashid@gmail.com"),
    Persoon(id=2,  naam="Sophie de Vries",    adres="Lange Voorhout 5",   woonplaats="Den Haag",   emailadres="sophie.devries@hotmail.com"),
    Persoon(id=3,  naam="Lars Janssen",       adres="Marktstraat 8",      woonplaats="Utrecht",    emailadres="lars.janssen@outlook.com"),
    # ... voeg meer personen toe
]
```

> **Let op:** In een echte applicatie gebruik je een database zoals PostgreSQL of SQLite. In deze workshop slaan we alles in het geheugen op. Dit betekent dat alle wijzigingen verloren gaan bij het herstarten van de server.

---

## Stap 4 — GET alle personen

Voeg het endpoint toe dat alle personen teruggeeft:

```python
@app.get("/personen", response_model=List[Persoon])
def get_personen():
    return PERSONEN
```

### Testen

Open http://127.0.0.1:8000/personen in je browser of via de `/docs` pagina.

**Verwacht resultaat:**
```json
[
  {
    "id": 1,
    "naam": "Mohammed Al-Rashid",
    "adres": "Keizersgracht 12",
    "woonplaats": "Amsterdam",
    "emailadres": "m.alrashid@gmail.com"
  },
  ...
]
```

---

## Stap 5 — GET één persoon op ID

```python
@app.get("/personen/{persoon_id}", response_model=Persoon)
def get_persoon(persoon_id: int):
    for persoon in PERSONEN:
        if persoon.id == persoon_id:
            return persoon
    raise HTTPException(status_code=404, detail="Persoon niet gevonden")
```

### Uitleg

- `{persoon_id}` in het pad is een **path parameter** — FastAPI converteert dit automatisch naar een `int`.
- Als de persoon niet gevonden wordt, gooien we een `HTTPException` met statuscode `404`.

### Testen

- **Gevonden:** http://127.0.0.1:8000/personen/1 → statuscode `200`
- **Niet gevonden:** http://127.0.0.1:8000/personen/9999 → statuscode `404`

---

## Stap 6 — POST persoon toevoegen

```python
@app.post("/personen", response_model=Persoon, status_code=201)
def voeg_persoon_toe(persoon: Persoon):
    for p in PERSONEN:
        if p.id == persoon.id:
            raise HTTPException(
                status_code=400,
                detail=f"Persoon met id {persoon.id} bestaat al"
            )
    PERSONEN.append(persoon)
    return persoon
```

### Uitleg

- `status_code=201` — bij een succesvolle POST sturen we `201 Created` terug in plaats van `200 OK`.
- We controleren first of het ID al bestaat om duplicaten te voorkomen.

### Testen via `/docs`

Ga naar http://127.0.0.1:8000/docs, klik op `POST /personen` → **Try it out** en stuur:

```json
{
  "id": 51,
  "naam": "Test Persoon",
  "adres": "Teststraat 99",
  "woonplaats": "Teststad",
  "emailadres": "test@test.com"
}
```

---

## Stap 7 — PUT persoon bewerken

```python
@app.put("/personen/{persoon_id}", response_model=Persoon)
def bewerk_persoon(persoon_id: int, update: PersoonUpdate):
    for i, persoon in enumerate(PERSONEN):
        if persoon.id == persoon_id:
            bijgewerkt = persoon.model_copy(update=update.model_dump(exclude_none=True))
            PERSONEN[i] = bijgewerkt
            return bijgewerkt
    raise HTTPException(status_code=404, detail="Persoon niet gevonden")
```

### Uitleg

- `update.model_dump(exclude_none=True)` — converteert het update-model naar een dictionary, maar slaat velden over die `None` zijn (niet meegestuurd).
- `persoon.model_copy(update=...)` — maakt een kopie van de bestaande persoon met de gewijzigde velden.

### Testen via `/docs`

Stuur een `PUT` naar `/personen/1` met alleen het te wijzigen veld:

```json
{
  "naam": "Nieuwe Naam"
}
```

De overige velden (`adres`, `woonplaats`, `emailadres`) blijven ongewijzigd.

---

## Stap 8 — DELETE persoon verwijderen

```python
@app.delete("/personen/{persoon_id}", status_code=200)
def verwijder_persoon(persoon_id: int):
    for i, persoon in enumerate(PERSONEN):
        if persoon.id == persoon_id:
            PERSONEN.pop(i)
            return {"message": f"Persoon met id {persoon_id} is verwijderd"}
    raise HTTPException(status_code=404, detail="Persoon niet gevonden")
```

### Testen via `/docs`

Stuur een `DELETE` naar `/personen/1`. Controleer daarna via `GET /personen/1` of de persoon inderdaad weg is (verwacht: `404`).

---

## Stap 9 — Tests schrijven

Maak het bestand `test_main.py` aan:

```python
import pytest
from fastapi.testclient import TestClient
from main import app, PERSONEN

client = TestClient(app)


@pytest.fixture(autouse=True)
def herstel_personen():
    """Reset de PERSONEN lijst na elke test zodat tests onafhankelijk zijn."""
    origineel = PERSONEN.copy()
    yield
    PERSONEN.clear()
    PERSONEN.extend(origineel)
```

### Tests voor GET /

```python
class TestRoot:
    def test_root_status_200(self):
        response = client.get("/")
        assert response.status_code == 200

    def test_root_bericht(self):
        response = client.get("/")
        assert response.json() == {"message": "Welkom bij FastAPI Copilte!"}
```

### Tests voor GET /personen

```python
class TestGetPersonen:
    def test_geeft_lijst_terug(self):
        response = client.get("/personen")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_eerste_persoon_velden(self):
        response = client.get("/personen")
        persoon = response.json()[0]
        assert "id" in persoon
        assert "naam" in persoon
        assert "emailadres" in persoon
```

### Tests voor POST /personen

```python
class TestPostPersoon:
    NIEUWE_PERSOON = {
        "id": 51,
        "naam": "Test Persoon",
        "adres": "Teststraat 99",
        "woonplaats": "Teststad",
        "emailadres": "test@test.com"
    }

    def test_toevoegen_status_201(self):
        response = client.post("/personen", json=self.NIEUWE_PERSOON)
        assert response.status_code == 201

    def test_duplicate_id_400(self):
        response = client.post("/personen", json={
            "id": 1, "naam": "Kopie", "adres": "Straat 1",
            "woonplaats": "Stad", "emailadres": "kopie@test.com"
        })
        assert response.status_code == 400
```

### Tests uitvoeren

```bash
pytest test_main.py -v
```

**Verwachte output:**
```
test_main.py::TestRoot::test_root_status_200   PASSED
test_main.py::TestRoot::test_root_bericht      PASSED
test_main.py::TestGetPersonen::...             PASSED
...
```

---

## Eindresultaat overzicht

Je `main.py` bevat nu:

```
main.py
├── imports (FastAPI, Pydantic, typing)
├── app = FastAPI(...)
├── class Persoon(BaseModel)
├── class PersoonUpdate(BaseModel)
├── PERSONEN: List[Persoon] = [...]
├── GET  /                        → root()
├── GET  /health                  → health_check()
├── GET  /personen                → get_personen()
├── GET  /personen/{id}           → get_persoon()
├── POST /personen                → voeg_persoon_toe()
├── PUT  /personen/{id}           → bewerk_persoon()
└── DELETE /personen/{id}         → verwijder_persoon()
```

### Handige links tijdens de workshop

| Link | Beschrijving |
|------|--------------|
| http://127.0.0.1:8000/docs | Swagger UI — interactieve API docs |
| http://127.0.0.1:8000/redoc | ReDoc — alternatieve API docs |
| http://127.0.0.1:8000/openapi.json | Ruwe OpenAPI specificatie |

### Vervolgstappen

- Koppel een echte database met **SQLAlchemy** of **SQLModel**
- Voeg authenticatie toe met **OAuth2 / JWT**
- Schrijf meer tests voor edge cases
- Bekijk de Django workshop: [DJANGO_WORKSHOP.md](DJANGO_WORKSHOP.md)
