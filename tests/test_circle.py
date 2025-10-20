"""Тесты круга: площадь, ошибки валидации."""
import math
import pytest
from geometry import Circle

def test_circle_area_unit_radius():
    c = Circle(1)
    assert math.isclose(c.area(), math.pi, rel_tol=1e-12)

def test_circle_area_typical():
    c = Circle(5)
    assert math.isclose(c.area(), math.pi * 25, rel_tol=1e-12)

def test_circle_invalid_radius_type():
    with pytest.raises(TypeError):
        Circle("3")  # type: ignore[arg-type]

def test_circle_invalid_radius_value():
    with pytest.raises(ValueError):
        Circle(0)
