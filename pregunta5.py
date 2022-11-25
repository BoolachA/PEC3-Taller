#Declaración de variables
tweet = input("Tweet: ")
hashtags = []
contador=""
countingHashtag = False

#Añadimos un espacio final al tweet ya que el programa almacena los tweets a cada espacio encontrado, sin esta correción el último hashtag no aparecería en la lista
tweet += " "

#Pasamos por todas las letras del tweet
for char in tweet:
    #Si se encuentra el simbolo # hay dos posibilidades:
    if(char == "#"):
        #No estamos contando un hashtag en el momento y pasamos a contar
        if(not countingHashtag):
            countingHashtag = True
        #Ya estabamos contando un hashtag, por lo tanto se almacena el anterior y reiniciamos el contador para contar uno nuevo
        else:
            #Si el hashtag anterior tiene longitud 1 ("#"), no lo añadimos a la lista. Asi se evitan hashtags duplicados (ej: ##Tweet ####Prueba)
            if(len(contador)>1):
                #Si tiene longitud mayor que 1, lo añadimos a la lista de hashtags
                hashtags.append(contador)
            #Se reinicia el contador
            contador=""
    #Si estamos contando un hashtag y hay un espacio, dejamos de contar
    elif(char == " " and countingHashtag == True):
        countingHashtag = False
        if(len(contador)>1):
            #Almacenamos el hashtag en la lista (si tiene longitud superior a 1)
            hashtags.append(contador)
        #Se reinicia el contador
        contador=""
    #Después de todas las verificaciones, si seguimos contando el hashtag, añadimos la letra actual al contador y pasamos a la siguiente
    if(countingHashtag == True):
        contador += char

print("Hashtags: ", hashtags)
input("")