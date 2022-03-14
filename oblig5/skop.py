# Oppgave 3

# Vi definerer først funksjonen minFunksjon som ikke tar noen parametere. Så defineres prosedyren hovedprogram, også uten parametere.Hovedprogram kjøres. a blir definert 42, b definert 0, vi printer b. Variabel a blir satt til samme verdi som variabel b.

# minFunksjon kalles, mens b fortsatt er 42. En for-løkke kjører to ganger. Varibel c er satt til 2. Dette printes. Vi plusser så c med 1, c er nå 3. b blir satt til 10, deretter blir b satt til b + a. a er en lokal variabel (42) i hovedprogram og ikke tilgjengelig i minFunksjon. Vi får error på dette.


# Vi kan forklare flyten slik:
# hovedprogram:
    # a er 42, b er 0
    # print b
    #b er 42
    #a er 42, kjør minFunksjon()
# minFunksjon:
# loop to ganger:
    # c er 2
    # print c som er 2
    # !error a er lokal variabel i hovedprogram(vi løser dette med å sette a som global variabel)
    # c er 3, b er 52
    # print b
    # c er 2
    # print c som er 2
    # c er 3, b er 52
    # print b som er 52
# slutt loop
# hovedprogram:
    # b er 42
    # print b
    # print a





