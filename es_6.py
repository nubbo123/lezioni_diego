# =============== Esercizio 6 ===============
# Scrivi un programma che crei una lista della spesa
# Il programma deve:
# - Chiedere prodotti all'utente finché non scrive 'fine'
# - Mostrare la lista numerata alla fine
# Suggerimento: usa una lista e un ciclo while

lista_spesa = []


while True :
    alimento_spesa = input("Elenca gli alimenti.\n")
    if alimento_spesa.lower()=="fine":
        break
    lista_spesa.append(alimento_spesa)


print("\n La tua lista della spesa: ")
for i,prodotto in enumerate(lista_spesa,1):
    print(f"{i}. {prodotto}")


