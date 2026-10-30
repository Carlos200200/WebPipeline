##########################################################
#   Word_Count_Raw
# Es el mismo Word_Count, contador de palabras de un archivo txt pero con ciertas modificaciones:
# 1. Ahora solo cuenta de un texto por parametro (sin archivo)
# 2. Esta función la consume flask para su procesamiento web (por eso los parametros)
###########################################################

import string

# Depende de que le llegue un texto ya decodificado
# Ej.: contenido_texto = archivo.read().decode('utf-8')
def Contador_Palabras_Dicc(Archivo_Flask) -> dict:

    # Este es el dicc donde se guardará el conteo
    Contador_Palabras = {}

    for Linea in Archivo_Flask:
        # La decodificacion genera solo texto, entonces se separa por split
        Palabras_Linea = Linea.decode('utf-8').split()
        
        # Se podria usar Regular expressions para mayor eficiencia
        for Palabra in Palabras_Linea:
            # Normalizar la Palabra
            Palabra = Palabra.capitalize() # Minuscula
            Palabra = Palabra.strip(string.punctuation) # Todos los simbolos
            Contador_Palabras[Palabra] = Contador_Palabras.get(Palabra, 0) + 1

    # Resultado
    for PalabraDicc in Contador_Palabras:
        print (f"{PalabraDicc}: {Contador_Palabras[PalabraDicc]}")

    return Contador_Palabras
