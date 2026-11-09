import time  # Importo il modulo del tempo nel Mondo Principale

# Inizializzo le variabili nel MONDO PRINCIPALE.
# Mettere 'n = 0' qui fa nascere la variabile fin da subito:
# serve a zittire il Guardiano (Pyright) ed evitare il solito avviso "PossiblyUnboundVariable"
# nel ciclo di countdown più in basso.
n = 0
valido = False

# --- SOTTO-MONDO 1: CICLO DI VALIDAZIONE ---
# Entro nel ciclo finché la variabile valido rimane False
while valido == False:
    print("inserire un valore intero positivo")

    # Prendo l'input dall'utente e lo salvo nella variabile 'n' (convertito in float per i controlli)
    n = float(input())

    # Controllo se il numero è intero e positivo:
    # 1) n >= 0 garantisce che non sia negativo
    # 2) (n - int(n)) == 0 verifica che non ci sia parte decimale
    if n >= 0 and (n - int(n)) == 0:
        n = int(n)     # Converto n in un intero pulito
        valido = True  # Cambio il semaforo a True per spezzare il ciclo e uscire dal sotto-mondo
    else:
        print("ce la fai a fare quello che ti si chiene ripeto INTERO E POSITIVO...")

# --- RITORNO AL MONDO PRINCIPALE ---
print("il valore inserito è positivo intero")
print("inizio del countdown")

# --- SOTTO-MONDO 2: CICLO DEL COUNTDOWN ---
# Ora il ciclo usa la variabile 'n' già convalidata dal sotto-mondo precedente.
# Essendo 'n' nata nel Mondo Principale all'inizio del file, Pyright non si lamenta più.
while n >= 0:
    print(n)          # Stampo il valore corrente
    n = n - 1         # Decremento di 1
    time.sleep(0.08)  # Metto in pausa il programma per 80 millisecondi (0.08s) ad ogni ciclo
