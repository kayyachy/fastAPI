*** Settings ***
Resource          resources.robot
Library           Collections

Suite Setup       De API server is beschikbaar
Suite Teardown    De sessie wordt gesloten

*** Test Cases ***

# ═══════════════════════════════════════════════════════════════
# ROOT ENDPOINT
# ═══════════════════════════════════════════════════════════════

ROOT - De root endpoint geeft een HTTP 200 terug
    [Tags]    root    smoke
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/"
    Then De statuscode is 200

ROOT - Het welkomstbericht is correct
    [Tags]    root    smoke
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/"
    Then Het veld "message" heeft waarde "Welkom bij FastAPI Copilte!"

# ═══════════════════════════════════════════════════════════════
# HEALTH ENDPOINT
# ═══════════════════════════════════════════════════════════════

HEALTH - De health endpoint geeft een HTTP 200 terug
    [Tags]    health    smoke
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/health"
    Then De statuscode is 200

HEALTH - De status is ok
    [Tags]    health    smoke
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/health"
    Then Het veld "status" heeft waarde "ok"

# ═══════════════════════════════════════════════════════════════
# GET /personen
# ═══════════════════════════════════════════════════════════════

GET PERSONEN - De lijst met personen is opvraagbaar
    [Tags]    get    personen    regression
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/personen"
    Then De statuscode is 200
    And De response een lijst is

GET PERSONEN - De lijst bevat minimaal 50 records
    [Tags]    get    personen    regression
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/personen"
    Then De lijst minimaal 50 records bevat

GET PERSONEN - Elk record bevat alle verplichte velden
    [Tags]    get    personen    regression
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/personen"
    Then Het eerste record de velden id, naam, adres, woonplaats en emailadres bevat

GET PERSONEN - De eerste persoon is Mohammed Al-Rashid uit Amsterdam
    [Tags]    get    personen    regression
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/personen"
    Then Het eerste item veld "naam" heeft waarde "Mohammed Al-Rashid"
    And Het eerste item veld "woonplaats" heeft waarde "Amsterdam"

# ═══════════════════════════════════════════════════════════════
# GET /personen/{id}
# ═══════════════════════════════════════════════════════════════

GET PERSOON - Een bestaande persoon is opvraagbaar op ID
    [Tags]    get    persoon    regression
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/personen/1"
    Then De statuscode is 200

GET PERSOON - De juiste data wordt teruggegeven bij ID 1
    [Tags]    get    persoon    regression
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/personen/1"
    Then Het veld "naam" heeft waarde "Mohammed Al-Rashid"
    And Het veld "woonplaats" heeft waarde "Amsterdam"
    And Het veld "emailadres" heeft waarde "m.alrashid@gmail.com"

GET PERSOON - De laatste persoon is opvraagbaar op ID 50
    [Tags]    get    persoon    regression
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/personen/50"
    Then De statuscode is 200
    And Het veld "naam" heeft waarde "Zara El Amrani"
    And Het veld "woonplaats" heeft waarde "Schiedam"

GET PERSOON - Een onbekend ID geeft HTTP 404 terug
    [Tags]    get    persoon    regression    negatief
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/personen/9999"
    Then De statuscode is 404

GET PERSOON - De foutmelding is correct bij een onbekend ID
    [Tags]    get    persoon    regression    negatief
    Given De API server is beschikbaar
    When Ik een GET verzoek stuur naar "/personen/9999"
    Then De foutmelding exact "Persoon niet gevonden" is

# ═══════════════════════════════════════════════════════════════
# POST /personen
# ═══════════════════════════════════════════════════════════════

POST PERSOON - Een nieuwe persoon toevoegen geeft HTTP 201 terug
    [Tags]    post    persoon    regression
    Given De API server is beschikbaar
    When Ik een POST verzoek stuur naar "/personen" met body
    ...    id=${99}
    ...    naam=Robot Test Persoon
    ...    adres=Robotstraat 1
    ...    woonplaats=Robotstad
    ...    emailadres=robot@test.com
    Then De statuscode is 201
    And Het veld "naam" heeft waarde "Robot Test Persoon"
    [Teardown]    Ik een DELETE verzoek stuur naar "/personen/99"

POST PERSOON - De toegevoegde persoon is daarna opvraagbaar
    [Tags]    post    persoon    regression
    Given De API server is beschikbaar
    When Ik een POST verzoek stuur naar "/personen" met body
    ...    id=${98}
    ...    naam=Opvraagbare Persoon
    ...    adres=Testlaan 5
    ...    woonplaats=Teststad
    ...    emailadres=opvraag@test.com
    And Ik een GET verzoek stuur naar "/personen/98"
    Then De statuscode is 200
    And Het veld "naam" heeft waarde "Opvraagbare Persoon"
    [Teardown]    Ik een DELETE verzoek stuur naar "/personen/98"

POST PERSOON - Een duplicate ID geeft HTTP 400 terug
    [Tags]    post    persoon    regression    negatief
    Given De API server is beschikbaar
    When Ik een POST verzoek stuur naar "/personen" met body
    ...    id=${1}
    ...    naam=Duplicate Persoon
    ...    adres=Straat 1
    ...    woonplaats=Stad
    ...    emailadres=dup@test.com
    Then De statuscode is 400

POST PERSOON - De foutmelding is correct bij een duplicate ID
    [Tags]    post    persoon    regression    negatief
    Given De API server is beschikbaar
    When Ik een POST verzoek stuur naar "/personen" met body
    ...    id=${1}
    ...    naam=Duplicate Persoon
    ...    adres=Straat 1
    ...    woonplaats=Stad
    ...    emailadres=dup@test.com
    Then De statuscode is 400
    And De foutmelding "bestaat al" bevat

# ═══════════════════════════════════════════════════════════════
# PUT /personen/{id}
# ═══════════════════════════════════════════════════════════════

PUT PERSOON - Een bestaande persoon bewerken geeft HTTP 200 terug
    [Tags]    put    persoon    regression
    Given De API server is beschikbaar
    When Ik een PUT verzoek stuur naar "/personen/10" met body
    ...    naam=Bijgewerkte Naam
    Then De statuscode is 200
    [Teardown]    Ik een PUT verzoek stuur naar "/personen/10" met body    naam=Lena Mulder

PUT PERSOON - De naam wordt correct bijgewerkt
    [Tags]    put    persoon    regression
    Given De API server is beschikbaar
    When Ik een PUT verzoek stuur naar "/personen/10" met body
    ...    naam=Gewijzigde Naam Robot
    And Ik een GET verzoek stuur naar "/personen/10"
    Then Het veld "naam" heeft waarde "Gewijzigde Naam Robot"
    [Teardown]    Ik een PUT verzoek stuur naar "/personen/10" met body    naam=Lena Mulder

PUT PERSOON - Niet meegestuurde velden blijven ongewijzigd
    [Tags]    put    persoon    regression
    Given De API server is beschikbaar
    And Ik een GET verzoek stuur naar "/personen/10"
    And Het veld "adres" heeft waarde "Schoollaan 28"
    When Ik een PUT verzoek stuur naar "/personen/10" met body
    ...    naam=Alleen Naam Wijzigen
    And Ik een GET verzoek stuur naar "/personen/10"
    Then Het veld "adres" heeft waarde "Schoollaan 28"
    [Teardown]    Ik een PUT verzoek stuur naar "/personen/10" met body    naam=Lena Mulder

PUT PERSOON - Een onbekend ID geeft HTTP 404 terug
    [Tags]    put    persoon    regression    negatief
    Given De API server is beschikbaar
    When Ik een PUT verzoek stuur naar "/personen/9999" met body
    ...    naam=Bestaat Niet
    Then De statuscode is 404
    And De foutmelding exact "Persoon niet gevonden" is

# ═══════════════════════════════════════════════════════════════
# DELETE /personen/{id}
# ═══════════════════════════════════════════════════════════════

DELETE PERSOON - Een bestaande persoon verwijderen geeft HTTP 200 terug
    [Tags]    delete    persoon    regression
    Given De API server is beschikbaar
    And Ik een POST verzoek stuur naar "/personen" met body
    ...    id=${96}
    ...    naam=Te Verwijderen
    ...    adres=Weg 1
    ...    woonplaats=Nergens
    ...    emailadres=weg@test.com
    When Ik een DELETE verzoek stuur naar "/personen/96"
    Then De statuscode is 200

DELETE PERSOON - Het bevestigingsbericht is aanwezig na verwijderen
    [Tags]    delete    persoon    regression
    Given De API server is beschikbaar
    And Ik een POST verzoek stuur naar "/personen" met body
    ...    id=${95}
    ...    naam=Te Verwijderen 2
    ...    adres=Weg 2
    ...    woonplaats=Nergens
    ...    emailadres=weg2@test.com
    When Ik een DELETE verzoek stuur naar "/personen/95"
    Then De statuscode is 200
    And Het bevestigingsbericht "verwijderd" bevat

DELETE PERSOON - Een verwijderd record is niet meer opvraagbaar
    [Tags]    delete    persoon    regression
    Given De API server is beschikbaar
    And Ik een POST verzoek stuur naar "/personen" met body
    ...    id=${94}
    ...    naam=Te Verwijderen 3
    ...    adres=Weg 3
    ...    woonplaats=Nergens
    ...    emailadres=weg3@test.com
    When Ik een DELETE verzoek stuur naar "/personen/94"
    And Ik een GET verzoek stuur naar "/personen/94"
    Then De statuscode is 404

DELETE PERSOON - Een onbekend ID geeft HTTP 404 terug
    [Tags]    delete    persoon    regression    negatief
    Given De API server is beschikbaar
    When Ik een DELETE verzoek stuur naar "/personen/9999"
    Then De statuscode is 404

DELETE PERSOON - De foutmelding is correct bij een onbekend ID
    [Tags]    delete    persoon    regression    negatief
    Given De API server is beschikbaar
    When Ik een DELETE verzoek stuur naar "/personen/9999"
    Then De statuscode is 404
    And De foutmelding exact "Persoon niet gevonden" is