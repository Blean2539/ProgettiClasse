import random
from threading import Thread

Lavanderia = []


class Lavatrice(Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.Ciclo_Lavaggio = random.randint(3,6)

    def Run(self):
        print(f"Lavatrice : {self.id} ha iniziato il ciclo di lavaggio di {self.Ciclo_Lavaggio} Minuti")
        for a in range(self.Ciclo_Lavaggio):
            print(f"Lavatrice {self.id} sta lavando...{a+1} / {self.Ciclo_Lavaggio}")
        print(f"Lavatrice {self.id} ha completato il ciclo del lavaggio")

def Avvia_Lavatrici(lista):
    for lavatrice in lista:
        lavatrice.start()


Lavatrice1 = Lavatrice("l1")
Lavatrice2 = Lavatrice("l2")
Lavatrice3 = Lavatrice("l3")
Lavatrice4 = Lavatrice("l4")

Lavanderia.append(Lavatrice1)
Lavanderia.append(Lavatrice2)
Lavanderia.append(Lavatrice3)
Lavatrice.append(Lavatrice4)


Avvia_Lavatrici(Lavanderia)
