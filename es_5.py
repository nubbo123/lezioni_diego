# =============== Esercizio 5 ===============
# Scrivi un programma che calcoli la somma dei primi N numeri
# Esempio: se N = 5, calcola 1 + 2 + 3 + 4 + 5
# Suggerimento: usa un ciclo for e range()

# for numero in range(1,12):
#   print(numero)

def somma_1_to_N (numero):
    somma = 0
    iterazione = 1
    for n in range(1,numero+1):
        somma = somma+n
        print(f"Somma:{somma}, Iter:{iterazione}, n:{n}")
#stessa cosa sarebbe print(somma)
        iterazione = iterazione+1
    return somma

        

numero_N = int(input("Dimmi il numero"))
somma = somma_1_to_N(numero_N)
print (somma)


