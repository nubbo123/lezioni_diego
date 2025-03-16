# =============== Esercizio 3 ===============
# Scrivi un programma che calcoli l'area di un rettangolo
# Formula: base × altezza
# Suggerimento: chiedi all'utente base e altezza

def area_rettangolo(a,b):
    return(a*b)


richiesta_base = int(input("Dimmi la base: \n"))
richiesta_altezza = int(input("Dimmi l'altezza: \n"))


risultato=area_rettangolo(richiesta_altezza,richiesta_base)
print("l'area del rettangolo è:",risultato)
    