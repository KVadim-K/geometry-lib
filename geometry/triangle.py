"""Треугольник: площадь по Герону, проверка прямоугольности."""
from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Tuple
from .shapes import Shape

@dataclass(frozen=True)
class Triangle(Shape):
    a: float
    b: float
    c: float

    def __post_init__(self) -> None:
        # Валидация типов и знаков
        for name, val in (("a", self.a), ("b", self.b), ("c", self.c)):
            if not isinstance(val, (int, float)):
                raise TypeError(f"{name} must be a number")
            if val <= 0:
                raise ValueError(f"{name} must be > 0")
        # Треугольное неравенство
        a, b, c = self.a, self.b, self.c
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("triangle inequality violated")

    def area(self) -> float:
        """Площадь по формуле Герона."""
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        s = p * (p - a) * (p - b) * (p - c)
        return math.sqrt(max(s, 0.0))

    def is_right(self, *, rel_tol: float = 1e-9, abs_tol: float = 1e-12) -> bool:
        """True, если треугольник прямоугольный (Пифагор с допусками)."""
        x, y, z = self._sorted_sides()
        return math.isclose(z*z, x*x + y*y, rel_tol=rel_tol, abs_tol=abs_tol)

    def _sorted_sides(self) -> Tuple[float, float, float]:
        """Возвращает стороны по возрастанию (вспомогательный метод)."""
        return tuple(sorted((self.a, self.b, self.c)))  # type: ignore[return-value]
