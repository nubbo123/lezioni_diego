# Soluzioni degli Esercizi Python per Principianti
# Qui trovi le soluzioni complete e commentate di tutti gli esercizi

# =============== Esercizio 1: Saluto Personalizzato ===============
print("\n=== Soluzione Esercizio 1 ===")
# Chiediamo il nome all'utente usando input()
nome = input("Come ti chiami? ")
# Usiamo una f-string per inserire il nome nel messaggio
print(f"Ciao {nome}! Benvenuto nel mondo della programmazione!")


# =============== Esercizio 2: Convertitore di Temperatura ===============
print("\n=== Soluzione Esercizio 2 ===")
# Convertiamo l'input in float per gestire i numeri decimali
celsius = float(input("Inserisci la temperatura in Celsius: "))
# Applichiamo la formula di conversione
fahrenheit = (celsius * 9/5) + 32
# Stampiamo il risultato
print(f"{celsius}°C equivalgono a {fahrenheit}°F")


# =============== Esercizio 3: Area del Rettangolo ===============
print("\n=== Soluzione Esercizio 3 ===")
# Chiediamo le dimensioni e le convertiamo in float
base = float(input("Inserisci la base del rettangolo: "))
altezza = float(input("Inserisci l'altezza del rettangolo: "))
# Calcoliamo l'area
area = base * altezza
print(f"L'area del rettangolo è: {area}")


# =============== Esercizio 4: Pari o Dispari ===============
print("\n=== Soluzione Esercizio 4 ===")
# Convertiamo l'input in intero
numero = int(input("Inserisci un numero: "))
# Usiamo l'operatore modulo (%) per trovare il resto della divisione per 2
if numero % 2 == 0:  # Se il resto è 0, il numero è pari
    print(f"Il numero {numero} è pari")
else:
    print(f"Il numero {numero} è dispari")


# =============== Esercizio 5: Somma dei Primi N Numeri ===============
print("\n=== Soluzione Esercizio 5 ===")
# Chiediamo fino a che numero sommare
n = int(input("Fino a che numero vuoi sommare? "))
somma = 0  # Inizializziamo la variabile somma a 0
# Usiamo un ciclo for per sommare i numeri da 1 a n
for i in range(1, n + 1):  # range(1, n+1) genera numeri da 1 a n
    somma += i  # Aggiungiamo ogni numero alla somma
print(f"La somma dei primi {n} numeri è: {somma}")


# =============== Esercizio 6: Lista della Spesa ===============
print("\n=== Soluzione Esercizio 6 ===")
# Creiamo una lista vuota
lista_spesa = []
# Usiamo un ciclo while per chiedere prodotti finché l'utente non scrive 'fine'
while True:
    item = input("Aggiungi un prodotto alla lista (o scrivi 'fine' per terminare): ")
    if item.lower() == 'fine':  # Convertiamo in minuscolo per accettare anche 'FINE' o 'Fine'
        break  # Usciamo dal ciclo
    lista_spesa.append(item)  # Aggiungiamo il prodotto alla lista

# Stampiamo la lista numerata usando enumerate
print("\nLa tua lista della spesa:")
for i, prodotto in enumerate(lista_spesa, 1):  # enumerate(lista, 1) parte a numerare da 1
    print(f"{i}. {prodotto}")


# =============== Esercizio 7: Indovina il Numero ===============
print("\n=== Soluzione Esercizio 7 ===")
import random  # Importiamo il modulo random per generare numeri casuali

# Generiamo un numero casuale tra 1 e 10
numero_segreto = random.randint(1, 10)
tentativi = 0  # Contatore dei tentativi
indovinato = False  # Flag per tenere traccia se il numero è stato indovinato

# Diamo all'utente 3 tentativi
while not indovinato and tentativi < 3:
    guess = int(input("Indovina il numero (tra 1 e 10): "))
    tentativi += 1
    
    if guess == numero_segreto:
        print(f"Complimenti! Hai indovinato in {tentativi} tentativi!")
        indovinato = True
    elif guess < numero_segreto:
        print("Troppo basso!")
    else:
        print("Troppo alto!")

# Se non ha indovinato dopo 3 tentativi
if not indovinato:
    print(f"Mi dispiace! Il numero era {numero_segreto}") 