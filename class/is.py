
class Person:
	def __init__(self):
		self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)


x = 10
if x is None:
	print("x is None : ( ")
else:
	print("x is not None")

x = None
if x is None:
	print("x is None")
else:
	print("x is not None : ( ")


