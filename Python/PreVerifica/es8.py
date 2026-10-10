lista_giocatori = []
loop = True
scelta = 0
numero = 0

class Squadra:
    def __init__(self, lista_giocatori):
        self.lista_giocatori = lista_giocatori

    def aggiungi_giocatore(self, giocatore):
        giocatore = input("inserisci il nome del giocatore: ")
        self.lista_giocatori.append(giocatore)
        print(f"giocatore {giocatore} aggiunto alla squadra")
    def mostra_giocatori(self, lista_giocatori):
        for i in lista_giocatori:
            print(i)
    def numero_giocatori (self, lista_giocatori):
      numero = len(lista_giocatori)
      return numero

squadra = Squadra(lista_giocatori)

while loop == True:
    scelta = int(input("\n1. aggiungi giocatore \n2. mostra giocatori \n3. numero giocatori \n4. esci \n-> Seleziona: "))

    if scelta == 1:
        print("1")

    elif scelta == 2:
         print("2")
    elif scelta == 3:
        numero = squadra.numero_giocatori()
        print(numero)
    elif scelta == 4:
        print("4")
