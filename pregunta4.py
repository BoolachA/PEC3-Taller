import os

#Función encargada de limpiar la consola segun el sistema operativo, retorna el 0 para indicar que su correcto funcionamiento
def limpiarConsola():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")
    return 0

#Función que toma como entrada una matriz y devuelve un string con la matriz impresa en 3 lineas
def matrizTexto(matriz):
    linea1 = linea2 = linea3 = " "
    #Pasamos por toodos los elementos de la fila X y los almacenamos en "lineaX"
    for x in range(len(matriz)):
        linea1 += str(matriz[x][0]) + " "
    for x in range(len(matriz)):
        linea2 += str(matriz[x][1]) + " "
    for x in range(len(matriz)):
        linea3 += str(matriz[x][2]) + " "
    #Se unen todas las lineas en un string
    lineaFinal = str(linea1 + "\n" + linea2 + "\n" + linea3)
    #Retornamos la linea final
    return lineaFinal

#Función que toma como entrada una matriz, pide al usuário rellenarla y devuelve un string con la matriz impresa en 3 lineas (con la función anterior)
def requestMatriz():
    matriz = [[], [], [], []]
    #Forzamos que la matriz tenga una dimensión de 4x3
    for x in range(4):
        for y in range(3):
            #Bucle que controla si el input del usuário es un numero entero
            numeroEntero = False
            while(not numeroEntero):
                try:
                    matriz[x].append(int(input("Numero entero: ")))
                    #Si no hay errores, terminamos el bucle y pasamos al siguiente paso
                    numeroEntero = True
                except:
                    #Si python detecta algun error, reiniciamos el bucle y volvemos a pedir un numero entero al usuário
                    print("Solamente numeros enteros.")
            limpiarConsola()
    #Llamamos la función de imprimir matrices para retornar el texto de la matriz modificada
    return matriz

#Función que toma como entrada dos matrices y las suma, devolviendo un string con la matriz final impresa en 3 lineas
def sumMatrices(matriz1,matriz2):
    matrizFinal = [[],[],[],[]]
    #Se utilizan dos FOR'S para pasar por todos los elementos de las matrices
    for x in range(4):
        for y in range(3):
            #Se añade a la matriz final la suma de ambos elementos
            matrizFinal[x].append(matriz1[x][y]+matriz2[x][y])
    return matrizFinal

if __name__ == "__main__":
    print("Valores para matriz A: ")
    #Llamamos la función que rellena la matriz indicada y la imprime en pantalla
    matrizA = requestMatriz()
    print(matrizTexto(matrizA))
    input("Pulse cualquier botón para continuar con la matriz B")
    matrizB = requestMatriz()
    print(matrizTexto(matrizB))
    limpiarConsola()
    input(f"La matriz:\n{matrizTexto(matrizA)}\nSerá sumada con:\n{matrizTexto(matrizB)}\nPresione cualquier botón para continuar")
    limpiarConsola()
    #Llamamos la función suma las matrices indicadas y nos devuelve un string con el resultado
    sumaMatrices = sumMatrices(matrizA,matrizB)
    print(f"Resultado:\n{matrizTexto(sumaMatrices)}")
    input("")
