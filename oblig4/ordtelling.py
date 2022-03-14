# Oppgave 4
# ordtelling og bokstavtelling

# funksjon som teller bokstaver i et ord
def bokstavteller(ord):
    antall = 0
    # finner om bokstav er i ordet
    for i in ord:
        # antall øker da med 1 for hver loop
        antall += 1
    return antall

#funksjon som teller ord i en setning og legger de til i ordbok
def ordteller(setning):
    dict = {}
    ordene = setning.split()

    for i in ordene:
        # dersom ord finnes i dict, øker antall ganger. Ellers legger vi det til
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

setning = input("Skriv inn en setning: ")
ordGanger = ordteller(setning)

print("Det er", len(ordGanger),  "ord i setningen din.")
for i in ordGanger:
    print("Ordet", i, "forekommer", ordGanger[i], "ganger, og har", bokstavteller(i), "bokstaver")