
# コンポジション
# 「has-a関係」：別クラスのオブジェクトを変数として持たせる

class Dog:
	def __init__(self, name ,breed, owner):
		self.name = name
		self.breed = breed
		self.owner = owner

class Person:
	def __init__(self, name):
		self.name = name	

nomura = Person("Nomura Takahiro")
cockie = Dog("Cockie", "hyblid", nomura)
print(cockie.owner.name)


