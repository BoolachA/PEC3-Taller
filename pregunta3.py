import os

lista = []

def limpiarConsola():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

for x in range(15):
    correcto = False
    limpiarConsola()
    print(lista)
    while(not correcto):
        try: 
            elemento = int(input("Numero del 0 al 10: "))
            if(elemento<0 or elemento>10):
                raise Exception("InvalidRange")
            else:
                lista.append(elemento)
                correcto=True
        except:
            print("Solamente numeros del 0 al 10")

limpiarConsola()
print(lista)
for num in range(len(lista)):
    if(lista[num] != 5 and lista[num] != 10):
        print(".")
    elif(lista[num] == 5):
        if(num==0):
            print("[*]")
        else:
            print("*"*lista[num-1])
    elif(lista[num] == 10):
        if(num==0):
            print("[**]")
        elif(lista[0]==5 and num==1):
            print("[JACKPOT]")
        else:
            print("*"*lista[num-1], "[]", "*"*lista[num-1])