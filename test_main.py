import pytest
from fastapi.testclient import TestClient
from main import app, PERSONEN, Persoon

client = TestClient(app)


# ─── Fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def herstel_personen():
    """Reset de PERSONEN lijst na elke test zodat tests onafhankelijk zijn."""
    origineel = PERSONEN.copy()
    yield
    PERSONEN.clear()
    PERSONEN.extend(origineel)


# ─── GET / ────────────────────────────────────────────────────────────────────

class TestRoot:
    def test_root_status_200(self):
        response = client.get("/")
        assert response.status_code == 200

    def test_root_bericht(self):
        response = client.get("/")
        assert response.json() == {"message": "Welkom bij FastAPI Copilte!"}


# ─── GET /health ──────────────────────────────────────────────────────────────

class TestHealth:
    def test_health_status_200(self):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_ok(self):
        response = client.get("/health")
        assert response.json() == {"status": "ok"}


# ─── GET /personen ────────────────────────────────────────────────────────────

class TestGetPersonen:
    def test_geeft_lijst_terug(self):
        response = client.get("/personen")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_bevat_50_records(self):
        response = client.get("/personen")
        assert len(response.json()) == 50

    def test_eerste_persoon_velden(self):
        response = client.get("/personen")
        persoon = response.json()[0]
        assert "id" in persoon
        assert "naam" in persoon
        assert "adres" in persoon
        assert "woonplaats" in persoon
        assert "emailadres" in persoon

    def test_eerste_persoon_waarden(self):
        response = client.get("/personen")
        persoon = response.json()[0]
        assert persoon["id"] == 1
        assert persoon["naam"] == "Mohammed Al-Rashid"
        assert persoon["woonplaats"] == "Amsterdam"


# ─── GET /personen/{id} ───────────────────────────────────────────────────────

class TestGetPersoon:
    def test_bestaand_id(self):
        response = client.get("/personen/1")
        assert response.status_code == 200

    def test_correcte_data_terug(self):
        response = client.get("/personen/5")
        data = response.json()
        assert data["id"] == 5
        assert data["naam"] == "Tim van den Berg"
        assert data["woonplaats"] == "Eindhoven"

    def test_niet_bestaand_id_404(self):
        response = client.get("/personen/9999")
        assert response.status_code == 404

    def test_niet_bestaand_id_bericht(self):
        response = client.get("/personen/9999")
        assert response.json()["detail"] == "Persoon niet gevonden"

    def test_laatste_persoon(self):
        response = client.get("/personen/50")
        assert response.status_code == 200
        assert response.json()["naam"] == "Zara El Amrani"


# ─── POST /personen ───────────────────────────────────────────────────────────

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

    def test_toevoegen_geeft_persoon_terug(self):
        response = client.post("/personen", json=self.NIEUWE_PERSOON)
        data = response.json()
        assert data["id"] == 51
        assert data["naam"] == "Test Persoon"
        assert data["emailadres"] == "test@test.com"

    def test_toevoegen_staat_in_lijst(self):
        client.post("/personen", json=self.NIEUWE_PERSOON)
        response = client.get("/personen/51")
        assert response.status_code == 200
        assert response.json()["naam"] == "Test Persoon"

    def test_duplicate_id_400(self):
        response = client.post("/personen", json={
            "id": 1,
            "naam": "Kopie",
            "adres": "Straat 1",
            "woonplaats": "Stad",
            "emailadres": "kopie@test.com"
        })
        assert response.status_code == 400

    def test_duplicate_id_bericht(self):
        response = client.post("/personen", json={
            "id": 1,
            "naam": "Kopie",
            "adres": "Straat 1",
            "woonplaats": "Stad",
            "emailadres": "kopie@test.com"
        })
        assert "bestaat al" in response.json()["detail"]

    def test_lijst_groeit_na_toevoegen(self):
        client.post("/personen", json=self.NIEUWE_PERSOON)
        response = client.get("/personen")
        assert len(response.json()) == 51


# ─── PUT /personen/{id} ───────────────────────────────────────────────────────

class TestPutPersoon:
    def test_bewerken_status_200(self):
        response = client.put("/personen/1", json={"naam": "Gewijzigde Naam"})
        assert response.status_code == 200

    def test_naam_bijgewerkt(self):
        client.put("/personen/1", json={"naam": "Nieuwe Naam"})
        response = client.get("/personen/1")
        assert response.json()["naam"] == "Nieuwe Naam"

    def test_emailadres_bijgewerkt(self):
        client.put("/personen/1", json={"emailadres": "nieuw@email.com"})
        response = client.get("/personen/1")
        assert response.json()["emailadres"] == "nieuw@email.com"

    def test_overige_velden_ongewijzigd(self):
        originele_adres = client.get("/personen/1").json()["adres"]
        client.put("/personen/1", json={"naam": "Alleen Naam Wijzigen"})
        response = client.get("/personen/1")
        assert response.json()["adres"] == originele_adres

    def test_meerdere_velden_tegelijk(self):
        client.put("/personen/2", json={"naam": "Nieuw", "woonplaats": "Rotterdam"})
        response = client.get("/personen/2")
        assert response.json()["naam"] == "Nieuw"
        assert response.json()["woonplaats"] == "Rotterdam"

    def test_niet_bestaand_id_404(self):
        response = client.put("/personen/9999", json={"naam": "X"})
        assert response.status_code == 404


# ─── DELETE /personen/{id} ────────────────────────────────────────────────────

class TestDeletePersoon:
    def test_verwijderen_status_200(self):
        response = client.delete("/personen/1")
        assert response.status_code == 200

    def test_verwijder_bericht(self):
        response = client.delete("/personen/1")
        assert "verwijderd" in response.json()["message"]

    def test_persoon_niet_meer_op_te_halen(self):
        client.delete("/personen/1")
        response = client.get("/personen/1")
        assert response.status_code == 404

    def test_lijst_krimpt_na_verwijderen(self):
        client.delete("/personen/1")
        response = client.get("/personen")
        assert len(response.json()) == 49

    def test_niet_bestaand_id_404(self):
        response = client.delete("/personen/9999")
        assert response.status_code == 404

    def test_niet_bestaand_id_bericht(self):
        response = client.delete("/personen/9999")
        assert response.json()["detail"] == "Persoon niet gevonden"
