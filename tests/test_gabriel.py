import sys
import os

# Agrega la carpeta raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from Examen2 import MiClase   # Asegúrate que Examen2.py está en la carpeta raíz del proyecto

# -------------------------------------------------
# FIXTURE: crea un objeto de MiClase reutilizable
# -------------------------------------------------
@pytest.fixture
def objeto():
    return MiClase(5, 120, 12, [], [])

# -------------------------------------------------
# PRUEBAS PARA ObtieneValencia
# -------------------------------------------------

def test_obtiene_valencia_con_digitos_impares(objeto):
    # 13579 → todos son impares → 5
    assert objeto.ObtieneValencia(13579) == 5

def test_obtiene_valencia_sin_digitos_impares(objeto):
    # 24680 → ninguno impar → 0
    assert objeto.ObtieneValencia(24680) == 0

# -------------------------------------------------
# PRUEBAS PARA DivisibleTempo
# -------------------------------------------------

def test_divisible_tempo_numero_pequenno(objeto):
    # divisores de 6 → [1, 2, 3, 6]
    assert objeto.DivisibleTempo(6) == [1, 2, 3, 6]

def test_divisible_tempo_primo(objeto):
    # 7 es primo → [1, 7]
    assert objeto.DivisibleTempo(7) == [1, 7]
