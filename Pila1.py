
pila = []


for i in range(1, 11):
    pila.append(i)
print("Pila con 10 elementos:", pila)


print("Elemento en la cima:", pila[-1])


for i in range(4):
    pila.pop()
print("Pila después de quitar 4 elementos:", pila)

print("Tamaño actual:", len(pila))
print("¿Está vacía?:", len(pila) == 0)


while len(pila) > 0:
    pila.pop()

print("Pila final:", pila)
print("¿Está vacía al final?:", len(pila) == 0)