# Bruker blir spurt om navn, hvor de kommer fra og hvor gammel de er. Dette printes så ut som en tekst

# funksjon for å definere hvordan input fra bruker skal printes
def personalia():
    # lagrer input fra bruker i variabler som vi kan printe ut senere
    navn = input("Skriv inn hele navnet ditt: ")
    sted = input("Hvor i Norge kommer du fra?: ")
    alder = input("Hvor gammel er du?: ")

    # printer varaibler + tekst
    print("Hei,", navn, "som er", alder, "og kommer fra", sted, "\n")

# caller funksjonen personalia x 3
personalia()
personalia()
personalia()
