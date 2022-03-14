# Oppgave 5

# Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil

# Formatet vil se slik ut:
#   Skulderbredde 4
#   Halsvidde 3.2
#   Livvidde 10

# Hint: du kan bruke funksjonen .split() for å gjøre dette.

# La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi
# og returner ordboken. Lag deretter en prosedyre som tar imot en liste av mål og
# benytter seg av tommerTilCm som du skrev tidligere for å skrive ut målene i centimeter.


# en funksjon som leser inn fil og splitter nøkkel og verdi. Vi returnerer så verdiene fra ordboken
def skredderMaal():
    ordbok = {}
    fil = open("skreddermaal.csv")
    for linje in fil:
        biter = linje.split()
        kdel = biter[0]
        maal = float(biter[1])
        ordbok[kdel] = maal
    print(ordbok)
    return ordbok.values()

# denne funksjonen kommer fra regnefunksjoner. Jeg fikk feil når jeg importerte, så legger den her.
def tommerTilCm(antallTommer):
    # først sjekker vi om antallTommer er større enn 0
    assert antallTommer > 0
    # her regner vi om tommer til cm
    return antallTommer * 2.54

# prosedyre som tar i mot verdier i en tom liste. Benytter så tommerTilCm for å regne om verdien til cm og legge til liste
def listeTilCm(ordbok):
    tommer_liste = []
    for tommer in ordbok:
        tommer_liste.append(tommerTilCm(tommer))
    print("Mål i cm:")
    return tommer_liste

print(listeTilCm(skredderMaal()))



