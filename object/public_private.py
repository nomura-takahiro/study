
# Pythonにはプライベート変数はなく、パブリック変数
# Pythonではアクセスしてほしくない変数、メソッドには先頭にアンダーラインを付ける
# ※自己責任で使うってもいいけど。。

class PublicPrivate:
	def __init__(self):
		# 使ってもいい
		self.public = "safe"
		# 使うべきではない
		self,_unsafe = "unsafe"

	def public_method(self):
		# 使ってもいい
		# pass文は文が必須な構文で何もしない意味
		pass

	def _unsafe_method(self):
		# 使うべきではない
		pass

