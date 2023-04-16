"""Realizar un programa que muestre la cantidad de números que son múltiplos de 2 o de 3
comprendidos entre 1 y 100"""

multiplos_dos_tres = 0

nums = range (0,101)

for multiples_two_or_three in nums:
    print (multiples_two_or_three, " es múltiplo de 2 o 3: " , multiples_two_or_three % 2 == 0 or multiples_two_or_three % 3 == 0)
    if multiples_two_or_three % 2 == 0 or multiples_two_or_three %3 == 0:   
        multiplos_dos_tres = multiplos_dos_tres + 1
print("La cantidad de números que son múltiplos de 2 o de 3 entre 1 y 100 es:",  multiplos_dos_tres)

