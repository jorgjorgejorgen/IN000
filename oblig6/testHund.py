# Oppgave 3: test for klassen hund

from hund import Hund

def hovedprogram():
    hund1 = Hund(12, 10)
    hund1.spring()
    hund1.spis(7)
    print(hund1.hentVekt())
    hund1.spring()
    hund1.spis(12)
    print(hund1.hentVekt())

hovedprogram()