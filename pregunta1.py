#Programa solo funciona en python 3.10.X o superiores debido al uso de match/case en la línea 39
import os

#Variable para controlar el bucle del menú
running = True

#Diccionário donde se guardan los contactos
agendaDic={
}

#Función encargada de limpiar la consola segun el sistema operativo, retorna el 0 para indicar que su correcto funcionamiento
def limpiarConsola():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")
    return 0

#Bucle que se mantendrá activo hasta que el usuário elija la opción de salir
while(running):
    limpiarConsola()
    #Construcción del menu dentro de un bucle que se mantendrá activo hasta que el usuário elija una opción válida
    opcionValida = False
    while(not opcionValida):
        print("-------------AGENDA-------------\n1.Añadir Modificar\n2.Borrar\n3.Buscar\n4.Listar\n5.Salir")
        try:
            opcion = int(input(""))
            #Si la opción es valida terminamos el bucle, si la opción no existe forzamos un error y reiniciamos el bucle
            if(opcion > 5 or opcion < 1):
                raise Exception("invalidOpc")
            else:
                opcionValida=True
        except:
            limpiarConsola()
            print("Opción inválida")

    #Para evitar el uso de elifs se utiliza match/case para comparar "opción" con 5 posibles casos.
    #Al terminar el caso correspondiente (a excepción del caso 5), se reinicia el bucle principal y se vuelve a imprimir el menu
    match opcion:
        #Caso 1 (Añadir contacto)
        case 1:
            limpiarConsola()
            contacto = input("Nombre del contacto: ")
            numero = input("Numero del contacto: ")
            agendaDic[contacto] = numero
            input("\nPulse cualquier tecla para continuar")
        #Caso 2 (Eliminar contacto)
        case 2:
            limpiarConsola()
            select = input("Eliminar contacto: ")
            try:
                del agendaDic[select]
                print("Contacto borrado.")
            except:
                print("Contacto no encontrado")
            input("\nPulse cualquier tecla para continuar")
        #Caso 3 (Buscar contacto)
        case 3:
            limpiarConsola()
            select = input("Buscador: ")
            try:
                print(f"{select}: {agendaDic[select]}")
            except:
                print("Contacto no encontrado")
            input("\nPulse cualquier tecla para continuar")
        #Caso 4 (Imprimir contactos)
        case 4:
            limpiarConsola()
            #Con el uso de un for, pasamos por todos los contactos del diccionario y los imprimimos con su correspondiente numero
            for contacto in agendaDic:
                print(f"{contacto}: {agendaDic[contacto]}")
            input("\nPulse cualquier tecla para continuar")
        #Caso 5 (Salir)
        case 5:
            #Se modifica la variable de control del bucle principal para finalizar el programa
            running = False
