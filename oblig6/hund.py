# Oppgave 3

class Hund:
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    # metoder for å få alder og vekt
    def hentAlder(self):
        return self._alder

    def hentVekt(self):
        return  self._vekt

    # metode for å minske metthet
    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1

    # hvis hunden spiser, øker vekt
    def spis(self, tall):
        # legger til heltall til metthet
        self._metthet += int(tall)
        if tall > 7:
            self._vekt += 1


