
# test12

import math


# ①
class Apple:
	# インスタンス化
	# ①色、②重さ、③産地、④状態
	def __init__(self, color, weight, origin, status):
		self.color = color
		self.weight = weight
		self.origin = origin
		self.status = status

# 実処理
apple = Apple("red", 400, "青森", "flesh")
print(apple.color)
print(apple.weight)
print(apple.origin)
print(apple.status)



# ②
class Circle:
	def __init__(self, rad):
		self.radius = rad

	# 円の面積を算出
	def area(self):
		return (self.radius * self.radius) * math.pi

# 実処理
circle = Circle(5)
print(circle.radius)
print(circle.area())



# ③
class Triangle:
	def __init__(self, l, h):
		self.length = l
		self.height = h

	# 三角形の面積を算出
	def area(self):
		return (self.length * self.height) / 2

# 実処理
triangle = Triangle(10, 4)
print(triangle.length)
print(triangle.height)
print(triangle.area())



# ④
class Hexagon:
	# 正六角形の1辺の長さを設定
	def __init__(self, l):
		self.len = l

	# 外周の長さを算出
	def calculate_perimeter(self):
		return self.len * 6

# 実処理
hexagon = Hexagon(6)
print(hexagon.len)
print(hexagon.calculate_perimeter())











