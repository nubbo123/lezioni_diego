# Documentazione delle Funzioni Python
# Questo file contiene la spiegazione di tutte le funzioni utilizzate negli esercizi

# =============== Funzioni di Input/Output ===============

# print() - Stampa un messaggio a schermo
"""
Descrizione: Mostra testo o valori sulla console
Sintassi: print(valore1, valore2, ...)
Esempio:
"""
nome = "Mario"
età = 25
print("Base:")
print("Ciao")  # Stampa: Ciao
print("Con variabili:")
print("Mi chiamo", nome, "e ho", età, "anni")  # Stampa: Mi chiamo Mario e ho 25 anni
print("\nCon f-string:")
print(f"Mi chiamo {nome} e ho {età} anni")  # Stampa: Mi chiamo Mario e ho 25 anni


# input() - Legge input dall'utente
"""
Descrizione: Permette di ricevere input dall'utente tramite tastiera
Sintassi: input(messaggio)
Esempio:
"""
print("\n=== input() ===")
nome = input("Come ti chiami? ")  # L'utente può inserire il suo nome
print(f"Hai inserito: {nome}")


# =============== Funzioni di Conversione ===============

# int() - Converte in numero intero
"""
Descrizione: Converte un valore in un numero intero
Sintassi: int(valore)
Esempio:
"""
print("\n=== int() ===")
numero_stringa = "123"
numero_intero = int(numero_stringa)  # Converte "123" in 123
print(f"Stringa '{numero_stringa}' convertita in intero: {numero_intero}")


# float() - Converte in numero decimale
"""
Descrizione: Converte un valore in un numero decimale
Sintassi: float(valore)
Esempio:
"""
print("\n=== float() ===")
prezzo_stringa = "19.99"
prezzo_float = float(prezzo_stringa)  # Converte "19.99" in 19.99
print(f"Stringa '{prezzo_stringa}' convertita in float: {prezzo_float}")


# str() - Converte in stringa
"""
Descrizione: Converte un valore in una stringa
Sintassi: str(valore)
Esempio:
"""
print("\n=== str() ===")
numero = 42
numero_stringa = str(numero)  # Converte 42 in "42"
print(f"Numero {numero} convertito in stringa: '{numero_stringa}'")


# =============== Funzioni per Liste ===============

# len() - Calcola la lunghezza
"""
Descrizione: Restituisce il numero di elementi in una sequenza (lista, stringa, ecc.)
Sintassi: len(sequenza)
Esempio:
"""
print("\n=== len() ===")
lista = [1, 2, 3, 4, 5]
testo = "Ciao"
print(f"Lunghezza lista {lista}: {len(lista)}")  # Stampa: 5
print(f"Lunghezza testo '{testo}': {len(testo)}")  # Stampa: 4


# sum() - Calcola la somma
"""
Descrizione: Calcola la somma di tutti gli elementi in una sequenza numerica
Sintassi: sum(sequenza)
Esempio:
"""
print("\n=== sum() ===")
numeri = [10, 20, 30, 40]
somma = sum(numeri)
print(f"Somma dei numeri {numeri}: {somma}")  # Stampa: 100


# append() - Aggiunge elemento alla lista
"""
Descrizione: Aggiunge un elemento alla fine di una lista
Sintassi: lista.append(elemento)
Esempio:
"""
print("\n=== append() ===")
frutti = ["mela", "pera"]
print(f"Lista originale: {frutti}")
frutti.append("banana")
print(f"Lista dopo append: {frutti}")


# =============== Funzioni per Stringhe ===============

# lower() - Converte in minuscolo
"""
Descrizione: Converte una stringa in lettere minuscole
Sintassi: stringa.lower()
Esempio:
"""
print("\n=== lower() ===")
testo = "CIAO Mondo!"
print(f"Originale: {testo}")
print(f"Minuscolo: {testo.lower()}")


# join() - Unisce stringhe
"""
Descrizione: Unisce elementi di una sequenza usando una stringa come separatore
Sintassi: separatore.join(sequenza)
Esempio:
"""
print("\n=== join() ===")
parole = ["Python", "è", "fantastico"]
frase = " ".join(parole)
print(f"Lista parole: {parole}")
print(f"Frase unita: {frase}")


# =============== Moduli e Funzioni Importate ===============

# random.choice() - Scelta casuale
"""
Descrizione: Seleziona un elemento casuale da una sequenza
Sintassi: random.choice(sequenza)
Esempio:
"""
print("\n=== random.choice() ===")
import random
colori = ["rosso", "verde", "blu"]
scelta = random.choice(colori)
print(f"Colore scelto casualmente da {colori}: {scelta}")


# string.ascii_letters - Lettere dell'alfabeto
"""
Descrizione: Contiene tutte le lettere dell'alfabeto (maiuscole e minuscole)
Esempio:
"""
print("\n=== string.ascii_letters ===")
import string
print(f"Lettere disponibili: {string.ascii_letters}")


# string.digits - Cifre numeriche
"""
Descrizione: Contiene tutte le cifre da 0 a 9
Esempio:
"""
print("\n=== string.digits ===")
print(f"Cifre disponibili: {string.digits}")


# =============== Operatori Speciali ===============

# // (Divisione intera)
"""
Descrizione: Esegue una divisione restituendo solo la parte intera
Sintassi: numero1 // numero2
Esempio:
"""
print("\n=== Divisione intera (//) ===")
minuti = 90
ore = minuti // 60
print(f"{minuti} minuti diviso 60 = {ore} ore (parte intera)")


# % (Modulo - Resto della divisione)
"""
Descrizione: Restituisce il resto di una divisione
Sintassi: numero1 % numero2
Esempio:
"""
print("\n=== Modulo (%) ===")
minuti_resto = 90 % 60
print(f"90 minuti modulo 60 = {minuti_resto} minuti (resto)")


# [::-1] (Slice inverso)
"""
Descrizione: Inverte una sequenza
Sintassi: sequenza[::-1]
Esempio:
"""
print("\n=== Slice inverso [::-1] ===")
parola = "Python"
print(f"Parola originale: {parola}")
print(f"Parola invertita: {parola[::-1]}")


# =============== Strutture di Controllo: Cicli ===============

# for con range() - Ciclo con contatore
"""
Descrizione: Esegue un ciclo per un numero specifico di volte
Sintassi: for variabile in range(start, stop, step)
Note: 
- start: valore iniziale (opzionale, default 0)
- stop: valore finale (escluso)
- step: incremento (opzionale, default 1)
Esempio:
"""
print("\n=== for con range() ===")
print("Contare da 1 a 5:")
for i in range(1, 6):  # 6 è escluso
    print(f"Numero: {i}")

print("\nContare di 2 in 2:")
for i in range(0, 10, 2):  # da 0 a 9 con passo 2
    print(f"Numero: {i}")


# for con lista - Ciclo su elementi
"""
Descrizione: Esegue un ciclo su ogni elemento di una sequenza
Sintassi: for elemento in sequenza
Esempio:
"""
print("\n=== for con lista ===")
animali = ["gatto", "cane", "coniglio"]
for animale in animali:
    print(f"Animale: {animale}")


# for con enumerate() - Ciclo con indice
"""
Descrizione: Esegue un ciclo su una sequenza fornendo sia l'indice che il valore
Sintassi: for indice, valore in enumerate(sequenza, start=0)
Note: start è opzionale e definisce da che numero iniziare a contare
Esempio:
"""
print("\n=== for con enumerate() ===")
frutta = ["mela", "pera", "banana"]
print("Lista numerata da 1:")
for indice, frutto in enumerate(frutta, 1):  # inizia a contare da 1
    print(f"{indice}. {frutto}")


# while - Ciclo con condizione
"""
Descrizione: Esegue un ciclo finché una condizione rimane vera
Sintassi: while condizione:
Esempio:
"""
print("\n=== while ===")
print("Conto alla rovescia:")
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Via!")


# break e continue - Controllo del flusso nei cicli
"""
Descrizione: 
- break: esce immediatamente dal ciclo
- continue: salta alla prossima iterazione
Esempio:
"""
print("\n=== break e continue ===")
print("Esempio break:")
for i in range(1, 6):
    if i == 4:
        break
    print(f"Numero: {i}")
print("Ciclo interrotto al 4")

print("\nEsempio continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"Numero: {i}")
print("Il numero 3 è stato saltato")


# while True con break - Ciclo infinito controllato
"""
Descrizione: Crea un ciclo che continua finché non viene esplicitamente interrotto
Sintassi: while True:
Esempio:
"""
print("\n=== while True con break ===")
print("Esempio di input con possibilità di uscita:")
while True:
    risposta = input("Scrivi qualcosa (o 'esci' per terminare): ")
    if risposta.lower() == 'esci':
        print("Programma terminato")
        break
    print(f"Hai scritto: {risposta}") 