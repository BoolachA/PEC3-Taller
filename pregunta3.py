import os

lista = []

#Función encargada de limpiar la consola segun el sistema operativo, retorna el 0 para indicar que su correcto funcionamiento
def limpiarConsola():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")
    return 0

#Se solicita al usuário 15 elementos
for x in range(15):
    correcto = False
    limpiarConsola()
    print(lista)
    #Bucle finaliza cuando el numero dado por el usuário no genera ningun error
    while(not correcto):
        try: 
            elemento = int(input("Numero del 0 al 10: "))
            if(elemento<0 or elemento>10):
                #Generamos un error si el numero no está entre 0 y 10
                raise Exception("InvalidRange")
            else:
                #Si el numero es válido lo añadimos a la lista y finalizamos el bucle
                lista.append(elemento)
                correcto=True
        except:
            #Se detecta un error y reiniciamos el bucle
            limpiarConsola()
            print("Solamente numeros del 0 al 10")

limpiarConsola()
print(lista)
#Pasamos por todos los elementos de la lista
for num in range(len(lista)):
    if(lista[num] != 5 and lista[num] != 10):
        #Si imprime un . si el elemento no es 10 o 5
        print(".")
    elif(lista[num] == 5):
        if(num==0):
            #Si hay un 5 en la primera posición imprimimos [*]
            print("[*]")
        else:
            #Multiplicamos "*" por el numero anterior al 5
            print("*"*lista[num-1])
    elif(lista[num] == 10):
        if(num==0):
            #10 en la primera posición, se imprime [**]
            print("[**]")
        elif(lista[0]==5 and num==1):
            #5 en la primera posición y 10 en la segunda, imprimimos [JACKPOT]
            print("[JACKPOT]")
        else:
            #Multiplicamos "*" por el numero anterior al 10 y lo imprimimos en el formato indicado por el enunciado
            print("*"*lista[num-1], "[]", "*"*lista[num-1])
input("Pulse cualquier tecla para continuar")
