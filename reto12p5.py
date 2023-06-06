def reci(text): # Hacemos una función
    palabras = text.split() 
    desti = {}  # Diccionario que contiene los destinatarios
    for i in range(len(palabras)):
        if (palabras[i] == "by" or palabras[i] == "BY") and "." in palabras[i-1]:  # Revisar que hayan by y BY
            if palabras[i+1] in desti: 
                desti[palabras[i+1]] += 1
            else:
                desti[palabras[i+1]] = 1  
    listado = list(desti.items())  #Lista de tuplas que contiene el destinatario y los mensajes dados a el 
    return listado
with open("mbox-short.txt", "r") as file:
    coso = reci(file.read())
    for i in range(len(coso)):
        lenstr = len(coso[i])
        print(*coso[i], sep=(5*" "),end="\n") # printeo