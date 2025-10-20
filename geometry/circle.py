"""Круг: площадь по формуле πr², базовая валидация радиуса."""
from __future__ import annotations
import math
from dataclasses import dataclass
from .shapes import Shape

@dataclass(frozen=True)
class Circle(Shape):
    radius: float  # радиус > 0

    def __post_init__(self) -> None:
        if not isinstance(self.radius, (int, float)):
            raise TypeError("radius must be a number")
        if self.radius <= 0:
            raise ValueError("radius must be > 0")

    def area(self) -> float:
        """Возвращает площадь круга: π * r^2."""
        return math.pi * (self.radius ** 2)
