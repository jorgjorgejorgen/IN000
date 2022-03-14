# Oppgave 3
# Program som lar brukere lage plan for reise.

steder = []
klesplagg = []
avreisedato = []
reiseplan = steder, klesplagg, avreisedato

# krever input x5 til de tre listene i reiseplan
for i in range(0, 5):
    sted = input("Skriv inn reisemål: ")
    klaer = input("Skriv inn klesplagg: ")
    dato = input("Skriv inn avreisedato: ")
    steder.append(sted)
    klesplagg.append(klaer)
    avreisedato.append(dato)

# skrive ut reiseplanen
for i in reiseplan:
    print(i)

# tar en indeksverdi fra bruker
indeks1 = int(input("Skriv inn plass i reiseplan: "))
# dersom tallet er større eller lik 0 ikke ute av range i reiseplan
if indeks1 >= 0 and indeks1 <= len(reiseplan)-1:
    # bruker kan velge neste plass i listen
    indeks2 = int(input("Skriv inn plass i liste: "))
    if indeks2 >= 0 and indeks2 <= len(reiseplan[indeks1])-1:
        print(reiseplan[indeks1][indeks2])
    else:
        print("Ugyldig innput!")
else:
    print("Ugyldig innput!")