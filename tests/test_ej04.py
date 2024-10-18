import pytest
from src.ej04_def2 import pasar_celsius_a_farenheit
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_pasar_celsius_a_farenheit():
    assert pasar_celsius_a_farenheit(22) == -5.56

