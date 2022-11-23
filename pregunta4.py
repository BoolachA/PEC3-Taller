#  x x x x
#  x x x x
#  x x x x
import os

matrizA = [[],[],[],[]]
matrizB = [[],[],[],[]]

def limpiarConsola():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")


for x in range(4):
    for y in range(3):
        matrizA[x].append(int(input("Numero entero: ")))
print(matrizA)