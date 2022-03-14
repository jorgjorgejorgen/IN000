# Oppgave 1

# lager liste med tre tall
liste = [1, 3, 2]
# legge til 4 i listen
liste.append(4)

# printer første og siste tall i liste
print(liste[0], liste[3])
# legger sammen tallene i listen
sum = sum(liste)
print("Summen av tallene er:", sum)
# ganger tallene i listen
produkt = liste[0] * liste[1] * liste[2] * liste[3]
print("Produktet er:", produkt)

# liste med sum og produkt
listeToTall = [sum, produkt]
print(listeToTall)

# ny liste som slår sammen liste og listen med sum og produkt
nyListe = liste + listeToTall
print(nyListe)
# fjerne de to siste tallene i listen
nyListe.remove(10), nyListe.remove(24)
print(nyListe)


# to liste som skal ha fire navn som input
navn = []
navn.append(input("\nSkriv inn navn 1: ").upper())
navn.append(input("Skriv inn navn 2: ").upper())
navn.append(input("Skriv inn navn 3: ").upper())
navn.append(input("Skriv inn navn 4: ").upper())

# dersom listen inneholder jørgen
if "JØRGEN" in navn:
    print("Takk! Du husket meg!")
# listen inneholder ikke jørgen
else:
    print("Har du glemt meg?")

