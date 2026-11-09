freq = {}  # crea il dizionario


print("inserire una striga di cui contare le singole lettere")
stringa = input()       #prende l'input dall'utente e lo mette in variabile nel mondo principale (script principale)


def conta_caratteri(stringa):    #crea una funzione è copia la variabile stringa nel micromondo (funzione) e (diventa var locale)

    for carattere in stringa:  #python gestisce le stringe come liste di caratteri quindi se esegui un for su una stringa, il for itera su ogni carattere


        if carattere in freq:
            freq[carattere] = freq[carattere] + 1 #se il carattere è esiste gia, incrementa il suo conteggio
        else:
            freq[carattere] = 1 #se il carattere non esiste, lo aggiunge al dizionario con conteggio 1

    return freq #apre il portale dal micro mondo e lancia il contenuto del dizionario nel mondo principale (script principale)

freq = conta_caratteri(stringa) #lui sa che ce un portale con qualcosa che arriva dal micro mondo (conta_caratteri)
                                #e assegna a qualsiasi cosa essa sia il nome che diciamo in questo caso "freq"



for i in freq:
    print(i, freq[i]) #stampa il contenuto del dizionario uno alla volta
