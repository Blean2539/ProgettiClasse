def conta_lettere(parola):
    dizionario = {}
    for lettera in parola:
        if lettera in dizionario:
            c = dizionario[lettera]
            dizionario[lettera] = c + 1
        else:
            dizionario[lettera] = 1
    return dizionario

p = input("Inserisci una parola: ")
print(conta_lettere(p))


#spigazione scorrimento dizionario

dizionario_ritornato = conta_lettere(p)
for chiave in dizionario_ritornato:
    print(f'{chiave} - {dizionario_ritornato[chiave]}')

#fine spiegazione
