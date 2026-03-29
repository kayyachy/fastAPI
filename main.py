from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="FastAPI Copilte", version="0.1.0")


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


PERSONEN: List[Persoon] = [
    Persoon(id=1,  naam="Mohammed Al-Rashid",   adres="Keizersgracht 12",      woonplaats="Amsterdam",   emailadres="m.alrashid@gmail.com"),
    Persoon(id=2,  naam="Sophie de Vries",       adres="Lange Voorhout 5",      woonplaats="Den Haag",    emailadres="sophie.devries@hotmail.com"),
    Persoon(id=3,  naam="Lars Janssen",          adres="Marktstraat 8",         woonplaats="Utrecht",     emailadres="lars.janssen@outlook.com"),
    Persoon(id=4,  naam="Fatima El Ouali",       adres="Bergweg 33",            woonplaats="Rotterdam",   emailadres="f.elouali@gmail.com"),
    Persoon(id=5,  naam="Tim van den Berg",      adres="Dorpsstraat 17",        woonplaats="Eindhoven",   emailadres="tim.vandenberg@live.nl"),
    Persoon(id=6,  naam="Emma Bakker",           adres="Hoofdstraat 45",        woonplaats="Groningen",   emailadres="emma.bakker@gmail.com"),
    Persoon(id=7,  naam="Yusuf Özdemir",         adres="Stationsplein 2",       woonplaats="Tilburg",     emailadres="y.ozdemir@yahoo.com"),
    Persoon(id=8,  naam="Nora Visser",           adres="Parkweg 19",            woonplaats="Almere",      emailadres="nora.visser@hotmail.com"),
    Persoon(id=9,  naam="Daan Smit",             adres="Kerkstraat 7",          woonplaats="Breda",       emailadres="daan.smit@gmail.com"),
    Persoon(id=10, naam="Lena Mulder",           adres="Schoollaan 28",         woonplaats="Nijmegen",    emailadres="lena.mulder@outlook.com"),
    Persoon(id=11, naam="Ahmed Benali",          adres="Tulpstraat 3",          woonplaats="Haarlem",     emailadres="ahmed.benali@gmail.com"),
    Persoon(id=12, naam="Julia Meijer",          adres="Rozenlaan 14",          woonplaats="Arnhem",      emailadres="julia.meijer@live.nl"),
    Persoon(id=13, naam="Sander Boer",           adres="Industrieweg 55",       woonplaats="Enschede",    emailadres="sander.boer@hotmail.com"),
    Persoon(id=14, naam="Yasmine Khalil",        adres="Vondelstraat 9",        woonplaats="Zwolle",      emailadres="y.khalil@gmail.com"),
    Persoon(id=15, naam="Pieter de Jong",        adres="Nieuwstraat 22",        woonplaats="Apeldoorn",   emailadres="pieter.dejong@outlook.com"),
    Persoon(id=16, naam="Sara Linders",          adres="Julianaweg 37",         woonplaats="Maastricht",  emailadres="sara.linders@gmail.com"),
    Persoon(id=17, naam="Kevin Willems",         adres="Beatrixlaan 6",         woonplaats="Leiden",      emailadres="kevin.willems@yahoo.com"),
    Persoon(id=18, naam="Amira Tahir",           adres="Koningstraat 50",       woonplaats="Dordrecht",   emailadres="amira.tahir@hotmail.com"),
    Persoon(id=19, naam="Roos van Dijk",         adres="Willemstraat 11",       woonplaats="Zoetermeer",  emailadres="roos.vandijk@gmail.com"),
    Persoon(id=20, naam="Niels Hermans",         adres="Prins Hendrikstraat 4", woonplaats="Deventer",    emailadres="niels.hermans@live.nl"),
    Persoon(id=21, naam="Bilal Chaoui",          adres="Vossenlaan 16",         woonplaats="Delft",       emailadres="bilal.chaoui@gmail.com"),
    Persoon(id=22, naam="Merel Kok",             adres="Zonnebloemstraat 25",   woonplaats="Alkmaar",     emailadres="merel.kok@outlook.com"),
    Persoon(id=23, naam="Joost Hendriks",        adres="Havenstraat 38",        woonplaats="Amersfoort",  emailadres="joost.hendriks@hotmail.com"),
    Persoon(id=24, naam="Leila Nasser",          adres="Boslaan 21",            woonplaats="Venlo",       emailadres="leila.nasser@gmail.com"),
    Persoon(id=25, naam="Bram Peters",           adres="Rembrandtstraat 44",    woonplaats="Helmond",     emailadres="bram.peters@yahoo.com"),
    Persoon(id=26, naam="Iris Vermeer",          adres="Mozartlaan 10",         woonplaats="Leeuwarden",  emailadres="iris.vermeer@gmail.com"),
    Persoon(id=27, naam="Omar Idrissi",          adres="Spinozaweg 29",         woonplaats="Zaandam",     emailadres="omar.idrissi@hotmail.com"),
    Persoon(id=28, naam="Fleur Timmermans",      adres="Wilhelminalaan 3",      woonplaats="Ede",         emailadres="fleur.timmermans@outlook.com"),
    Persoon(id=29, naam="Tom van Leeuwen",       adres="Erasmusstraat 18",      woonplaats="Hilversum",   emailadres="tom.vanleeuwen@live.nl"),
    Persoon(id=30, naam="Nadia Hamid",           adres="Sophiastraat 41",       woonplaats="Roosendaal",  emailadres="nadia.hamid@gmail.com"),
    Persoon(id=31, naam="Rick Kuijpers",         adres="Tramweg 13",            woonplaats="Spijkenisse",  emailadres="rick.kuijpers@hotmail.com"),
    Persoon(id=32, naam="Mila Schouten",         adres="Chopinplein 7",         woonplaats="Emmen",       emailadres="mila.schouten@gmail.com"),
    Persoon(id=33, naam="Karim Aouad",           adres="Lindelaan 30",          woonplaats="Capelle a/d IJssel", emailadres="karim.aouad@yahoo.com"),
    Persoon(id=34, naam="Denise van Rooij",      adres="Kastanjelaan 53",       woonplaats="Heerlen",     emailadres="denise.vanrooij@outlook.com"),
    Persoon(id=35, naam="Mark Peeters",          adres="Schipholweg 26",        woonplaats="Sittard",     emailadres="mark.peeters@gmail.com"),
    Persoon(id=36, naam="Hana Berrada",          adres="Populierenlaan 15",     woonplaats="Gouda",       emailadres="hana.berrada@hotmail.com"),
    Persoon(id=37, naam="Stefan Dekker",         adres="Iepenlaan 48",          woonplaats="Purmerend",   emailadres="stefan.dekker@live.nl"),
    Persoon(id=38, naam="Lotte Huisman",         adres="Beukenweg 36",          woonplaats="Hoorn",       emailadres="lotte.huisman@gmail.com"),
    Persoon(id=39, naam="Anouar El Habti",       adres="Dennenlaan 9",          woonplaats="Alphen a/d Rijn", emailadres="anouar.elhabti@outlook.com"),
    Persoon(id=40, naam="Charlotte Engel",       adres="Magnoliapad 20",        woonplaats="Lelystad",    emailadres="charlotte.engel@hotmail.com"),
    Persoon(id=41, naam="Jesse van Beek",        adres="Veluwelaan 34",         woonplaats="Harderwijk",  emailadres="jesse.vanbeek@gmail.com"),
    Persoon(id=42, naam="Samira Ouali",          adres="Hertogstraat 5",        woonplaats="Bergen op Zoom", emailadres="samira.ouali@yahoo.com"),
    Persoon(id=43, naam="Wouter Groot",          adres="Lübeckstraat 27",       woonplaats="Nieuwegein",  emailadres="wouter.groot@outlook.com"),
    Persoon(id=44, naam="Eva Brouwer",           adres="Azalealaan 43",         woonplaats="Weert",       emailadres="eva.brouwer@gmail.com"),
    Persoon(id=45, naam="Tariq Mansouri",        adres="Dahliastraat 61",       woonplaats="Oss",         emailadres="tariq.mansouri@hotmail.com"),
    Persoon(id=46, naam="Anna de Wit",           adres="Klimopweg 8",           woonplaats="Middelburg",  emailadres="anna.dewit@live.nl"),
    Persoon(id=47, naam="Bas Vrijhoeven",        adres="Goudenregenstraat 32",  woonplaats="Drachten",    emailadres="bas.vrijhoeven@gmail.com"),
    Persoon(id=48, naam="Layla Boukhari",        adres="Narcissusstraat 47",    woonplaats="Vlaardingen",  emailadres="layla.boukhari@outlook.com"),
    Persoon(id=49, naam="Hugo van Ommen",        adres="Heideweg 6",            woonplaats="Veenendaal",  emailadres="hugo.vanommen@hotmail.com"),
    Persoon(id=50, naam="Zara El Amrani",        adres="Seringenlaan 23",       woonplaats="Schiedam",    emailadres="zara.elamrani@gmail.com"),
]


@app.get("/")
def root():
    return {"message": "Welkom bij FastAPI Copilte!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/personen", response_model=List[Persoon])
def get_personen():
    return PERSONEN


@app.get("/personen/{persoon_id}", response_model=Persoon)
def get_persoon(persoon_id: int):
    for persoon in PERSONEN:
        if persoon.id == persoon_id:
            return persoon
    raise HTTPException(status_code=404, detail="Persoon niet gevonden")


@app.post("/personen", response_model=Persoon, status_code=201)
def voeg_persoon_toe(persoon: Persoon):
    for p in PERSONEN:
        if p.id == persoon.id:
            raise HTTPException(status_code=400, detail=f"Persoon met id {persoon.id} bestaat al")
    PERSONEN.append(persoon)
    return persoon


@app.put("/personen/{persoon_id}", response_model=Persoon)
def bewerk_persoon(persoon_id: int, update: PersoonUpdate):
    for i, persoon in enumerate(PERSONEN):
        if persoon.id == persoon_id:
            bijgewerkt = persoon.model_copy(update=update.model_dump(exclude_none=True))
            PERSONEN[i] = bijgewerkt
            return bijgewerkt
    raise HTTPException(status_code=404, detail="Persoon niet gevonden")


@app.delete("/personen/{persoon_id}", status_code=200)
def verwijder_persoon(persoon_id: int):
    for i, persoon in enumerate(PERSONEN):
        if persoon.id == persoon_id:
            PERSONEN.pop(i)
            return {"message": f"Persoon met id {persoon_id} is verwijderd"}
    raise HTTPException(status_code=404, detail="Persoon niet gevonden")
