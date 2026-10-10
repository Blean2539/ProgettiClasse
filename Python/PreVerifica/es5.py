lista_filtrata = []
lista_filtrata_ripulita = []

print("inserire 7 valori")

lista_input = []
for i in range(7):
    lista_input.append(int(input()))  # prende l'input dall'utente e riempie la lista nel mondo principale

print("inserire il valore di filtraggio")
n = int(input())  # prende la soglia di filtraggio e la salva nella variabile 'n' del mondo principale


def filtra_maggiori(lista, n1):  # passa lista_input dentro 'lista' e n dentro 'n1' (var locali)
    lista_filtrata2 = []  # CREA LA LISTA DENTRO IL MICRO-MONDO (nasce dentro la funzione, isolata da fuori)

    for i in range(len(lista)):
        if lista[i] > n1:
            lista_filtrata2.append(lista[i])  # se l'elemento e' maggiore della soglia, lo aggiunge alla lista del micro-mondo

    return lista_filtrata2  # apre il portale e lancia il contenuto di 'lista_filtrata2' nel mondo principale


lista_filtrata = filtra_maggiori(lista_input, n)  # riceve dal portale e assegna a 'lista_filtrata' nel mondo principale
lista_filtrata_ripulita = set(lista_filtrata)  # elimina i duplicati trasformando in set

print(lista_filtrata_ripulita)  # stampa il risultato finale
