import pytest
from src.ej05_def2 import calcular_iva
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_calcular_iva():
    assert calcular_iva(23, 21) == "El precio final del artículo con IVA (21.00) es 27.83€."
