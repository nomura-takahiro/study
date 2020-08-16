
#クラス定義

# 矩形クラス
class Rectangle:
	# 幅と長さを設定
	def __init__(self, w, l):
		self.width = w
		self.len = l

	# 面積を算出
	def area(self):
		return self.width * self.len

	# サイズ変更
	def change_size(self, w, l):
		self.width = w
		self.len = l


# 実処理
rectangle = Rectangle(10,20)
# 10 *"20 の面積を算出 = 200
print(rectangle.area())
# サイズを変更(Rectangleクラス型？なのでメソッドで呼び出し可能)
rectangle.change_size(20,40)
# 20 * 40の面積を算出 = 800
print(rectangle.area())

