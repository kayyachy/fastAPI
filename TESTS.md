# Unit Tests – FastAPI Copilte

Documentatie van alle unit tests voor de FastAPI Copilte applicatie.

---

## 🛠️ Vereisten

Zorg dat de virtual environment actief is en de packages geïnstalleerd zijn:

```powershell
.venv\Scripts\Activate.ps1
pip install pytest httpx
```

---

## ▶️ Tests uitvoeren

```powershell
# Alle tests uitvoeren
.venv\Scripts\pytest test_main.py -v

# Alleen een specifieke klasse testen
.venv\Scripts\pytest test_main.py::TestPostPersoon -v

# Alleen een specifieke test uitvoeren
.venv\Scripts\pytest test_main.py::TestDeletePersoon::test_verwijderen_status_200 -v

# Tests met samenvatting
.venv\Scripts\pytest test_main.py -v --tb=short
```

---

## 📋 Testoverzicht

**Totaal: 31 tests** | Bestand: `test_main.py`

---

### ✅ TestRoot (2 tests)

Endpoint: `GET /`

| Test | Beschrijving |
|------|-------------|
| `test_root_status_200` | Controleert of de root endpoint HTTP 200 teruggeeft |
| `test_root_bericht` | Controleert of het welkomstbericht correct is |

---

### ✅ TestHealth (2 tests)

Endpoint: `GET /health`

| Test | Beschrijving |
|------|-------------|
| `test_health_status_200` | Controleert of de health endpoint HTTP 200 teruggeeft |
| `test_health_ok` | Controleert of de status `"ok"` is |

---

### ✅ TestGetPersonen (4 tests)

Endpoint: `GET /personen`

| Test | Beschrijving |
|------|-------------|
| `test_geeft_lijst_terug` | Controleert of de response een lijst is |
| `test_bevat_50_records` | Controleert of er precies 50 personen zijn |
| `test_eerste_persoon_velden` | Controleert of alle velden aanwezig zijn (`id`, `naam`, `adres`, `woonplaats`, `emailadres`) |
| `test_eerste_persoon_waarden` | Controleert de correcte waarden van de eerste persoon |

---

### ✅ TestGetPersoon (5 tests)

Endpoint: `GET /personen/{id}`

| Test | Beschrijving |
|------|-------------|
| `test_bestaand_id` | Controleert HTTP 200 bij een geldig ID |
| `test_correcte_data_terug` | Controleert of de juiste persoon wordt teruggegeven |
| `test_niet_bestaand_id_404` | Controleert HTTP 404 bij een onbekend ID |
| `test_niet_bestaand_id_bericht` | Controleert de foutmelding bij een onbekend ID |
| `test_laatste_persoon` | Controleert of persoon met ID 50 correct opgehaald wordt |

---

### ✅ TestPostPersoon (6 tests)

Endpoint: `POST /personen`

| Test | Beschrijving |
|------|-------------|
| `test_toevoegen_status_201` | Controleert HTTP 201 bij succesvol toevoegen |
| `test_toevoegen_geeft_persoon_terug` | Controleert of de toegevoegde persoon wordt teruggegeven |
| `test_toevoegen_staat_in_lijst` | Controleert of de nieuwe persoon opvraagbaar is na toevoegen |
| `test_duplicate_id_400` | Controleert HTTP 400 bij een al bestaand ID |
| `test_duplicate_id_bericht` | Controleert de foutmelding bij een duplicate ID |
| `test_lijst_groeit_na_toevoegen` | Controleert of de lijst van 50 naar 51 records groeit |

---

### ✅ TestPutPersoon (6 tests)

Endpoint: `PUT /personen/{id}`

| Test | Beschrijving |
|------|-------------|
| `test_bewerken_status_200` | Controleert HTTP 200 bij succesvol bewerken |
| `test_naam_bijgewerkt` | Controleert of de naam correct wordt bijgewerkt |
| `test_emailadres_bijgewerkt` | Controleert of het emailadres correct wordt bijgewerkt |
| `test_overige_velden_ongewijzigd` | Controleert of niet-meegestuurde velden ongewijzigd blijven |
| `test_meerdere_velden_tegelijk` | Controleert of meerdere velden tegelijk bijgewerkt kunnen worden |
| `test_niet_bestaand_id_404` | Controleert HTTP 404 bij een onbekend ID |

---

### ✅ TestDeletePersoon (6 tests)

Endpoint: `DELETE /personen/{id}`

| Test | Beschrijving |
|------|-------------|
| `test_verwijderen_status_200` | Controleert HTTP 200 bij succesvol verwijderen |
| `test_verwijder_bericht` | Controleert of het bevestigingsbericht aanwezig is |
| `test_persoon_niet_meer_op_te_halen` | Controleert of een verwijderde persoon HTTP 404 geeft |
| `test_lijst_krimpt_na_verwijderen` | Controleert of de lijst van 50 naar 49 records krimpt |
| `test_niet_bestaand_id_404` | Controleert HTTP 404 bij een onbekend ID |
| `test_niet_bestaand_id_bericht` | Controleert de foutmelding bij een onbekend ID |

---

## 🔄 Fixture

Elke test maakt gebruik van de `herstel_personen` fixture die automatisch na elke test de `PERSONEN` lijst reset naar de originele 50 records. Dit zorgt ervoor dat tests volledig onafhankelijk van elkaar zijn.

```python
@pytest.fixture(autouse=True)
def herstel_personen():
    origineel = PERSONEN.copy()
    yield
    PERSONEN.clear()
    PERSONEN.extend(origineel)
```

---

## 📊 Verwacht resultaat

```
31 passed in ~0.5s
```
