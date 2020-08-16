
def squared(x):
	"""
	Returns x ** 2
	:param x : int.
	return squared x^2
	"""
	return x**2

try:
	x = input(" Input num >> ")
	x = int(x)
except (ValueError, TypeError):
	print(" Invalid Input")

try:
	print(squared(x))
except TypeError:
	print(" x is TypeError")

