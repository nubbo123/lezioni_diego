# Soluzioni degli Esercizi Python per Principianti - Serie 2
# Qui trovi le soluzioni complete e commentate di tutti gli esercizi

# =============== Esercizio 1: Calcolatore di Media ===============
print("\n=== Soluzione Esercizio 1 ===")
# Creiamo una lista vuota per i numeri
numeri = []
# Chiediamo 5 numeri all'utente
for i in range(5):
    numero = float(input(f"Inserisci il {i+1}° numero: "))
    numeri.append(numero)
# Calcoliamo la media
media = sum(numeri) / len(numeri)
print(f"La media dei numeri inseriti è: {media}")


# =============== Esercizio 2: Contatore di Vocali ===============
print("\n=== Soluzione Esercizio 2 ===")
# Chiediamo la parola all'utente
parola = input("Inserisci una parola: ").lower()  # Convertiamo in minuscolo
vocali = "aeiou"
contatore = 0
# Contiamo le vocali
for lettera in parola:
    if lettera in vocali:
        contatore += 1
print(f"La parola '{parola}' contiene {contatore} vocali")


# =============== Esercizio 3: Generatore di Password ===============
print("\n=== Soluzione Esercizio 3 ===")
import random
import string
# Creiamo le stringhe di caratteri possibili
lettere = string.ascii_letters  # Lettere maiuscole e minuscole
numeri = string.digits  # Numeri da 0 a 9
# Generiamo la password
caratteri = lettere + numeri
password = ''.join(random.choice(caratteri) for i in range(8))
print(f"Password generata: {password}")


# =============== Esercizio 4: Convertitore di Tempo ===============
print("\n=== Soluzione Esercizio 4 ===")
# Chiediamo i minuti all'utente
minuti_totali = int(input("Inserisci il numero di minuti: "))
# Calcoliamo ore e minuti
ore = minuti_totali // 60  # Divisione intera per trovare le ore
minuti = minuti_totali % 60  # Resto per trovare i minuti rimanenti
print(f"{minuti_totali} minuti equivalgono a {ore} ore e {minuti} minuti")


# =============== Esercizio 5: Calcolatore di Sconto ===============
print("\n=== Soluzione Esercizio 5 ===")
# Chiediamo prezzo e sconto
prezzo_originale = float(input("Inserisci il prezzo originale: "))
sconto_percentuale = float(input("Inserisci la percentuale di sconto: "))
# Calcoliamo il prezzo scontato
sconto = sconto_percentuale / 100
prezzo_scontato = prezzo_originale * (1 - sconto)
print(f"Il prezzo scontato è: {prezzo_scontato:.2f} €")


# =============== Esercizio 6: Tabellina ===============
print("\n=== Soluzione Esercizio 6 ===")
# Chiediamo il numero all'utente
numero = int(input("Di quale numero vuoi vedere la tabellina? "))
# Stampiamo la tabellina
print(f"\nTabellina del {numero}:")
for i in range(1, 11):
    risultato = numero * i
    print(f"{numero} x {i} = {risultato}")


# =============== Esercizio 7: Palindromo ===============
print("\n=== Soluzione Esercizio 7 ===")
# Chiediamo la parola all'utente
parola = input("Inserisci una parola: ").lower()  # Convertiamo in minuscolo
# Verifichiamo se è palindroma
# Confrontiamo la parola con la sua versione invertita
if parola == parola[::-1]:  # [::-1] inverte la stringa
    print(f"'{parola}' è palindroma!")
else:
    print(f"'{parola}' non è palindroma.") 