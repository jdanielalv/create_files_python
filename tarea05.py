import os
from datetime import datetime

inicio = datetime.now().isoformat(timespec='microseconds')

file = open("tarea05.txt","w")
file.write("inicio:" + f"{inicio}")

for i in range (1, 100001):
    file.write("nro. " + f"{i}")

fin = datetime.now().isoformat(timespec='microseconds') 
file.write(" final:" + f"{fin}")
file.close()

print("inicio: " + f"{inicio}")
print("final : " + f"{fin}")
