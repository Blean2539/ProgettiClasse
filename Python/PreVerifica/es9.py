# --- CLASSE BASE (PADRE) ---
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")


# --- CLASSE DERIVATA (FIGLIA) ---
class Studente(Persona):
    def __init__(self, nome, eta, scuola):
        # super().__init__() serve a ereditare gli attributi della classe padre (Persona)
        super().__init__(nome, eta)
        self.scuola = scuola

    def info_studente(self):
        print(f"Frequento l'istituto: {self.scuola}.")


# --- MONDO PRINCIPALE ---
# Creazione dell'oggetto Studente come richiesto dalla traccia
studente1 = Studente("Francesco", 18, "IIS Volterra Elia")

print("--- ESECUZIONE METODI ---")
# Richiamo sia il metodo ereditato che quello della classe Studente
studente1.presentati()
studente1.info_studente()
