import pytest
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from Examen2 import MiClase

def test_ObtieneMasBailable_NumerosIguales():
    miClase = MiClase(5, 120, 12, [], [])
    lista = [0.9, 0.9, 0.9, 0.9]

    resultado = miClase.ObtieneMasBailable(lista)
    assert resultado == 0.9

def test_ObtieneMasBailable_ListaVacia():
    miClase = MiClase(5, 120, 12, [], [])
    lista = []

    resultado = miClase.ObtieneMasBailable(lista)
    assert resultado is None

def test_VerificaListaCanciones_ListaConContenido():
    miClase = MiClase(5, 120, 12, [], [])
    lista = ["Canción 1", "Canción 2", "Canción 3"]

    resultado = miClase.VerificaListaCanciones(lista)
    assert resultado == True

def test_VerificaListaCanciones_ListaNone():
    miClase = MiClase(5, 120, 12, [], [])
    lista = [None]

    resultado = miClase.VerificaListaCanciones(lista)
    assert resultado == False