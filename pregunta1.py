#Programa solo funciona en python 3.10 superiores debido al uso de match/case en la línea 15
import os

opcionValida = False

agendaDic={
    "contacto1" : "numero1",
    "contacto2" : "numero2",
    "contacto3" : "numero3"
}

def limpiarConsola():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

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

while(True):
    match opcion:
        case 1:
            print("1")
        case 2:
            print("2")
        case 3:
            print("3")
        case 4:
            limpiarConsola()
            for contacto in agendaDic:
                print(f"{contacto}: {agendaDic[contacto]}")
        case 5:
            os._exit(0)

input("")