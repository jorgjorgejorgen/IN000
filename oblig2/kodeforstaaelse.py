heltallSomTekst = input( "Tast inn et heltall! " )
heltall = int( heltallSomTekst )
if heltall < 10:
    print ( heltall + "Hei!" )


# a)
# Programmet vil nok ikke kunne kjøre, fordi vi forsøker å slå sammen en tekststreng med et heltall i if-testen.

# b)
# Input er en tekststreng, denne konverteres så til et heltall så det er mulig å regne.
# Dette kan gi problemer når vi skal slå samen heltall og tekststreng i linje 4.
# I og med at variabelen heltall er et tall, vil programmet forsøke å regne når vi skal slå sammen med tekststreng "Hei" hvis if-testen er gyldig.
# Programmet vil da ikke kunne kjøre. En mulighet er å bytte + med , i linje 4 så variabel 'heltall' og "Hei" kan printes om 'heltall' er mindre enn 10.
# Vi kan også forenkle programmet med å fjerne 'heltall', og heller sørge for at 'heltallSomTekst' er et tall: int(input))