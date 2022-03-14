# Oppgave 4

# funksjon for å vise personers matplan
def matplaner():
    # printer ut personene. Litt usikker på om dette er beste måte
    print(matliste.keys())
    # bruker skriver inn personen de vil ha planen til, legges til i variable navn
    navn = input("Hvem ønsker du matplanen til? Skriv inn navnet: ")
    # hvis navnet ikke finnes i listen
    if navn not in matliste:
        print("Fant ikke beboer")
    # navnet finnes i listen
    else:
        # vi vil ha matplanen, altså verdien til key.
        # vi finner da planen til personen som er skrevet inn
        matplan = matliste[navn]
        print(matplan)

# ordbok for personer med tilørende matplan
matliste = {
    "Kjell T Ringen": ["Frokost: Havregryn", "Lunsj: Egg", "Middag:Kjøttkaker"],
    "Rino Thue": ["Frokost: Havregryn", "Lunsj: Suppe", "Middag: Lasagne"],
    "Myysil Bergsprekken": ["Frokost: Brødskiver", "Lunsj: Egg", "Middag: Suppe"]
}

matplaner()

#Hvilken type samling (liste, mengde, ordbok) ville du brukt for å representere hver av
#de følgende eksemplene på data? Skriv litt om hvorfor, eventuelt med forbehold eller
#presiseringer.

#a. Brukernavn på alle IN1000 studentene
    # Her ville jeg brukt ordbok, da vi kan ha mange brukere, men bare én unik med et unikt brukernavn.
#b. Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000
    # Ville brukt ordbok her også, da score er en verdi tilknyttet én nøkkel (student).
#c. Alle vinnere i Lotto siste år (kun navn)
    # Her ville jeg brukt liste, siden vi kun skal holde orden på navnene på vinnere.
#d. All mat noen gjester i et selskap er allergisk mot (for å planlegge menyen)
    # Ville brukt ordbok her, da vi trenger noe (en person eller gruppe) å knytte allergien til.
    # En mulighet er også å bruke liste, da vi ikke nødvendigvis trenger å ha unike elementer i listen.
    # En person kan for eksempel ha flere allergier og personen kan være oppført flere ganger. Dette hadde nok kanskje blitt litt uoversiktlig


