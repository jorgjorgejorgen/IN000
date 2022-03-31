# Oppgave 1

# klasse for motorsykkel med merke, regnr. og km.stand

class Motorsykkel:
    def __init__(self, merke, reg, km):
        self._merke = merke
        self._reg = reg
        self._km = km

    def kjor(self, km):
        self._km = self._km + km

    def hentKilometerstand(self):
        return self._km

    def skrivUt(self):
        print(self._merke, self._reg, self._km)

