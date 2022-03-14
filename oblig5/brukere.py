# Oppgave 2

# Et program som lager nye brukernavn basert på navn. Vi gir dem så en epost basert på brukernavnet

ordbok = {}

# funksjon som lager brukernavn ved å splitte for- og etternavn
def lagBrukernavn(navn):
    navn = navn.lower().split(" ")
    # brukernavn blir fornavn + førsste bokstav av etternavn, vi returnerer så et brukernavn
    brukernavn = navn[0] + navn[1][0]
    return brukernavn

# funksjon lager epost ved å slå sammen brukernavn med et suffix, returnerer en streng
def lagEpost(brukernavn, suffix):
    return str(f"{brukernavn}@{suffix}")

# prosedyre som printer ut brukere i 'ordbok'og deres epost-adresse
def skrivUtEposter(ordbok):
    for bruker in ordbok:
        print(f"Brukeren {bruker} har epost-adressen: {ordbok[bruker]}")

# while-løkke som kjører så lenge bruker ikke taster 's'
def whileLokke():
    svar = ""
    while (svar != "s"):
        svar = input("Tast 'i' for å lage ny bruker, Tast 'p' for å skrive ut eposter, Tast 's' for åavslutte: ").lower()
        if svar == "s":
            break
        elif svar == "p":
            skrivUtEposter(ordbok)
        elif svar  == "i":
        # svar er 'i'. vi må da kjøre prosedyren lagBrukernavn og lage brukernavn basert på input
        # så kjører vi lagEpost og lagrer input i ordbok
            navn = input("Skriv inn fornavn og etternavn: ")
            suffix = input("Skriv inn suffix for epost-adressen din: ")
            brukernavn = f"{lagBrukernavn(navn)}"
            ordbok[brukernavn] = lagEpost(brukernavn, suffix)
whileLokke()


