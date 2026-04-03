# 🐍 Django Workshop — Van FastAPI naar Django REST Framework

> **Doel van deze workshop:** Dezelfde Personen-API die we kennen van FastAPI, opnieuw bouwen met Django en Django REST Framework (DRF).

---

## 📌 Inhoudsopgave

1. [Vergelijking: FastAPI vs Django](#1-vergelijking-fastapi-vs-django)
2. [Vereisten](#2-vereisten)
3. [Installatie](#3-installatie)
4. [Django project aanmaken](#4-django-project-aanmaken)
5. [App aanmaken](#5-app-aanmaken)
6. [Model definiëren](#6-model-definiëren)
7. [Database migraties uitvoeren](#7-database-migraties-uitvoeren)
8. [Serializer aanmaken](#8-serializer-aanmaken)
9. [Views (endpoints) aanmaken](#9-views-endpoints-aanmaken)
10. [URL routing instellen](#10-url-routing-instellen)
11. [Startdata laden (fixtures)](#11-startdata-laden-fixtures)
12. [Server starten & testen](#12-server-starten--testen)
13. [Admin panel](#13-admin-panel)
14. [Overzicht: FastAPI vs Django vergelijking](#14-overzicht-fastapi-vs-django-vergelijking)
15. [Projectstructuur](#15-projectstructuur)

---

## 1. Vergelijking: FastAPI vs Django

| Eigenschap | FastAPI | Django + DRF |
|---|---|---|
| Type | Micro-framework (alleen API) | Full-stack framework |
| Database | Handmatig (in-memory, SQLAlchemy, etc.) | Ingebouwde ORM |
| Admin panel | ❌ Niet aanwezig | ✅ Gratis ingebouwd |
| Validatie | Pydantic modellen | Serializers |
| Automatische docs | Swagger via `/docs` | Browsable API via DRF |
| Snelheid opzetten | Zeer snel | Iets meer configuratie |
| Geschikt voor | Kleine, snelle API's | Grotere applicaties |

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

## 3. Installatie

### Stap 1: Maak een nieuwe projectmap aan

```bash
mkdir django_personen
cd django_personen
```

### Stap 2: Maak een virtual environment aan en activeer het

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> ⚠️ **Fout bij activeren op Windows?** Voer dit eerst uit:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**macOS / Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### Stap 3: Installeer de benodigde packages

```bash
pip install django djangorestframework
```

Maak daarna een `requirements.txt` aan:

```bash
pip freeze > requirements.txt
```

---

## 4. Django project aanmaken

```bash
django-admin startproject personen_project .
```

> ✅ De punt (`.`) zorgt ervoor dat de bestanden in de huidige map worden aangemaakt.

Je hebt nu de volgende structuur:

```
django_personen/
├── manage.py
└── personen_project/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### DRF toevoegen aan `settings.py`

Open `personen_project/settings.py` en voeg `rest_framework` toe aan `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',   # ← VOEG DIT TOE
]
```

---

## 5. App aanmaken

In Django splits je functionaliteit op in **apps**. Maak een app aan voor personen:

```bash
python manage.py startapp personen
```

Voeg de nieuwe app toe aan `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'personen',   # ← VOEG DIT TOE
]
```

---

## 6. Model definiëren

Open `personen/models.py` en definieer het `Persoon` model.  
Dit is de Django-equivalent van de Pydantic `BaseModel` in FastAPI:

**FastAPI (oud):**
```python
class Persoon(BaseModel):
    id: int
    naam: str
    adres: str
    woonplaats: str
    emailadres: str
```

**Django (nieuw) — `personen/models.py`:**
```python
from django.db import models


class Persoon(models.Model):
    naam = models.CharField(max_length=100)
    adres = models.CharField(max_length=200)
    woonplaats = models.CharField(max_length=100)
    emailadres = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.naam} ({self.woonplaats})"
```

> 💡 Django beheert het `id` veld automatisch als primaire sleutel — je hoeft het niet zelf toe te voegen.

---

## 7. Database migraties uitvoeren

Django gebruikt migraties om de database up-to-date te houden met je modellen.

### Migratie aanmaken:

```bash
python manage.py makemigrations
```

### Migratie toepassen:

```bash
python manage.py migrate
```

> ✅ Django gebruikt standaard SQLite (`db.sqlite3`). Geen extra configuratie nodig.

---

## 8. Serializer aanmaken

Een **serializer** in DRF doet hetzelfde als een Pydantic model in FastAPI: het valideert data en zet het om van/naar JSON.

Maak het bestand `personen/serializers.py` aan:

```python
from rest_framework import serializers
from .models import Persoon


class PersoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persoon
        fields = ['id', 'naam', 'adres', 'woonplaats', 'emailadres']
```

---

## 9. Views (endpoints) aanmaken

Open `personen/views.py` en maak de API views aan met DRF's `viewsets`:

```python
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Persoon
from .serializers import PersoonSerializer


@api_view(['GET'])
def root(request):
    return Response({"message": "Welkom bij de Django Personen API!"})


@api_view(['GET'])
def health_check(request):
    return Response({"status": "ok"})


class PersoonViewSet(viewsets.ModelViewSet):
    queryset = Persoon.objects.all()
    serializer_class = PersoonSerializer
```

### Vergelijking met FastAPI:

| FastAPI endpoint | Django equivalent |
|---|---|
| `@app.get("/personen")` | `PersoonViewSet` → `list()` |
| `@app.get("/personen/{id}")` | `PersoonViewSet` → `retrieve()` |
| `@app.post("/personen")` | `PersoonViewSet` → `create()` |
| `@app.put("/personen/{id}")` | `PersoonViewSet` → `update()` |
| `@app.delete("/personen/{id}")` | `PersoonViewSet` → `destroy()` |

> 💡 Met een `ModelViewSet` krijg je **alle CRUD-operaties gratis** — geen aparte functies nodig!

---

## 10. URL routing instellen

### `personen/urls.py` aanmaken (nieuw bestand):

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'personen', views.PersoonViewSet)

urlpatterns = [
    path('', views.root),
    path('health/', views.health_check),
    path('', include(router.urls)),
]
```

### `personen_project/urls.py` aanpassen:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personen.urls')),
]
```

---

## 11. Startdata laden (fixtures)

In FastAPI hadden we een hardcoded lijst van 50 personen. In Django laden we dit via een **fixture**.

Maak de map aan:

```bash
mkdir -p personen/fixtures
```

Maak het bestand `personen/fixtures/personen.json` aan met de startdata:

```json
[
  {"model": "personen.persoon", "pk": 1,  "fields": {"naam": "Mohammed Al-Rashid",  "adres": "Keizersgracht 12",      "woonplaats": "Amsterdam",   "emailadres": "m.alrashid@gmail.com"}},
  {"model": "personen.persoon", "pk": 2,  "fields": {"naam": "Sophie de Vries",      "adres": "Lange Voorhout 5",      "woonplaats": "Den Haag",    "emailadres": "sophie.devries@hotmail.com"}},
  {"model": "personen.persoon", "pk": 3,  "fields": {"naam": "Lars Janssen",         "adres": "Marktstraat 8",         "woonplaats": "Utrecht",     "emailadres": "lars.janssen@outlook.com"}},
  {"model": "personen.persoon", "pk": 4,  "fields": {"naam": "Fatima El Ouali",      "adres": "Bergweg 33",            "woonplaats": "Rotterdam",   "emailadres": "f.elouali@gmail.com"}},
  {"model": "personen.persoon", "pk": 5,  "fields": {"naam": "Tim van den Berg",     "adres": "Dorpsstraat 17",        "woonplaats": "Eindhoven",   "emailadres": "tim.vandenberg@live.nl"}},
  {"model": "personen.persoon", "pk": 6,  "fields": {"naam": "Emma Bakker",          "adres": "Hoofdstraat 45",        "woonplaats": "Groningen",   "emailadres": "emma.bakker@gmail.com"}},
  {"model": "personen.persoon", "pk": 7,  "fields": {"naam": "Yusuf Özdemir",        "adres": "Stationsplein 2",       "woonplaats": "Tilburg",     "emailadres": "y.ozdemir@yahoo.com"}},
  {"model": "personen.persoon", "pk": 8,  "fields": {"naam": "Nora Visser",          "adres": "Parkweg 19",            "woonplaats": "Almere",      "emailadres": "nora.visser@hotmail.com"}},
  {"model": "personen.persoon", "pk": 9,  "fields": {"naam": "Daan Smit",            "adres": "Kerkstraat 7",          "woonplaats": "Breda",       "emailadres": "daan.smit@gmail.com"}},
  {"model": "personen.persoon", "pk": 10, "fields": {"naam": "Lena Mulder",          "adres": "Schoollaan 28",         "woonplaats": "Nijmegen",    "emailadres": "lena.mulder@outlook.com"}},
  {"model": "personen.persoon", "pk": 11, "fields": {"naam": "Ahmed Benali",         "adres": "Tulpstraat 3",          "woonplaats": "Haarlem",     "emailadres": "ahmed.benali@gmail.com"}},
  {"model": "personen.persoon", "pk": 12, "fields": {"naam": "Julia Meijer",         "adres": "Rozenlaan 14",          "woonplaats": "Arnhem",      "emailadres": "julia.meijer@live.nl"}},
  {"model": "personen.persoon", "pk": 13, "fields": {"naam": "Sander Boer",          "adres": "Industrieweg 55",       "woonplaats": "Enschede",    "emailadres": "sander.boer@hotmail.com"}},
  {"model": "personen.persoon", "pk": 14, "fields": {"naam": "Yasmine Khalil",       "adres": "Vondelstraat 9",        "woonplaats": "Zwolle",      "emailadres": "y.khalil@gmail.com"}},
  {"model": "personen.persoon", "pk": 15, "fields": {"naam": "Pieter de Jong",       "adres": "Nieuwstraat 22",        "woonplaats": "Apeldoorn",   "emailadres": "pieter.dejong@outlook.com"}},
  {"model": "personen.persoon", "pk": 16, "fields": {"naam": "Sara Linders",         "adres": "Julianaweg 37",         "woonplaats": "Maastricht",  "emailadres": "sara.linders@gmail.com"}},
  {"model": "personen.persoon", "pk": 17, "fields": {"naam": "Kevin Willems",        "adres": "Beatrixlaan 6",         "woonplaats": "Leiden",      "emailadres": "kevin.willems@yahoo.com"}},
  {"model": "personen.persoon", "pk": 18, "fields": {"naam": "Amira Tahir",          "adres": "Koningstraat 50",       "woonplaats": "Dordrecht",   "emailadres": "amira.tahir@hotmail.com"}},
  {"model": "personen.persoon", "pk": 19, "fields": {"naam": "Roos van Dijk",        "adres": "Willemstraat 11",       "woonplaats": "Zoetermeer",  "emailadres": "roos.vandijk@gmail.com"}},
  {"model": "personen.persoon", "pk": 20, "fields": {"naam": "Niels Hermans",        "adres": "Prins Hendrikstraat 4", "woonplaats": "Deventer",    "emailadres": "niels.hermans@live.nl"}},
  {"model": "personen.persoon", "pk": 21, "fields": {"naam": "Bilal Chaoui",         "adres": "Vossenlaan 16",         "woonplaats": "Delft",       "emailadres": "bilal.chaoui@gmail.com"}},
  {"model": "personen.persoon", "pk": 22, "fields": {"naam": "Merel Kok",            "adres": "Zonnebloemstraat 25",   "woonplaats": "Alkmaar",     "emailadres": "merel.kok@outlook.com"}},
  {"model": "personen.persoon", "pk": 23, "fields": {"naam": "Joost Hendriks",       "adres": "Havenstraat 38",        "woonplaats": "Amersfoort",  "emailadres": "joost.hendriks@hotmail.com"}},
  {"model": "personen.persoon", "pk": 24, "fields": {"naam": "Leila Nasser",         "adres": "Boslaan 21",            "woonplaats": "Venlo",       "emailadres": "leila.nasser@gmail.com"}},
  {"model": "personen.persoon", "pk": 25, "fields": {"naam": "Bram Peters",          "adres": "Rembrandtstraat 44",    "woonplaats": "Helmond",     "emailadres": "bram.peters@yahoo.com"}},
  {"model": "personen.persoon", "pk": 26, "fields": {"naam": "Iris Vermeer",         "adres": "Mozartlaan 10",         "woonplaats": "Leeuwarden",  "emailadres": "iris.vermeer@gmail.com"}},
  {"model": "personen.persoon", "pk": 27, "fields": {"naam": "Omar Idrissi",         "adres": "Spinozaweg 29",         "woonplaats": "Zaandam",     "emailadres": "omar.idrissi@hotmail.com"}},
  {"model": "personen.persoon", "pk": 28, "fields": {"naam": "Fleur Timmermans",     "adres": "Wilhelminalaan 3",      "woonplaats": "Ede",         "emailadres": "fleur.timmermans@outlook.com"}},
  {"model": "personen.persoon", "pk": 29, "fields": {"naam": "Tom van Leeuwen",      "adres": "Erasmusstraat 18",      "woonplaats": "Hilversum",   "emailadres": "tom.vanleeuwen@live.nl"}},
  {"model": "personen.persoon", "pk": 30, "fields": {"naam": "Nadia Hamid",          "adres": "Sophiastraat 41",       "woonplaats": "Roosendaal",  "emailadres": "nadia.hamid@gmail.com"}},
  {"model": "personen.persoon", "pk": 31, "fields": {"naam": "Rick Kuijpers",        "adres": "Tramweg 13",            "woonplaats": "Spijkenisse", "emailadres": "rick.kuijpers@hotmail.com"}},
  {"model": "personen.persoon", "pk": 32, "fields": {"naam": "Mila Schouten",        "adres": "Chopinplein 7",         "woonplaats": "Emmen",       "emailadres": "mila.schouten@gmail.com"}},
  {"model": "personen.persoon", "pk": 33, "fields": {"naam": "Karim Aouad",          "adres": "Lindelaan 30",          "woonplaats": "Capelle a/d IJssel", "emailadres": "karim.aouad@yahoo.com"}},
  {"model": "personen.persoon", "pk": 34, "fields": {"naam": "Denise van Rooij",     "adres": "Kastanjelaan 53",       "woonplaats": "Heerlen",     "emailadres": "denise.vanrooij@outlook.com"}},
  {"model": "personen.persoon", "pk": 35, "fields": {"naam": "Mark Peeters",         "adres": "Schipholweg 26",        "woonplaats": "Sittard",     "emailadres": "mark.peeters@gmail.com"}},
  {"model": "personen.persoon", "pk": 36, "fields": {"naam": "Hana Berrada",         "adres": "Populierenlaan 15",     "woonplaats": "Gouda",       "emailadres": "hana.berrada@hotmail.com"}},
  {"model": "personen.persoon", "pk": 37, "fields": {"naam": "Stefan Dekker",        "adres": "Iepenlaan 48",          "woonplaats": "Purmerend",   "emailadres": "stefan.dekker@live.nl"}},
  {"model": "personen.persoon", "pk": 38, "fields": {"naam": "Lotte Huisman",        "adres": "Beukenweg 36",          "woonplaats": "Hoorn",       "emailadres": "lotte.huisman@gmail.com"}},
  {"model": "personen.persoon", "pk": 39, "fields": {"naam": "Anouar El Habti",      "adres": "Dennenlaan 9",          "woonplaats": "Alphen a/d Rijn", "emailadres": "anouar.elhabti@outlook.com"}},
  {"model": "personen.persoon", "pk": 40, "fields": {"naam": "Charlotte Engel",      "adres": "Magnoliapad 20",        "woonplaats": "Lelystad",    "emailadres": "charlotte.engel@hotmail.com"}},
  {"model": "personen.persoon", "pk": 41, "fields": {"naam": "Jesse van Beek",       "adres": "Veluwelaan 34",         "woonplaats": "Harderwijk",  "emailadres": "jesse.vanbeek@gmail.com"}},
  {"model": "personen.persoon", "pk": 42, "fields": {"naam": "Samira Ouali",         "adres": "Hertogstraat 5",        "woonplaats": "Bergen op Zoom", "emailadres": "samira.ouali@yahoo.com"}},
  {"model": "personen.persoon", "pk": 43, "fields": {"naam": "Wouter Groot",         "adres": "Lübeckstraat 27",       "woonplaats": "Nieuwegein",  "emailadres": "wouter.groot@outlook.com"}},
  {"model": "personen.persoon", "pk": 44, "fields": {"naam": "Eva Brouwer",          "adres": "Azalealaan 43",         "woonplaats": "Weert",       "emailadres": "eva.brouwer@gmail.com"}},
  {"model": "personen.persoon", "pk": 45, "fields": {"naam": "Tariq Mansouri",       "adres": "Dahliastraat 61",       "woonplaats": "Oss",         "emailadres": "tariq.mansouri@hotmail.com"}},
  {"model": "personen.persoon", "pk": 46, "fields": {"naam": "Anna de Wit",          "adres": "Klimopweg 8",           "woonplaats": "Middelburg",  "emailadres": "anna.dewit@live.nl"}},
  {"model": "personen.persoon", "pk": 47, "fields": {"naam": "Bas Vrijhoeven",       "adres": "Goudenregenstraat 32",  "woonplaats": "Drachten",    "emailadres": "bas.vrijhoeven@gmail.com"}},
  {"model": "personen.persoon", "pk": 48, "fields": {"naam": "Layla Boukhari",       "adres": "Narcissusstraat 47",    "woonplaats": "Vlaardingen", "emailadres": "layla.boukhari@outlook.com"}},
  {"model": "personen.persoon", "pk": 49, "fields": {"naam": "Hugo van Ommen",       "adres": "Heideweg 6",            "woonplaats": "Veenendaal",  "emailadres": "hugo.vanommen@hotmail.com"}},
  {"model": "personen.persoon", "pk": 50, "fields": {"naam": "Zara El Amrani",       "adres": "Seringenlaan 23",       "woonplaats": "Schiedam",    "emailadres": "zara.elamrani@gmail.com"}}
]
```

Laad de fixture in de database:

```bash
python manage.py loaddata personen
```

---

## 12. Server starten & testen

### Server starten:

```bash
python manage.py runserver
```

De server draait op **http://127.0.0.1:8000**

### Beschikbare endpoints:

| Method | URL | Beschrijving |
|--------|-----|--------------|
| `GET` | `/` | Welkomstbericht |
| `GET` | `/health/` | Health check |
| `GET` | `/personen/` | Alle personen ophalen |
| `GET` | `/personen/{id}/` | Één persoon ophalen op ID |
| `POST` | `/personen/` | Nieuwe persoon toevoegen |
| `PUT` | `/personen/{id}/` | Persoon volledig bewerken |
| `PATCH` | `/personen/{id}/` | Persoon gedeeltelijk bewerken |
| `DELETE` | `/personen/{id}/` | Persoon verwijderen |

> ⚠️ **Let op:** Django URLs eindigen standaard op een `/` (trailing slash)

### Testen via de browser:

Open http://127.0.0.1:8000/personen/ in je browser — DRF toont een interactieve **Browsable API** pagina!

### Testen via de terminal (curl):

```bash
# Alle personen ophalen
curl http://127.0.0.1:8000/personen/

# Één persoon ophalen
curl http://127.0.0.1:8000/personen/1/

# Nieuwe persoon toevoegen
curl -X POST http://127.0.0.1:8000/personen/ \
  -H "Content-Type: application/json" \
  -d '{"naam": "Test Persoon", "adres": "Teststraat 1", "woonplaats": "Teststad", "emailadres": "test@example.com"}'

# Persoon bewerken
curl -X PUT http://127.0.0.1:8000/personen/1/ \
  -H "Content-Type: application/json" \
  -d '{"naam": "Nieuw Naam", "adres": "Nieuw Adres 1", "woonplaats": "Amsterdam", "emailadres": "nieuw@example.com"}'

# Persoon verwijderen
curl -X DELETE http://127.0.0.1:8000/personen/1/
```

---

## 13. Admin panel

Een groot voordeel van Django is het **gratis admin panel**. Hiermee kun je data beheren via een webinterface.

### Superuser aanmaken:

```bash
python manage.py createsuperuser
```

Vul een gebruikersnaam, e-mailadres en wachtwoord in.

### Persoon model registreren in admin — `personen/admin.py`:

```python
from django.contrib import admin
from .models import Persoon


@admin.register(Persoon)
class PersoonAdmin(admin.ModelAdmin):
    list_display = ['id', 'naam', 'woonplaats', 'emailadres']
    search_fields = ['naam', 'woonplaats', 'emailadres']
    list_filter = ['woonplaats']
```

### Admin panel openen:

Ga naar http://127.0.0.1:8000/admin/ en log in met je superuser account.

---

## 14. Overzicht: FastAPI vs Django vergelijking

### Model/Schema

| FastAPI | Django |
|---|---|
| `class Persoon(BaseModel)` | `class Persoon(models.Model)` |
| `class PersoonUpdate(BaseModel)` | Serializer met `partial=True` |
| Alleen validatie, geen database | Model + database + validatie |

### Routes/Endpoints

| FastAPI | Django + DRF |
|---|---|
| `@app.get("/personen")` | `router.register(r'personen', ViewSet)` |
| `@app.post("/personen")` | Ingebouwd in `ModelViewSet` |
| `raise HTTPException(404)` | `raise Http404` of automatisch via DRF |

### Applicatie starten

| FastAPI | Django |
|---|---|
| `uvicorn main:app --reload` | `python manage.py runserver` |
| `http://127.0.0.1:8000/docs` | `http://127.0.0.1:8000/personen/` (Browsable API) |

---

## 15. Projectstructuur

Na het volgen van alle stappen ziet jouw project er zo uit:

```
django_personen/
├── .venv/                        # Virtual environment
├── manage.py                     # Django management tool
├── requirements.txt              # Pakketlijst
├── db.sqlite3                    # SQLite database (automatisch aangemaakt)
│
├── personen_project/             # Hoofdproject configuratie
│   ├── __init__.py
│   ├── settings.py               # Instellingen (INSTALLED_APPS, etc.)
│   ├── urls.py                   # Hoofd URL routing
│   └── wsgi.py
│
└── personen/                     # Personen app
    ├── __init__.py
    ├── admin.py                  # Admin panel configuratie
    ├── apps.py
    ├── migrations/               # Database migraties
    │   └── 0001_initial.py
    ├── models.py                 # Persoon model (database schema)
    ├── serializers.py            # Data validatie & serialisatie
    ├── urls.py                   # URL routing voor personen
    ├── views.py                  # API endpoints (views)
    └── fixtures/
        └── personen.json         # Startdata (50 personen)
```

---

## 🎉 Gefeliciteerd!

Je hebt de Personen-API succesvol omgebouwd van FastAPI naar Django REST Framework. Je beschikt nu over:

- ✅ Een volledige CRUD API voor personen
- ✅ Een echte database (SQLite) in plaats van in-memory opslag
- ✅ Een gratis admin panel om data te beheren
- ✅ Een interactieve Browsable API voor testen in de browser
- ✅ 50 personen als startdata via fixtures

---

## 📦 Gebruikte packages

| Package | Beschrijving |
|---------|--------------|
| `django` | Het volledige Django framework |
| `djangorestframework` | Django REST Framework voor API's |

Installeer alles met:

```bash
pip install django djangorestframework
```
