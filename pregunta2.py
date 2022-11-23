import os

trabajadores = [["Eduardo", 140.52],["Paco", 1005.98],["Diego", 282.39],["Juliano", 1197.80],["Hernesto", 666.04],["Juan", 851.61],["Juan el otro", 644.05],["Camilo ventanas", 1656.90],["Lourdes", 463.55],["Revilla", 1721.73]]

SALARIO_MINIMO=900.0

sum = 0.0
media = 0.0

def limpiarConsola():    
    input("\nPulse cualquier tecla para continuar")
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")
        

for index in range(len(trabajadores)):
    if(trabajadores[index][1]<SALARIO_MINIMO):
        print(f"Actualizado sueldo de {trabajadores[index][0]} ({trabajadores[index][1]} --> {SALARIO_MINIMO})")
        trabajadores[index][1]=SALARIO_MINIMO
limpiarConsola()

for index in range(len(trabajadores)):
    print(f"{trabajadores[index][0]}: {trabajadores[index][1]}")
    sum += float(trabajadores[index][1])
media = sum/len(trabajadores)
print(f"\nMedia de sueldos: {media}")
limpiarConsola()

for index in range(len(trabajadores)):
    if(trabajadores[index][1]<media):
        print(f"Incremento de 3% en el sueldo de {trabajadores[index][0]} ({trabajadores[index][1]} --> {trabajadores[index][1]+(trabajadores[index][1]*0.03)})")
        trabajadores[index][1] = trabajadores[index][1]+(trabajadores[index][1]*0.03)
limpiarConsola()

for index in range(len(trabajadores)):
    print(f"{trabajadores[index][0]}: {trabajadores[index][1]}")
limpiarConsola()