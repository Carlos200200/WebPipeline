##########################################################
#   Word_Count_Web
# Es el mismo Word_Count, contador de palabras de un archivo txt pero con ciertas modificaciones:
# 1. Una carpeta de busqueda de arhcivos
# 2. Muestra en un archivo web, usando Flask
###########################################################

import sys
import string

import os
from flask import Flask, render_template, request, current_app

app = Flask(__name__)

# Ruta dentro del contenedor donde va a buscar los archivos (la otra ver era en ".")
CARPETA_ARCHIVOS = "/app"

print("Cantidad de argumentos:", len(sys.argv))
#print("Nombre del programa:", sys.argv[0])

@app.route('/')
def index():
    # Lee los datos guardados en la configuración de Flask
    datos = current_app.config.get('RESULTADO_CONTEO')
    error = current_app.config.get('ERROR_CONTEO')
    # Por defecto render_template busca en la carpeta ""
    return render_template('indexWeb.html', resultado=datos, error=error)


def main():
    # Arg 0 es nombre del programa
    if len(sys.argv) < 2:
        print("Uso: python programa.py <Archivo.txt>")
        return

    print("Archivo para Contar: ", sys.argv[1])

    Nombre_Archivo = sys.argv[1]
    #Ruta_Completa = os.path.join(CARPETA_ARCHIVOS, Nombre_Archivo)

    Contador_Palabras = {}

    with open(Nombre_Archivo, "r", encoding="utf-8") as Archivo:
        for Linea in Archivo:
            #print(Linea.strip())
            Palabras_Linea = Linea.split()

            for Palabra in Palabras_Linea:
                # Normalizar la Palabra
                Palabra = Palabra.capitalize() # Minuscula
                Palabra = Palabra.strip(string.punctuation) # Todos los simbolos
                Contador_Palabras[Palabra] = Contador_Palabras.get(Palabra, 0) + 1

    # Resultado
    for PalabraDicc in Contador_Palabras:
        print (f"{PalabraDicc}: {Contador_Palabras[PalabraDicc]}")

    # Mandando el resultado al index
    app.config['RESULTADO_CONTEO'] = {
                    "archivo": Nombre_Archivo,
                    "palabras": Contador_Palabras
             }

    # Una vez procesado inicia el servicio web en Flask
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()


