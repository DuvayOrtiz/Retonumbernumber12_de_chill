def topp50(text): # Definimos una canción 
    texto = text.split()  # Hacemos un texto separado por el espacio
    for i in range(len(texto)): #revisamos que no sea de caracter numerico
        if not texto[i].isalpha():
            coso1 = texto[i].strip(",;.:-_")  #borramos los signos
            texto.pop(i)
            texto.insert(i, coso1) 
    coso = {} # creamos un  diccionario
    for word in texto:
        if word in coso and word.isalpha():
            coso[word] += 1
        elif word not in coso and word.isalpha():
            coso[word] = 1
    coso2 = [list(coso.items())[i][::-1] for i in range(len(coso))] # se invierte el valor de los 50 
    coso3 = sorted(coso2, reverse=True)[:50]  # ordena la palabras por cantidad
    top50 = [coso3[i][1] for i in range(len(coso3))] # Crea una lista solo con palabras
    return top50
with open("mbox-short.txt", "r") as file:
    print(topp50(file.read()), sep = ",") # Printeo la funcion