# Oppgave 3

liste = []
minSum = 0
# krever et tall fra bruker
tall = int(input("Skriv inn et tall: "))
# mens tall input ikke er 0
while tall != 0:
    # legg til tall i tom liste og be om ny input
    liste.append(tall)
    tall = int(input("Skriv inn tall: "))
else:
    print("Tallet er null")

# printer alle tall i lista
for i in liste:
   print("Listen inneholder tallet: ", i)

# summerer tall med neste tall
for i in liste:
    minSum += i
    print("Tall pluss forrige tall er:", minSum)

# minste tall i listen
tallSjekk = liste[0]
for i in liste:
    if i < tallSjekk:
        tallSjekk = i
print("Det minste tallet i listen er: ", tallSjekk)

# største tall
for i in liste:
    if i > tallSjekk:
        tallSjekk = i
print("Det største tallet i listen er: ", tallSjekk)


