# Método tradicional
lista = []
for letra in 'casa':
    lista.append(letra)
print(lista)

#Otra manera de hacerlo 
s= 'casa'
l = list (s)
print (l)

# Con comprensión de listas
lista = [letra for letra in 'casa']
print(lista)

#Ejemplo número 2
#Crear una lista con las potencias de 2 de los primeros 10 números:

# Método tradicional
lista = []
for numero in range(0,11):
    lista.append(numero**2)
print(lista)

# Con comprensión de listas
lista = [numero**2 for numero in  range(0,11)]
print(lista)