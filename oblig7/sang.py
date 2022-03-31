# Oppgave 2
# Klassen Sang defineres

class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

    # returnerer artist og tittel som en streng
    def __str__(self):
        return f"{self._artist} av {self._tittel}"

    # spiller av musikken
    def spill(self):
        print(f"Spiller {self}")

    # sjekker om artist oppgitt samsvarer med ett eller flere ord i artistens navn
    def sjekkArtist(self, navn):
        for i in navn.split():
            if i in self._artist.split():
                return True
        return False

    # sjekker om tittel som legges inn samsvarer med tittel i objektet
    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        else:
            return False

    # sjekker om artist og tittel stemmer med instansvariabler i objekt
    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkArtist(artist) and self.sjekkTittel(tittel):
            return True
        else:
            return False

