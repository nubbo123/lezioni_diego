# =============== Esercizio 4 ===============
# Scrivi un programma che determini se un numero è pari o dispari
# Suggerimento: usa l'operatore % (modulo) per trovare il resto della divisione per 2

def is_even (number):
    if number % 2 == 0:
        return True
    else :
        return False


numero_ignoto = int(input())
if is_even(numero_ignoto):
    print("The number is even!")
else :
    print("The number is odd!")
    

