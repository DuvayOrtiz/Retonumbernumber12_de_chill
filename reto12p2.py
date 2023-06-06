def contvoc(texto): # Hacemos una función
    s = 0 # Hacemos un contador
    for con in texto: # Buscamos las vocales en el texto
        if con.isalpha() and con not in "AEIOUaeiou":  # Revisamos que no sea numero y no sea vocal
            con += 1 # Sumamos al contador
    return con # retornamos el contador con la cantidad
with open("mbox-short.txt", "r") as file:
    texto = file.read()
print("La cantidad de consonantes del texto es ", contvoc(texto)) # printeamos la funcion