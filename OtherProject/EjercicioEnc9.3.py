"""Un docente de Programación tiene un listado de 3 notas registradas por cada uno de sus
N estudiantes. La nota final se compone de un trabajo práctico Integrador (35%), una
Exposición (25%) y un Parcial (40%). El docente requiere los siguientes informes claves
de sus estudiantes:
1.Nota promedio final de los estudiantes que reprobaron el curso. Un estudiante reprueba el curso si tiene una nota final inferior a 6.5
2.Porcentaje de alumnos que tienen una nota de integrador mayor a 7.5.
3.La mayor nota obtenida en las exposiciones.
4.Total de estudiantes que obtuvieron en el Parcial entre 4.0 y 7.5.
5.El programa pedirá la cantidad de alumnos que tiene el docente y en cada alumno pedirá
las 3 notas y calculará todos informes claves que requiere el docente"""

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos:"))

sumatoriaNotasEstudiantesReprobados = 0
numeroDeEstudiantesReprobados = 0
estudiantesConIntegradorMayor = 0
notaMaximaExposiciones = 0
totalDeEstudiantesNotaParcial = 0
alumnos = 0 

for alumnos in range (cantidad_alumnos):
    nota_integrador = float (input("Ingrese la nota del trabajo práctico del estudiante: "))
    nota_exposicion = float (input ("Ingrese la nota de la exposición del alumno: "))
    nota_parcial = float (input ("Ingrese la nota del parcial del estudiante: "))

    nota_final = (nota_integrador * 0.35)+ (nota_exposicion * 0.25) + (nota_parcial * 0.40)

    if nota_integrador < 6.5:
        print("Reprobo")
        numeroDeEstudiantesReprobados = numeroDeEstudiantesReprobados + 1
        sumatoriaNotasEstudiantesReprobados = sumatoriaNotasEstudiantesReprobados + nota_final
    
    #Porcentaje de alumnos que tienen una nota de integrador mayor a 7.5.
    if nota_integrador > 7.5 :
        estudiantesConIntegradorMayor = estudiantesConIntegradorMayor + 1
    
    #La mayor nota obtenida en las exposiciones
    if nota_exposicion > notaMaximaExposiciones:
        notaMaximaExposiciones = nota_exposicion
    
    #Total de estudiantes que obtuvieron en el Parcial entre 4.0 y 7.5
    if nota_parcial > 4.0 and nota_parcial < 7.5:
        totalDeEstudiantesNotaParcial = totalDeEstudiantesNotaParcial + 1
        
print("Nota promedio final estudiantes reprobados: ", (sumatoriaNotasEstudiantesReprobados/numeroDeEstudiantesReprobados))
print ("El porcentaje de alumnos con nota de trabajo integrador mayor a 7.5 es:  " , (estudiantesConIntegradorMayor * 100/cantidad_alumnos), " % ")
print ("La mayor nota obtenida en la exposiciones es: ", notaMaximaExposiciones)
print ("El total de estudiantes que obtuvieron en el parcial notas entre 4.0 y 7.5: ", totalDeEstudiantesNotaParcial)