# Oppgave 1: test for motorsykkell class

from motorsykkel import Motorsykkel

def hovedprogram():
    msykkel1 = Motorsykkel("Kawasaki", "L3597", 91708)
    msykkel2 = Motorsykkel("Tempo", "U28680", 1235)
    msykkel3 = Motorsykkel("Yamaha", "C19564", 67844)

    msykkel1.skrivUt()
    msykkel2.skrivUt()
    msykkel3.skrivUt()
    # øke km med 10 på msykkel3
    msykkel3.kjor(10)
    print(msykkel3.hentKilometerstand())

hovedprogram()

