dag1 = input('Skriv inn første dag ')
mnd1 = input('Skriv inn første måned ')
# skriv ut dato 1
print(dag1 + '.' + mnd1)

dag2 = input('Skriv inn siste dag ')
mnd2 = input('Skriv inn siste måned ')
# skriv ut dato 2
print(dag2 + '.' + mnd2)

# hvis første mnd er mindre eller lik andre mnd, og første dag da er mindre enn andre dag
if (mnd1 < mnd2) or (mnd1 == mnd2 and dag1 < dag2):
    print("Riktig rekkefølge!")
# hvis første mnd er større eller lik andre mnd og første dag også er mindre enn andre dag
elif (mnd1 > mnd2) or (mnd1 == mnd2 and dag1 > dag2):
    print ("Feil rekkefølge!")
else:
    print ("Samme dato!")