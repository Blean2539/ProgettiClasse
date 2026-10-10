
dati = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7, 7, 7]

contatore_7 = 0

for value in dati:
    if value == 7:
        contatore_7 += 1
print(f"Numero di 7 nella lista: {contatore_7}")

lista_dati = list(dati)

print(f"Lista dei dati: {lista_dati}")


set_dati = set(lista_dati)
print(f"Set dei dati: {set_dati}")
