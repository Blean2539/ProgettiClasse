lista1 = [2, 7, 6, 3, 5, 7]
lista2 = [1, 8, 3, 4, 9, 6]

set1 = set(lista1)
set2 = set(lista2)

print(set1, set2)

unione  = set1 | set2
print(unione)


intersezione = set1 & set2
print(intersezione)

differenza = set1 - set2
print(differenza)

# print(lista1, lista2)

# lista_union = lista1 + lista2

# print(lista_union)

# lista_intersezione = []

# for i in lista1:
#     if i in lista2:
#         lista_intersezione.append(i)

# print(lista_intersezione)
