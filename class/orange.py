

# クラス定義
class Orange:
	# インスタンス変数は__init__という特別なメソッドの中で定義し、オブジェクト作成時にPythonから呼び出される
	# __XXX__のようなものを特殊メソッドという
	# インスタンス化
	def __init__(self, w, c):
		# インスタンス変数の生成
		self.weight = w
		self.color = c
		self.mold = 0
		print("Created.!")

	# メソッド定義
	# メソッドでインスタンス変数の値を変更できる
	def rot(self, days, temp):
		self.mold = days * temp

# クラス呼び出し時にself部分は指定しなくていい
orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10,37)
print(orange.mold)



