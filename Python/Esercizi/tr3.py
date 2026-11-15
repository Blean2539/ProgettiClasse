import threading, random, time
from threading import Thread

class Pizza():
    def __init__(self, nome, costo, tempo):
        self.nome = nome
        self.costo = costo
        self.tempo = tempo

    def __str__(self):
        return self.nome
class Pizzaiolo(Thread):
    def __init__(self, nome_pizzaiolo):
        super().__init__()
        self.nome_pizzaiolo = nome_pizzaiolo
        self.ordini_assegnati = []
    def run(self):
        for pizza in self.ordini_assegnati:
            print(f"{self.nome_pizzaiolo} sta preparando {pizza}")
            for secondo_trascorso in range(pizza.tempo):
                print(f"{self.nome_pizzaiolo} sta impastando {pizza} da {secondo_trascorso+1} secondi ({pizza.tempo-secondo_trascorso}/{pizza.tempo})")
                time.sleep(1)
            print(f"{self.nome_pizzaiolo} ha finito di preparare {pizza}")
def main():
    Pizzaioli = [Pizzaiolo("Scoccianti"), Pizzaiolo("Fiore"), Pizzaiolo("Pakistano")]
    Pizze = [
        Pizza("Margherita", 5, 10),
        Pizza("Diavola", 6, 15),
        Pizza("Capricciosa", 7, 13),
        Pizza("Quattro Formaggi", 8, 4)
    ]
    for _ in range(10):
        random.choice(Pizzaioli).ordini_assegnati.append(random.choice(Pizze))

    for pizzaiolo in Pizzaioli:
        pizzaiolo.start()
    for pizzaiolo in Pizzaioli:
        pizzaiolo.join()

    print("Tutte le pizze sono state preparate")
    print(f"Totale pizze preparate: {sum([len(pizzaiolo.ordini_assegnati) for pizzaiolo in Pizzaioli])}")
if __name__ == "__main__":
    main()
