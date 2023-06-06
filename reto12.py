def contvoc(texto): # Hacemos una función
    s = 0 # Hacemos un contador 
    for voc in texto: # Buscamos las vocales en el texto
        if voc in "AEIOUaeiou": # Revisamos que esten las vocales
            voc += 1 # Sumamos al contador
    return voc # retornamos el contador con la cantidad
with open("mbox-short.txt", "r") as file:
    texto = file.read()
print("La cantidad de vocales del texto es ", contvoc(texto)) # printeamos la funcion