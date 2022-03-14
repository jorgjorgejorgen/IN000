# Oppgave 3

# Her får vi False fordi fruktmengde ikke er lik fruktliste. Dette fordi fruktmengde, som er en ordbok kun regner en oppføring av nøkkelverdien, selv om banan og eple er oppført flere ganger i ordboken.
fruktliste = ["eple", "eple", "banan", "banan", "banan"]
fruktmengde = {"eple", "eple", "banan", "banan", "banan"}
print(len(fruktliste) == len(fruktmengde))

# ny ordliste med frukt som nøkkel og antall som verdi
frukt_dict = {
    "eple": 2, "banan": 3
}
# her gjør vi nøyaktig som i oppgave 2
frukt = input("Hvilken frukt vil du legge til i listen? ").lower()
# sørge for at antall er int så vi kan regne
antall = int(input("Hvor mange har du? "))

# hvis antall skrevet inn er mindre enn 0
if antall < 0:
    print("Ugyldig input")
# hvis frukten ikke finnes i frukt_dict
if frukt not in frukt_dict:
    # vi må lagre frukt som key og antall som tilhørende verdi
    frukt_dict[frukt] = antall
# hvis frukten finnes allerede, må vi passe på å oppdatere antall
elif frukt in frukt_dict:
    print("Finnes fra før. Oppdaterer antall")
    # key er den samme, men vi må legge til og oppdatere antall
    frukt_dict[frukt] = frukt_dict[frukt] + antall

print(frukt_dict)