lista = []

for i in range(5):
    print("digita una parola da aggiungere alla lista")
    parola = input()
    lista.append(parola)

print(lista)

for parola in lista:
    if len(parola) > 5:
        print(parola)
