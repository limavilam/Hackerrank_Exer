"""Escribir un programa que calcule la suma de los N primeros números naturales. El valor
de N se leerá por teclado."""

natural_nums = int(input ("Ingrese un número entero positivo:"))
sume_naturals = 0 

for i in range (1, natural_nums+1):
    sume_naturals = sume_naturals + i

print("La suma de los", natural_nums, "primeros números naturales es:", sume_naturals)




