# --- MONDO PRINCIPALE ---
# Dichiaro e inizializzo le variabili nel Mondo Principale
# per garantire al Guardiano (Pyright) che esistano prima di ogni blocco
print("insierire l'intestatario e il saldo iniziale")
intestatario = input("inserisci l'intestatario: ")
saldo = int(input("inserisci il saldo iniziale: "))
loop = True
importo = 0


# --- DEFINIZIONE DELLA CLASSE ---
# Uso CamelCase 'ContoBancario' per conformità alla traccia
class ContoBancario:
    def __init__(self, intestatario, saldo):
        self.intestatario = intestatario
        self.saldo = saldo

    # Metodo per il deposito
    def deposita(self, importo):
        self.saldo += importo
        print(f"depositato con successo: {importo}")

    # Metodo per il prelievo con blocco se il saldo va sotto zero
    def preleva(self, importo):
        if self.saldo - importo >= 0:
            self.saldo -= importo
            print(f"prelevato con successo: {importo}")
        else:
            print("saldo insufficiente")

    # Metodo per mostrare il saldo attuale
    def mostra_saldo(self):
        print(f"saldo: {self.saldo}")


# --- CREAZIONE OGGETTO NEL MONDO PRINCIPALE ---
conto = ContoBancario(intestatario, saldo)


# --- SOTTO-MONDO: CICLO INTERATTIVO ---
while loop == True:
    print("\n1. deposita \n2. preleva \n3. mostra saldo \n4. esci")
    scelta = int(input("seleziona l'opzione: "))

    if scelta == 1:
        importo = int(input("scrivere importo: "))
        conto.deposita(importo)

    elif scelta == 2:
        importo = int(input("scrivere importo: "))
        conto.preleva(importo)

    elif scelta == 3:
        conto.mostra_saldo()

    elif scelta == 4:
        loop = False  # Spezzo il ciclo per uscire dal sotto-mondo

    else:
        print("scelta non valida")
