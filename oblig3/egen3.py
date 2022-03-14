# Oppgave 5

# Lag et program som sjekker om du svarer riktig eller galt på 4 spørsmål. Det er mulig å få 4 poeng dersom alle svar er korrekt.
# Det skal gis minuspoeng for galt svar og plusspoeng for riktig svar.
# Variabelen score holder telling på antall poeng

# Spørsmålene skal lagres i en liste av lister og svaralternativene i en liste av lister.
# Print ut spørsmålene og svaralternativer

# Definer quizen i en egen funksjon som heter quiz.


# Her har vi en liste med fire lister for spørsmål
quizSpm = [
    ["Hva har du laget hvis du lager Béchamel?"],
    ["Hvilket av disse alternativene er ikke en druetype?"],
    ["Hvilket land serverer de ofte 'Pico de Gallo'?"],
    ["Hva er nasjonalretten i USA?"]
]
# svarene lagrer vi også i en egen liste med lister
quizSvar = [
    ["A: En saus", "B: En suppe", "C: En gryte"],
    ["A: Chardonnay", "B: Merlot", "C: Azur"],
    ["A: Mexico", "B: Spania", "C: Italia"],
    ["A: Hot dog", "B: Brisket", "C: Hamburger", "D: Fritert kylling"]
]

# Funksjon for selve quizen
def quiz():
    score = 0
    # Her ønsker vi å printe ut første spørsmål. Vi må da indexe første rad, som er 0
    print(quizSpm[0])
    # vi vil ha allle svaralternativene til første spørsmål, vi indexer da hele den første raden i quizSvar
    print(quizSvar[0])
    # input fra bruker legges til i variabel svar.
    svar = input().upper()
    # hvis svar er "a", som er riktig, får bruker 1 poeng. Alle andre input her gir minuspoeng, dette er nok ikke ideelt.
    if svar == "A":
        score = score + 1
    else:
        score = score - 1

    # vi gjentar for andre spørsmål
    print(quizSpm[1])
    print(quizSvar[1])
    svar = input().upper()
    if svar == "C":
        score = score + 1
    else:
        score = score - 1

    # tredje spørsmål
    print(quizSpm[2])
    print(quizSvar[2])
    svar = input().upper()
    if svar == "A":
        score = score + 1
    else:
        score = score - 1

    # fjerde spørsmål
    print(quizSpm[3])
    print(quizSvar[3])
    svar = input().upper()
    if svar == "C":
        score = score + 1
    else:
        score = score - 1

    # quizen er ferdig og bruker får score
    print("Din score ble: ", score)

# kall funksjon og kjør quizen
quiz()
