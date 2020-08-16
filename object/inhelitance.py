
# 継承

# 他のクラスからメソッドや変数を引き継げる

class Shape:
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def print_size(self):
		print("{} by {}".format(self.width, self.len))

# Shapeクラスの子クラス
# Shapeクラスを指定することでメソッドと変数を継承する
class Square(Shape):
	def area(self):
		return self.width * self.len

	# 親クラスと同じメソッドを定義することで上書き(メソッドオーバーライド)できる
	# 上書きすると、親クラス側から呼び出しても上書きされた処理で実行される
	def print_size(self):
		print("I am {} by {}".format(self.width, self.len))



my_shape = Shape(20, 50)
my_shape.print_size()

a_square = Square(10,100)
a_square.print_size()
print(a_square.area())
a_square.print_size()


