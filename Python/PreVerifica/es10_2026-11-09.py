from threading import Thread
import random

lavanderia = []

class Lavatrice(Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.Ciclo_Lavaggio = random.randint(3,6)
    def run(self):
        print(f"{self.id} inizia il lavoro lavatrice")
        for a in range (self.Ciclo_Lavaggio):
            print(f"{self.id} sta lavando")
        print(f"{self.id} ha finito di lavare")

def Avvia_Lavatrici(lista_lavatrici):
    for x in lista_lavatrici:
        x.start()
l1 = Lavatrice("lav1")
l2 = Lavatrice("lav2")
l3 = Lavatrice("lav3")
l4 = Lavatrice("lav4")

lavanderia.append(l1)
lavanderia.append(l2)
lavanderia.append(l3)
lavanderia.append(l4)

Avvia_Lavatrici(lavanderia)
