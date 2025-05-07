#Estructura de datos no secuencial, no importa
#No elemento duplicados
#Representar Conjuntos

set1 = set([1, 2, 3,4, 5, 6, 7, 8, 9, 10])
set2 = set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

print("set1: ", set1)
print("set2: ", set2)

#Que elementos diff a set2
print(set1 - set2)

#Que elementos son comunes a set1 y set2
print(set1 & set2)
