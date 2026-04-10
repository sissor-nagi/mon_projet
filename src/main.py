def addition(a, b):
return a + b
tests/test_main.py
from src.main import addition
def test_addition():
assert addition(2, 3) == 5
