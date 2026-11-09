import time  # Importo il modulo del tempo nel Mondo Principale

loop = True
scelta = 0



class Utente:
    def __init__(self, id_utente, lista_preferiti):
        self.id_utente = id_utente
        lista_preferiti

class Piattaforma_Streaming:
    def __init__ (self):
        self.lista_contenuti = []
        self.lista_film = []
        self.lista_serietv = [] 

        
    
class Contenuto:
    def __init__(self, titolo, anno_pubb, durata_min, views):
        self.titolo = titolo
        self.anno_pubb = anno_pubb
        self.durata_min = durata_min
        self.views = views

    def riproduci(self):
        print(f"riproduzione contenuto: '{self.titolo}'  della durata di: {self.durata_min}")
    
    def info(self):
        print(self.titolo, self.anno_pubb, self.durata_min, self.views)


class Film(Contenuto):
    def __init__(self, titolo, anno_pubb, durata_min, views, genere, modalita_cinema):
        # super().__init__() serve a ereditare gli attributi della classe padre (Persona)
        super().__init__(titolo, anno_pubb, durata_min, views,  )
        self.genere = genere
        self.modalita_cinema = modalita_cinema

    def riproduci_film(self):
        print(f"riproduzione Film: '{self.titolo}'  della durata di: {self.durata_min}")

    def info_Film(self): #stampa tutti gli att di film
        print(f"ciao{self.titolo}")


class SerieTV(Contenuto):
    def __init__(self, titolo, anno_pubb, durata_min, views, numero_stagioni, modalità_maratona):
        # super().__init__() serve a ereditare gli attributi della classe padre (Persona)
        super().__init__(titolo, anno_pubb, durata_min, views,  )
        self.numero_stagioni = numero_stagioni
        self.modalità_maratona = modalità_maratona

    def riproduci_serie(self):
        print(f"riproduzione Serie: '{self.titolo}'  della durata di: {self.durata_min}")  ######    CONTROLLARE!!!!!!!!!!!! 
        
    def info_serietv(self): #stampa tutti gli att di serie
        print(self.titolo, self.anno_pubb, self.durata_min, self.views, self.numero_stagioni)


p = Piattaforma_Streaming()  # inizializzo la piattaforma streaming o meglio ne creo una

while loop == True:

    try:

        scelta = int(input("\n 1 Inserisci Film. \n 2 Inserisci Serie TV.  \n 3 Visualizza tutti i contenuti. \n 4 Cerca un contenuto. \n 5 Elimina un contenuto. \n 6 Riproduci tutti i contenuti. \n 7 Attiva modalità speciali. \n 8 Gestione preferiti \n 9 Mostra contenuto più visualizzato. \n 10 Esci. \n-> Seleziona: "))

        if scelta == 1:
            #inserimento film 
            print("inserire le info richieste:\n") 
            nome_film = input(f"inserire titolo film: ")
            anno_film = input(f"inserire anno_pub film: ")
            durata_film = input(f"inserire durata film in min: ")
            visual_film = input(f"inserire views film: ")
            gen_film = input(f"inserire genere film: ")
            mod_film = False
            # Aggiorniamo il numero totale dei giocatori
            f = Film(nome_film, anno_film, durata_film, visual_film, gen_film, mod_film)

            p.lista_contenuti.append(f)
            p.lista_film.append(f)

        elif scelta == 2:
            #Inserisci Serie TV
            print("inserire le info richieste:\n") 
            nome_serie = input(f"inserire titolo serie: ")
            anno_serie = input(f"inserire anno_pub serie: ")
            durata_serie = input(f"inserire durata serie in min: ")
            visual_serie = input(f"inserire views serie: ")
            gen_serie = input(f"inserire genere serie: ")
            mod_serie = False
            # Aggiorniamo il numero totale dei giocatori
            s = SerieTV(nome_serie, anno_serie, durata_serie, visual_serie, gen_serie, mod_serie)

            p.lista_contenuti.append(s)
            p.lista_serietv.append(s)

            print("contenuto aggiunto con successo!!!!")
            
        elif scelta == 3:
            #Visualizza tutti i contenuti
            
             for i in range(len(p.lista_contenuti)):
                if isinstance(i,Film):
                    p.lista_contenuti[i].info_Film()

                elif isinstance(i,SerieTV):
                    p.lista_contenuti[i].info_serietv()
                
                else:
                    # print("non entra nel if")
                    print("errore, riprovare")

        elif scelta == 4:
            cerca = input("inserire il titolo del contneuto da cercare")
            for i in range(len(p.lista_contenuti)):
                # ogg,classe se true modifica classe
                if p.lista_contenuti[i].titolo == cerca | isinstance(p.lista_contenuti[i],Film):
                    i.info_Film()  #chiedere al prof se si puo fare p.lista_contenuti[i].anno_pubb
                elif p.lista_contenuti[i].titolo == cerca | isinstance(p.lista_contenuti[i],SerieTV):
                    i.info_serietv()
                    

        elif scelta == 5:
            #Elimina un contenuto
            cerca = input("inserire il titolo del contneuto da eliminare")
            tipo = input("Film o Serie?: ")  #lo faccio inserire allutente perche esistono serire e film con lo stesso nome anche se spesso della stessa saga per in quel caso eliminerebbe per 
            #forza entrmbi e non va bene perche chiede di elimare il contenuto e sono due contenuti diversi
            if tipo == Film:
                for i in range(len(p.lista_film)):
                    # ogg,classe se true modifica classe

                    if p.lista_film[i].titolo == cerca:
                        for i in range(len(p.lista_film)):
                            del p.lista_film[i] 

                    elif p.lista_serietv[i].titolo == cerca:
                        for i in range(len(p.lista_serietv)):
                            del p.lista_serietv[i]

        elif scelta == 6:
            #Riproduci tutti i contenuti
            for i in range(len(p.lista_contenuti)):
                if isinstance(i,Film):
                    i.riproduci_film()

                elif isinstance(i,SerieTV):
                    i.riproduci_serie()

        elif scelta == 7:
            #Attiva modalità speciali
            print("")

        elif scelta == 8:
            #Gestione preferiti
            print("")

        elif scelta == 9:
            #Mostra contenuto più visualizzato
            print("")
            max = 0
            titolo_maxview = ""
            for i in range(len(p.lista_contenuti)):
                if isinstance(i,Film):
                    if max <= p.lista_contenuti[i].views():
                        max = p.lista_contenuti[i].views()
                        titolo_maxview = p.lista_contenuti[i].titolo()
                        

                elif isinstance(i,SerieTV):
                    if max <= p.lista_contenuti[i].views():
                        max = p.lista_contenuti[i].views()
                        titolo_maxview = p.lista_contenuti[i].titolo()
            print(f"il contenuto con il max numero di view è {titolo_maxview} con {max}")

        elif scelta == 10:
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
        
    except:
        continue

