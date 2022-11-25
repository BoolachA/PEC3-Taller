import os

#Declaración de constantes, listas y variables
SALARIO_MINIMO=900.0

trabajadores = [["Eduardo", 140.52],["Paco", 1005.98],["Diego", 282.39],["Juliano", 1197.80],["Hernesto", 666.04],["Juan", 851.61],["Juan el otro", 644.05],["Camilo ventanas", 1656.90],["Lourdes", 463.55],["Revilla", 1721.73]]

sum = 0.0
media = 0.0

#Función encargada de limpiar la consola segun el sistema operativo, retorna el 0 para indicar que su correcto funcionamiento
def limpiarConsola():    
    input("\nPulse cualquier tecla para continuar")
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")
    return 0
        
#Actualizar el sueldo de todos aquellos que tienen un sueldo inferior al salario minimo
#Comparamos el sueldo de todos los trabajadores con el salario minimo
for index in range(len(trabajadores)):
    #Trabajadores[Trabajador][0=NOMBRE,1=SUELDO]
    if(trabajadores[index][1]<SALARIO_MINIMO):
        #Si el sueldo resulta ser menor que el salario minimo, notificamos el cambio en la pantalla y actualizamos su sueldo
        print(f"Actualizado sueldo de {trabajadores[index][0]} ({trabajadores[index][1]} --> {SALARIO_MINIMO})")
        trabajadores[index][1]=SALARIO_MINIMO
limpiarConsola()

#Calculo de la media de sueldos
for index in range(len(trabajadores)):
    #Imprimimos todos los sueldos
    print(f"{trabajadores[index][0]}: {trabajadores[index][1]}")
    #En la variable sum guardamos la suma de todos los sueldos
    sum += float(trabajadores[index][1])
#Para obtener la media se divide la suma de todos los sueldos entre el numero de trabajadores en la lista
media = sum/len(trabajadores)
print(f"\nMedia de sueldos: {media}")
limpiarConsola()

#Aumento de 3% a los que estan por debajo de la media
for index in range(len(trabajadores)):
    if(trabajadores[index][1]<media):
        #Notificación en la pantalla
        print(f"Incremento de 3% en el sueldo de {trabajadores[index][0]} ({trabajadores[index][1]} --> {trabajadores[index][1]+(trabajadores[index][1]*0.03)})")
        #SueldoActualizado = sueldo + (sueldo * 0.03)
        trabajadores[index][1] = trabajadores[index][1]+(trabajadores[index][1]*0.03)
limpiarConsola()

#Finalmente imprimimos la lista en la pantalla para presentar el resultado final
for index in range(len(trabajadores)):
    print(f"{trabajadores[index][0]}: {trabajadores[index][1]}")
limpiarConsola()