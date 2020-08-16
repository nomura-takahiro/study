
def total(a, b, c, x=100, y=1000):
	"""
	Returns a + b + c + x + y
	:param a : int.
	:param b : int.
	:param c : int.
	return sum of from a to y
	"""
	return a + b + c + x + y

a = input(" First  num >> ")
b = input(" Second num >> ")
c = input(" Third  num >> ")
try:
	a = int(a)
	b = int(b)
	c = int(c)
	print(total())
except (ValueError, TypeError):
	print(" Invalid Input")



