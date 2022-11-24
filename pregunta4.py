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
    return 0

def matrizTexto(matriz):
    linea1 = linea2 = linea3 = " "
    for x in range(4):
        linea1 += str(matriz[x][0]) + " "
    for x in range(4):
        linea2 += str(matriz[x][1]) + " "
    for x in range(4):
        linea3 += str(matriz[x][2]) + " "
    lineaFinal = str(linea1 + "\n" + linea2 + "\n" + linea3)
    return lineaFinal

def requestMatriz(matriz):
    for x in range(4):
        for y in range(3):
            matriz[x].append(int(input("Numero entero: ")))
            limpiarConsola()
    return matrizTexto(matriz)


if __name__ == "__main__":
    limpiarConsola()
    print(requestMatriz(matrizA))
    input("Pulse cualquier botón para continuar con la matriz B")
    print(requestMatriz(matrizB))
    input("Pulse cualquier botón para continuar con la suma\n")
    input("")