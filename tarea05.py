import os
from datetime import datetime

rango = 100000
for x in range (5,9):
    date_format_str = '%Y-%m-%d %H:%M:%S.%f'
    inicio = datetime.strptime(f"{datetime.now()}", date_format_str)

    file = open("tarea05.txt","w")
    file.write(" Inicio test " + f"{x}" + " ceros. " + "{:,}".format(rango) + " numeros.")
    file.write(" Fecha hora de inicio: " + f"{inicio}" )

    #ciclo de n cantidad de números
    for i in range (0, rango):
        file.write("numero. " + f"{i}")

    fin = datetime.strptime(f"{datetime.now()}", date_format_str) 
    diff = fin - inicio
    file.write(" Fecha hora fin: " + f"{fin}")
    file.write(" Total tiempo de ejecución: " + f"{diff}")
    file.close()

    print(" ***** Inicio test " + f"{x}" + " ceros *******  " + "{:,}".format(rango) + " numeros ******* ")
    print(" Fecha hora de inicio: " + f"{inicio}" + " >> Fecha hora fin : " + f"{fin}")
    print(" Total tiempo de ejecución con : " + "{:,}".format(rango) + " numeros -> " + f"{diff}")
    rango = rango * 10
