import threading, time
from threading import Thread
from datetime import date, datetime


orologaio = []

class Orologio(Thread):
    def __init__(self, nome_orologio):
        super().__init__()
        self.nome_orologio = nome_orologio
        self.ora = datetime.now()

    def run(self):
        c = 3
        while c != 0:
            self.ora = datetime.now()
            print(f"{self.nome_orologio} : {self.ora}")
            time.sleep(2)
            c -= 1
        print(f"{self.nome_orologio} ha terminato il suo ciclo.")

def avviaOrologi(lista_orologi):
    for orologio in lista_orologi:
        orologio.start()

o1 = Orologio("Orologio 1")
o2 = Orologio("Orologio 2")
o3 = Orologio("Orologio 3")

orologaio.append(o2)
orologaio.append(o1)
orologaio.append(o3)


avviaOrologi(orologaio)
