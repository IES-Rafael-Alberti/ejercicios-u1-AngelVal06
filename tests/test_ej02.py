import pytest
from src.Ej02_def import importe_total
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_importe_total():
    assert importe_total(1, 1) == 1
    assert importe_total(0, 0) == 0
    assert importe_total(100, 1) == 100

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 1, 1),
        (0, 0, 0),
        (100, 1, 100),
        (15, 1, 15),
        (3, 8, 24),
    ]
)
def test_importe_total_params(input_n1, input_n2, expected):
    assert importe_total(input_n1, input_n2) == expected
