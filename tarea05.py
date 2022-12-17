import os
from datetime import datetime

rango = 100000
for x in range (5,9):
    date_format_str = '%Y-%m-%d %H:%M:%S.%f'
    inicio = datetime.strptime(f"{datetime.now()}", date_format_str)

    file = open("tarea05.txt","w")
    file.write("inicio: " + f"{inicio}" )

    for i in range (0, rango):
        file.write("nro. " + f"{i}")

    fin = datetime.strptime(f"{datetime.now()}", date_format_str) 
    diff = fin - inicio
    file.write(" final: " + f"{fin}")
    file.write("diferencia: " + f"{diff}")
    file.close()

    print("******* test " + f"{x}" + " ceros *******  " + f"{rango}" + " numeros ******* ")
    print("inicio: " + f"{inicio}" + " >> final : " + f"{fin}")
    print("diferencia: " + f"{diff}")
    rango = rango * 10
