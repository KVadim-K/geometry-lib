# 📐 Geometry Library ![CI](https://github.com/KVadim-K/geometry-lib/actions/workflows/ci.yml/badge.svg) ![Python](https://img.shields.io/badge/python-3.13-blue.svg)
Небольшая учебная библиотека на **Python**, реализующая вычисление площадей геометрических фигур с акцентом на простую расширяемую архитектуру и юнит-тесты.

## ✨ Возможности

- Вычисление площади **круга** по радиусу (πr²).
- Вычисление площади **треугольника** по трём сторонам (формула Герона).
- Проверка, является ли треугольник **прямоугольным** (по теореме Пифагора с допусками).
- **Фабрика** для создания фигур по строковому имени (без знания типа на этапе написания кода).
- Лёгкое добавление новых фигур через реестр. 

## 🧱 Структура проекта
```
geometry-lib/
├── geometry/
│ ├── init.py # Публичный API библиотеки
│ ├── shapes.py # Абстракции/интерфейсы (Shape, AreaComputable)
│ ├── circle.py # Класс круга
│ ├── triangle.py # Класс треугольника
│ └── factory.py # Фабрика и реестр фигур
├── tests/ # Юнит-тесты (pytest)
│ ├── test_circle.py
│ ├── test_triangle.py
│ └── test_api.py
├── .github/workflows/ci.yml # CI: прогон тестов на GitHub Actions
├── requirements.txt
├── LICENSE
└── README.md
```
---

## ⚙️ Установка

### Вариант 1 — базовый (рекомендуется для Windows)
Установит зависимости для запуска тестов и примеров:
```bash
pip install -r requirements.txt
```
### Вариант 2 — “editable install” (для упаковки/разработки библиотеки)

На Windows иногда мешают блокировки *.egg-info. Если столкнулись с WinError 32 — используйте вариант 1.

```bash
pip install -e .[dev]
```
## ▶️ Пример использования

```python
from geometry.factory import create_shape

circle = create_shape("circle", radius=3)
print(circle.area())  # 28.274333882308138

triangle = create_shape("triangle", a=3, b=4, c=5)
print(triangle.area())     # 6.0
print(triangle.is_right()) # True

```


## 🧪 Тестирование

Запуск всех тестов:
```bash
pytest
```
Ожидаемый результат:

```
11 passed, 0 failed
```

## 🧰 CI/CD

Каждый пуш автоматически запускает тесты на GitHub Actions (Ubuntu, Python 3.11).
Файл конфигурации: .github/workflows/ci.yml.
```yaml
name: CI

on:
  push:
    branches: [ main, master ]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest --maxfail=1 --disable-warnings -q

```
### 📌 Допущения и валидация

* Радиус круга и стороны треугольника должны быть положительными числами.

* Проверяется строгое треугольное неравенство (исключаем вырожденные случаи).

* Для проверки прямоугольности используется math.isclose с микродопусками (устойчиво к float).

## 📄 Лицензия

Проект распространяется по лицензии MIT (см. LICENSE).
## 💻 Автор

[KVadim-K](https://github.com/KVadim-K)


