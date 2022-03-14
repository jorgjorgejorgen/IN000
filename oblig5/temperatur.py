# Oppgave 4

# Lese filer med registrert høyeste temperatur. Vi vil lese fra fil og lagre to tabulære data i en ny tom ordbok
# dato er nøkkel og temperatur er verdi

ordbok = {}

# funksjonen tar inn et filnavn og splitter linjer i kolloner
def mndTemp(filnavn):
    filnavn = open(filnavn)
    for linje in filnavn:
        # linje splittes ved komma i filen
        biter = linje.split(",")
        # dato er nøkkel
        dato = biter[0]
        #tempratur er verdi
        temp = float(biter[1])
        # vi putter da nøkkel og verdi inn i den tomme ordboken og returnerer ordboken
        ordbok[dato] = temp
    return ordbok

# vi kaller lesFil funksjon og åpner filen med max mnd temperatur
mndTemp("max_temperatures_per_month.csv")

# prosedyren tar inn ordboken og en fil. Vi går gjennom linjene og splitter i kolonner
def dagligTemp(ordbok, filnavn):
    filnavn = open(filnavn)
    for linje in filnavn:
        biter = linje.split(",")
        # vi oppdaterer variabler for dato og temp for gjeldende fil
        dato = biter[0]
        temp = float(biter[2])
        # dersom vi finner en temperatur som er høyere en tidligere
        if temp > ordbok[dato]:
            print(f"Vi fant en ny rekord for {dato} med en temperatur på {temp} celsius. Den forrige rekorden var {ordbok[dato]} celsius ")
            # oppdatere ordbok med ny høyeste temp
            ordbok[dato] = temp
    print(ordbok)
    return ordbok

# kjøre prosedyre med filen for max daglige temperaturer
dagligTemp(ordbok, "max_daily_temperature_2018.csv")

# prosedyre som oppdaterer filen max_temperature_per_month basert på nye funn
def oppdatereMndTemp(filnavn, ordbok):
    filnavn = open(filnavn, "w")
    # iterere nøkkel og og verdi i ordboka vi laget og skrive ny temp til fil
    for n, v in ordbok.items():
        filnavn.write(str(n) + ','+ str(v) + '\n')
    filnavn.close()

oppdatereMndTemp("max_temperatures_per_month.csv", ordbok)

