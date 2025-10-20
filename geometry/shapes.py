"""Базовые интерфейсы фигур."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol

class Shape(ABC):
    """Абстрактная фигура: все фигуры обязаны реализовать area()."""
    @abstractmethod
    def area(self) -> float:
        """Площадь фигуры в квадратных единицах."""
        raise NotImplementedError

class AreaComputable(Protocol):
    """Протокол для объектов, у которых есть метод area()."""
    def area(self) -> float: ...
