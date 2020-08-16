
class Lion:
	def __init__(self, name):
		self.name = name

	# 特殊メソッド
	# print()にオブジェクトを渡すと、objectクラスから継承した__repr__メソッドを呼び出し、
	# 返ってきた値を出力する
	# __repr__メソッドをオーバーライドして出力したい内容に変更が可能
	def __repr__(self):
		return self.name


lion = Lion("Cha-")
# _repr__をオーバーライドしないとアドレスを表示する
print(lion)
print(Lion)


class AlwaysPositive:
	def __init__(self, number):
		self.n = number

	# 整数値は特殊メソッド__add__を持っている
	def __add__(self, other):
		return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)





