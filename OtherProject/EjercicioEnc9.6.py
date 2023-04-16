""" Siguiendo el ejercicio 2 de los ejercicios principales, ahora deberemos hacer lo mismo
pero que la cadena se muestre al revés. Por ejemplo, si tenemos la cadena: Hola,
deberemos mostrar a l o H."""

sentence = input ('Ingrese la palabra que quiere ser deletreada:')
len_sentence = len(sentence)

#Se usa para invertir cadenas
inverted_sentence = sentence [::-1]

for letra in inverted_sentence:
    print (letra, end = " ")
print ( )


