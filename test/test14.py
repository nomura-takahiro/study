
# test14

# ①
class Square:
	square_list = []

	def __init__(self, l):
		self.len = l
		self.square_list.append(self)

	def __repr__(self):
		return ("{} by {} by {} by {}".format(self.len, self.len, self.len, self.len))

	def compare(self, obj1, obj2):
		return obj1 is obj2


s1 = Square(30)
s2 = Square(40)

print(Square.square_list)
print(s1)
print(s2)

print(s1.compare(s1,s2))
print(s1.compare(s1,s1))

