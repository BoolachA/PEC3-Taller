tweet = input("Tweet: ")
hashtags = []
correcion = []
palabra=""
countHashtag = False


for x in tweet:
    if(x == "#"):
        if(not countHashtag):
            countHashtag = True
        else:
            if(len(palabra)>=1):
                hashtags.append(palabra)
            palabra=""
    elif(x == " "):
        countHashtag = False
        if(len(palabra)>=1):
                hashtags.append(palabra)
        palabra=""

    if(countHashtag == True):
        palabra += x

print(hashtags)