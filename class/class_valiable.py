

class Rectangle:
	# クラス変数
	# クラスオブジェクトからも、本クラスのインスタンスオブジェクトからも参照できる
	recs = []

	def __init__(self, w, l):
		self.width = w
		self.len = l
		# クラス変数に設定
		self.recs.append((self.width, self.len))

	def print_size(self):
		print("{} by {}".format(self.width, self.len))


r1 = Rectangle(10,24)
r2 = Rectangle(20,40)
r3 = Rectangle(100,200)

print(Rectangle.recs)
for i in r1.recs:
	print(i)

