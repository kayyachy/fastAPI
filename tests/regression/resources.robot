*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}         http://127.0.0.1:8000
${SESSIE}           fastapi_sessie
${RESPONSE}         ${EMPTY}

*** Keywords ***
# ── Setup / Teardown ──────────────────────────────────────────
De API server is beschikbaar
    Create Session    ${SESSIE}    ${BASE_URL}

De sessie wordt gesloten
    Delete All Sessions

# ── GET ───────────────────────────────────────────────────────
Ik een GET verzoek stuur naar "${pad}"
    ${RESPONSE}=    GET On Session    ${SESSIE}    ${pad}    expected_status=any
    Set Test Variable    ${RESPONSE}

# ── POST ──────────────────────────────────────────────────────
Ik een POST verzoek stuur naar "${pad}" met body
    [Arguments]    &{body}
    ${RESPONSE}=    POST On Session    ${SESSIE}    ${pad}    json=${body}    expected_status=any
    Set Test Variable    ${RESPONSE}

# ── PUT ───────────────────────────────────────────────────────────────────────
Ik een PUT verzoek stuur naar "${pad}" met body
    [Arguments]    &{body}
    ${RESPONSE}=    PUT On Session    ${SESSIE}    ${pad}    json=${body}    expected_status=any
    Set Test Variable    ${RESPONSE}

# ── DELETE ────────────────────────────────────────────────────
Ik een DELETE verzoek stuur naar "${pad}"
    ${RESPONSE}=    DELETE On Session    ${SESSIE}    ${pad}    expected_status=any
    Set Test Variable    ${RESPONSE}

# ── Validaties ────────────────────────────────────────────────
De statuscode is ${code}
    Should Be Equal As Integers    ${RESPONSE.status_code}    ${code}

Het veld "${veld}" heeft waarde "${waarde}"
    ${body}=    Set Variable    ${RESPONSE.json()}
    Should Be Equal    ${body}[${veld}]    ${waarde}

Het veld "${veld}" als integer heeft waarde ${waarde}
    ${body}=    Set Variable    ${RESPONSE.json()}
    Should Be Equal As Integers    ${body}[${veld}]    ${waarde}

De response een lijst is
    ${body}=    Set Variable    ${RESPONSE.json()}
    Should Not Be Empty    ${body}

De lijst minimaal ${aantal} records bevat
    ${body}=    Set Variable    ${RESPONSE.json()}
    ${lengte}=    Get Length    ${body}
    Should Be True    ${lengte} >= ${aantal}

Het eerste record de velden id, naam, adres, woonplaats en emailadres bevat
    ${eerste}=    Set Variable    ${RESPONSE.json()}[0]
    Dictionary Should Contain Key    ${eerste}    id
    Dictionary Should Contain Key    ${eerste}    naam
    Dictionary Should Contain Key    ${eerste}    adres
    Dictionary Should Contain Key    ${eerste}    woonplaats
    Dictionary Should Contain Key    ${eerste}    emailadres

Het eerste item veld "${veld}" heeft waarde "${waarde}"
    ${eerste}=    Set Variable    ${RESPONSE.json()}[0]
    Should Be Equal    ${eerste}[${veld}]    ${waarde}

De foutmelding "${tekst}" bevat
    ${body}=    Set Variable    ${RESPONSE.json()}
    Should Contain    ${body}[detail]    ${tekst}

De foutmelding exact "${tekst}" is
    ${body}=    Set Variable    ${RESPONSE.json()}
    Should Be Equal    ${body}[detail]    ${tekst}

Het bevestigingsbericht "${tekst}" bevat
    ${body}=    Set Variable    ${RESPONSE.json()}
    Should Contain    ${body}[message]    ${tekst}
