"""Публичный API библиотеки geometry."""
from .shapes import Shape
from .circle import Circle
from .triangle import Triangle
from .factory import create_shape, compute_area

__all__ = ["Shape", "Circle", "Triangle", "create_shape", "compute_area"]
