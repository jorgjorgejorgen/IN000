# Oppgave 2

#Opprett ordboka med følgende varer med tilhørende pris: melk - kr 14.90, brød - kr
#24.90, yoghurt - 12.90 og pizza - 39.90. Skriv ut innholdet i ordboken med en enkel
#print-setning.

matvarer = {"melk": 14.90,
            "brød": 24.90,
            "yoghurt": 12.90,
            "pizza": 39.90
            }
print(matvarer)

# legger til ny nøkkelverdi i ordboka basert på input
vare = input("Hva er varen: ").lower()
# tilegner verdi til nøkkelen
varePris = input("Hva koster varen?: ")
# lagrer nøkkel i dict og tilegner varePris som verdi
matvarer[vare] = varePris
print(matvarer)

# et problem her er hvis den nye varen har sammen navn som eksisterende vare.

