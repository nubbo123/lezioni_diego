# =============== Esercizio 2 ===============
# Scrivi un programma che converta i gradi Celsius in Fahrenheit
# Formula: (°C × 9/5) + 32 = °F
# Suggerimento: usa float() per convertire l'input in numero decimale

def conv_C_to_F(a):
    return(a*9/5 + 32)

numero_celsius = float(input())
risultato= conv_C_to_F(numero_celsius)


print(risultato)
