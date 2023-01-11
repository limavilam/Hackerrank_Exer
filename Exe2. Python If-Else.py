#Task
#Given an integer,n , perform the following conditional actions:
#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
#Input Format
#A single line containing a positive integer, .
#Constraints
#Output Format
#Print Weird if the number is weird. Otherwise, print Not Weird.

integer = input ('Enter a number:')
n = int (integer)
if n%2!=0:
    print ('Weird')
else:
    if  n in range (2,5):
        print ('Not Weird')
    elif n in range (6,20):  #No es else porque no se pude más de dos posibilidades ya que cuenta el if del primero. 
        print ('Weird')
    else:
        print ('Not Weird')
