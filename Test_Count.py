import pytest
from Word_Count_Raw import Contador_Palabras_Dicc

def test_archivo_simple():
    with open('TextodePrueba.txt', 'rb') as Archivo:
        assert Contador_Palabras_Dicc(Archivo) == {'Este': 1, 'Es': 1, 'Un': 1, 'Texto': 1, 'De': 1, 'Prueba': 1, 'Deberia': 1, 'Leer': 1, 'Esta': 1, 'Linea': 1, 'Hay': 1, 'Mas': 2, 'Y': 1, 'Todavia': 1}

def test_archivo_simbolos():
    with open('HolaMundo.txt', 'rb') as Archivo:
        assert Contador_Palabras_Dicc(Archivo) == {'Hola': 6, 'Holá': 1, 'Mundo': 6, 'Mundó': 1}

def test_archivo_vacio():
    with open('TextoVacio.txt', 'rb') as Archivo:
        assert Contador_Palabras_Dicc(Archivo) == {}

# Esto se pone en la 2da fase, para hacer modificaciones en GIT
##def test_archivo_invalido():
##    assert

