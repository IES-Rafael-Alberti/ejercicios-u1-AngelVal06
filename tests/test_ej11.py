import pytest
from src.Ej11_def import calcular_número
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_calcular_número():
    assert calcular_número(23) == "El resultado es 276.0"
