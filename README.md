# Geometry


Минималистичная библиотека на Python для расчёта площади круга и треугольника, с акцентом на простую расширяемую архитектуру, юнит‑тесты и пример фабрики.


## Возможности


- `Circle(radius)` → `area()` считает πr²
- `Triangle(a,b,c)` → `area()` по формуле Герона
- `Triangle.is_right()` проверяет прямоугольность (Пифагор с допусками)
- `compute_area(obj)` считает площадь у любого объекта с методом `.area()`
- `create_shape(name, **kwargs)` фабрика и реестр фигур (легко добавлять новые)


## Установка (локально для разработки)


```bash
python -m venv .venv
source .venv/bin/activate # Windows: .venv\\Scripts\\activate
pip install -e .[dev]