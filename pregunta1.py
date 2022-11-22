#Programa solo funciona en python 3.10 superiores debido al uso de match/case en la línea 15
#Para facilitar la comprehensión del código crearía una función para tareas que se repiten mucho como limpiar la consola según el sistema operativo
import os

running = True

agendaDic={
}

def limpiarConsola():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")


while(running):
    limpiarConsola()
    opcionValida = False
    while(not opcionValida):
        print("-------------AGENDA-------------\n1.Añadir Modificar\n2.Borrar\n3.Buscar\n4.Listar\n5.Salir")
        try:
            opcion = int(input(""))
            if(opcion > 5 or opcion < 1):
                raise Exception("invalidOpc")
            else:
                opcionValida=True
        except:
            print("Opción inválida")


    match opcion:
        case 1:
            limpiarConsola()
            contacto = input("Nombre del contacto: ")
            numero = input("Numero del contacto: ")
            agendaDic[contacto] = numero
            input("\nPulse cualquier tecla para continuar")

        case 2:
            limpiarConsola()
            select = input("Eliminar contacto: ")
            try:
                del agendaDic[select]
                print("Contacto borrado.")
            except:
                print("Contacto no encontrado")
            input("\nPulse cualquier tecla para continuar")

        case 3:
            limpiarConsola()
            select = input("Buscador: ")
            try:
                print(f"{select}: {agendaDic[select]}")
            except:
                print("Contacto no encontrado")
            input("\nPulse cualquier tecla para continuar")

        case 4:
            limpiarConsola()
            for contacto in agendaDic:
                print(f"{contacto}: {agendaDic[contacto]}")
            input("\nPulse cualquier tecla para continuar")

        case 5:
            running = False