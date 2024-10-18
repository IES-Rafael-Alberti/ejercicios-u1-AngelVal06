import pytest
from src.Ej01_def import hola_nombre
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_hola_nombre():
    assert hola_nombre("pepe") == "Hola, pepe"
    assert hola_nombre("pepe") == "Hola, pepe"
    assert hola_nombre("pepe") == "Hola, pepe"

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("pepe", "Hola, pepe"), 
        ("pepe", "Hola, pepe"),
        ("pepe", "Hola, pepe"),
        ("pepe", "Hola, pepe"),
        ("pepe", "Hola, pepe"),
    ]
)
def test_hola_nombre_params(input_n1, expected):
    assert hola_nombre(input_n1) == expected
