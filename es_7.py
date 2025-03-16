# =============== Esercizio 7 ===============
# Scrivi un programma che faccia indovinare un numero tra 1 e 10
# Il programma deve:
# - Generare un numero casuale
# - Dare all'utente 3 tentativi
# - Dire se il tentativo è troppo alto o troppo basso
# Suggerimento: importa il modulo random e usa random.randint(1, 10) 

import random

numero_randomico = random.randint(1,10)

for n in range(1,4):
    tentativo = int(input(f"Indovina il numero,tentativo n{n}\n"))
    if numero_randomico == tentativo:
        print("Hai indovinato")
        break
    elif numero_randomico < tentativo:
        print("Il tuo tentativo è maggiore del numero da indovinare,ritenta \n")
    else :
        print("Il tuo tentativo è minore del numero da indovinare\n")
    if n==3 :
        print(f"Non hai indovinato :(), il numero era{numero_randomico}")

    




    

