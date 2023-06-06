def contar(texto):
    mensaje = []  # lista para almacenar mensajes
    palabras = texto.split()  # se separan por espacios 
    for i in range(len(palabras)):
        if palabras[i] == "Received:":  
            segmento = []
            while palabras[i] != "-0500" and palabras[i] != "(GMT)":  # Lista de palabras desde "Received" hasta "(GMT)" o "-0500".
                segmento.append(palabras[i])
                i += 1
            mensaje.append(segmento)
    msg_dia = {}  # Hacemos una Diccionario
    for segmento in mensaje:
        indice = segmento.index('Jan')   # Extraer el día basado en el índice de "Jan".
        dia = int(segmento[indice - 1])  
        if dia in msg_dia:
            msg_dia[dia] += 1
        else:
            msg_dia[dia] = 1
    return msg_dia
with open("programacion.txt", "r") as file:
        msg_dia = contar(file.read())
        for dia in msg_dia:
            print(f"Se enviaron {msg_dia[dia]} mensajes enviados el {dia} de enero, 2008") # printeo
