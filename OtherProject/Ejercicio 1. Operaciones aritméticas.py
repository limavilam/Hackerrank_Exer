#Construir un programa que simule un menú de opciones para realizar las cuatro
#operaciones aritméticas básicas (suma, resta, multiplicación y división) con dos valores
#numéricos enteros. El usuario, además, debe especificar la operación con el primer
#carácter de la operación que desea realizar: ?S' o ?s? para la suma, ?R? o ?r? para la resta,
#?M? o ?m? para la multiplicación y ?D? o ?d? para la división.""

print("Bienvenido al programa de operaciones aritméticas")
print("Por favor, ingrese dos números enteros")

# Pedimos los dos números enteros
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

# Mostramos el menú de opciones
print("Elija la operación que desea realizar:")
print("S - Suma")
print("R - Resta")
print("M - Multiplicación")
print("D - División")

# Pedimos la opción al usuario
opcion = input("Opción: ")

# Realizamos la operación correspondiente según la opción elegida
if opcion == "S" or opcion == "s":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion == "R" or opcion == "r":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif opcion == "M" or opcion == "m":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif opcion == "D" or opcion == "d":
    # Validamos que el segundo número no sea cero para evitar una división entre cero
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("No se puede dividir entre cero")
else:
    print("Opción inválida")
