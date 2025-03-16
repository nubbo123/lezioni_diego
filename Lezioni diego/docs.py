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