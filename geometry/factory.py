"""Фабрика и реестр фигур для динамического создания по имени."""
from __future__ import annotations
from typing import Any, Dict, Type
from .shapes import Shape, AreaComputable
from .circle import Circle
from .triangle import Triangle

# Регистрация доступных фигур: легко расширить register_shape(...)
_SHAPE_REGISTRY: Dict[str, Type[Shape]] = {
    "circle": Circle,
    "triangle": Triangle,
}

def register_shape(name: str, cls: Type[Shape]) -> None:
    """Регистрирует новый класс фигуры под строковым ключом."""
    _SHAPE_REGISTRY[name.strip().lower()] = cls

def create_shape(name: str, /, **kwargs: Any) -> Shape:
    """Создаёт фигуру по имени без знания типа на этапе написания кода."""
    key = name.strip().lower()
    try:
        cls = _SHAPE_REGISTRY[key]
    except KeyError as exc:
        raise ValueError(f"Unknown shape: {name}") from exc
    return cls(**kwargs)  # type: ignore[arg-type]

def compute_area(shape: AreaComputable) -> float:
    """Вычисляет площадь у любого объекта с методом area() (duck typing)."""
    return shape.area()
