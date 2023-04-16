"""Realizar un programa que pida una frase y el programa deberá mostrar la frase con un
#espacio entre cada letra. La frase se mostrará así: H o l a."""

sentence = input ('Ingrese la palabra que quiere ser deletreada:')
len_sentence = len(sentence)

for letra in sentence:
    print (letra, end = " ")
print ( )


