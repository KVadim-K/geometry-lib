"""Тесты фабрики и duck typing API."""
import math
from geometry import Circle, Triangle, create_shape, compute_area

def test_factory_and_duck_typing():
    c = create_shape("circle", radius=2)
    t = create_shape("triangle", a=3, b=4, c=5)
    assert isinstance(c, Circle)
    assert isinstance(t, Triangle)
    assert math.isclose(compute_area(c), math.pi * 4, rel_tol=1e-12)
    assert math.isclose(compute_area(t), 6.0, rel_tol=1e-12)

class Dummy:
    """Простой объект с методом area() для демонстрации duck typing."""
    def area(self) -> float:
        return 42.0

def test_duck_typed_object():
    d = Dummy()
    assert compute_area(d) == 42.0
