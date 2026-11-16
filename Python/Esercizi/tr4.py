import threading
from threading import Thread


Robo = []


class Robot(Thread):
    def __init__(self, modello, velocita, liv_batt):
        super().__init__()
        self.modello = modello
        self.velocita = velocita
        self.liv_batt = liv_batt
        lista = []

class Consegna():
    def __init__(self, distanza, limite):
        self.distanza = distanza
        self.limite = limite

    def Iscrizione_gara (self, Lista_Robot):
        for i in range(self.limite)
            if self.liv_batt >=50:
