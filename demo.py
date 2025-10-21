from geometry.factory import create_shape

circle = create_shape("circle", radius=3)
print("Circle area:", circle.area())  # 28.274333882308138

triangle = create_shape("triangle", a=3, b=4, c=5)
print("Triangle area:", triangle.area())      # 6.0
print("Triangle is right:", triangle.is_right())  # True
