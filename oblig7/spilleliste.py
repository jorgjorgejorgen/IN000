# Oppgave 3
# Klassen Spilleliste defineres her

from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    # åpner en fil, fjerner mellomrom og splitter tittel artist ved kolon. Legger så til objektene i sanger
    def lesFraFil(self, filnavn):
        filnavn = open(filnavn, "r")
        for linje in filnavn:
            tittel, artist = linje.strip().split(";")
            self._sanger.append(Sang(artist, tittel))
        filnavn.close()

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)

    def spillSang(self, sang):
        sang.spill()

    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    # her går vi gjennom sangene og ser om tittel oppgitt finnes i en sang i spillelisten
    def finnSang(self, tittel):
            for i in self._sanger:
                if i.sjekkTittel(tittel):
                    return i
            return None

    # tar imot et artistnavn, lager lise og sjekker alle sanger i spilleliste.
    # returnerer alle sanger til gitt artist hvis True
    def hentArtistUtvalg(self, artistnavn):
        utvalg = []
        for i in self._sanger:
            if i.sjekkArtist(artistnavn):
                utvalg.append(i)
        return utvalg