import pytest
from src.prueba1 import comprobar_numero
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_comprobar_numero():
    assert comprobar_numero(1, 1) == 0
    assert comprobar_numero(0, 0) == 0
    assert comprobar_numero(100, -100) == 100

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 1, 0),
        (0, 0, 0),
        (100, -100, 100),
        (-15, -1, -1),
        (-3, 8, 8),
    ]
)
def test_comprobar_numero_params(input_n1, input_n2, expected):
    assert comprobar_numero(input_n1, input_n2) == expected
