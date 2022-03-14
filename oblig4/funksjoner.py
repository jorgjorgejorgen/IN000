# Oppgave 1

#funksjon som adderer to tall og returnerer summen
tall1 = 2
tall2 = 2

def adder(tall1, tall2):
    summen = tall1 + tall2
    print("Summen av tall1 og tall2", summen)

# kjører funksjonen to ganger
adder(tall1, tall2)
adder(tall1, tall2)

# funksjon for å sjekke forelomst av bokstav
streng = input("\nSkriv inn noen få ord her: ")
bokstav = input("Skriv inn en bokstav: ")
ganger = 0

# passer inn varialene over
def tellForekomst(bokstav, streng, ganger):
    for i in streng:
        # hvis bokstav finnes i input
        if i == bokstav:
            ganger += 1
            print(ganger)

tellForekomst(bokstav, streng, ganger)


