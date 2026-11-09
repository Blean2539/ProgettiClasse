import time  # Importo il modulo del tempo nel Mondo Principale

lista_giocatori = []
loop = True
scelta = 0
numero = 0

class Squadra:
    def __init__(self, lista_giocatori):
        self.lista_giocatori = lista_giocatori

    def aggiungi_giocatore(self, giocatore):
        # Prende direttamente il nome passato dal menu principale
        self.lista_giocatori.append(giocatore)
        print(f"giocatore {giocatore} aggiunto alla squadra")

    def mostra_giocatori(self, lista_giocatori):
        for i in lista_giocatori:
            print(i)

    def numero_giocatori(self, lista_giocatori):
        numero = len(lista_giocatori)
        return numero

squadra = Squadra(lista_giocatori)

while loop == True:
    scelta = int(input("\n1. aggiungi giocatore \n2. mostra giocatori \n3. numero giocatori \n4. esci \n-> Seleziona: "))

    if scelta == 1:
        nome_g = input(f"inserire nome giocatore n°{numero+1}: ")
        squadra.aggiungi_giocatore(nome_g)
        # Aggiorniamo il numero totale dei giocatori
        numero = len(squadra.lista_giocatori)

    elif scelta == 2:
        print("Giocatori presenti:")
        squadra.mostra_giocatori(squadra.lista_giocatori)

    elif scelta == 3:
        numero = squadra.numero_giocatori(squadra.lista_giocatori)
        print(f"Numero Giocatori attuale pari a: {numero}")

    elif scelta == 4:
        loop = False
        print("Chiusura Programma")
        time.sleep(0.08)
        print(".")
        time.sleep(0.08)
        print("..")
        time.sleep(0.08)
        print("...")
        time.sleep(0.16)
        print("done")
