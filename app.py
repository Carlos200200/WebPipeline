##########################################################
#   app.py
# Es donde flask busca para iniciar la webpage, aqui es todo el 
# procesamiento de la pagina
###########################################################

from flask import Flask, render_template, request

# Trayendo la funcion de conteo
from Word_Count_Raw import Contador_Palabras_Dicc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    Resultado = None
    if request.method == 'POST':
        archivo = request.files.get('archivo_txt')
        if archivo and archivo.filename != '':         
            
            # Aqui se hace la operación del conteo
            Resultado = Contador_Palabras_Dicc(archivo)
            
    return render_template('index.html', resultado=Resultado)

if __name__ == '__main__':
    app.run(debug=True)
