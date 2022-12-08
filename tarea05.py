import os
from datetime import datetime

date_format_str = '%Y-%m-%d %H:%M:%S.%f'
inicio = datetime.strptime(f"{datetime.now()}", date_format_str)

file = open("tarea05.txt","w")
file.write("inicio: " + f"{inicio}")

for i in range (1, 100001):
    file.write("nro. " + f"{i}")

fin = datetime.strptime(f"{datetime.now()}", date_format_str) 
diff = fin - inicio
file.write(" final: " + f"{fin}")
file.write("diferencia: " + f"{diff}")
file.close()

print("inicio: " + f"{inicio}")
print("final : " + f"{fin}")
print("diferencia: " + f"{diff}")
