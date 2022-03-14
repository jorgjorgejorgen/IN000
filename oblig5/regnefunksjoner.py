# Oppgave 1

# funksjon med to parametere a, b, som tester addisjon, returnerer resultat
def addisjon(a, b):
    return a + b

addere = addisjon(2, 2)
print(addere)

# funksjon som tester subtraksjon, a minus b
def subtraksjon(a, b):
    return  a - b

# funksjon som tester divisjon
def divisjon(a, b):
    return  a / b

# funksjon  for å teste om subtraksjon-funksjon er korrekt
def testSubtraksjon():
    # her passer vi inn to tall i assert for å se om vi får ønsket resultat ved subtraksjon.
    # om alt er korrekt skal det ikke gi error når vi kaller funksjonen.
    assert subtraksjon(2, 2) == 0
    assert subtraksjon(-2, -2) == 0
    assert subtraksjon(-2, 2) == - 4

def testDivisjon():
    assert divisjon(4, 2) == 2
    assert divisjon(-4, -2) == 2
    assert divisjon(4, -2) == -2

testSubtraksjon()
testDivisjon()

# funksjon som konvererer tommer til cm
def tommerTilCm(antallTommer):
    # først sjekker vi om antallTommer er større enn 0
    assert antallTommer > 0
    # her regner vi om tommer til cm
    return antallTommer * 2.54

# funksjon for å teste tommerTilCm. Vi sjekker her om 1 og 6 tomme gir riktig resultat i cm
def testTommerTilCm():
    assert tommerTilCm(1) == 2.54
    assert tommerTilCm(6) == 15.24
testTommerTilCm()

# prosedyre som tar tall fra input, vi bruker så tidligere prosedyrer for å regne
def skrivBeregninger():
    a = float(input("Skriv inn første tall: "))
    b = float(input("Skriv inn andre tall: "))
    print("Addisjon er: ", addisjon(a, b))
    print("Subtraksjon er: ", subtraksjon(a, b))
    print("Divisjon er: ", divisjon(a, b))

    # tar et nytt tall på input, c, for å regne om til cm
    print("\nKonvertering fra tommer til cm")
    c = float(input("Skriv inn tall i tommer: "))
    print(f"Resultat: {tommerTilCm(c)} cm")

skrivBeregninger()




