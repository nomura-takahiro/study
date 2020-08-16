
def division(x):
	"""
	Returns x / 2
	:param x : int.
	return division x by 2
	"""
	return x / 2

def multiplication(y):
	"""
	Returns y * 4
	:param y : int.
	return multiplication y by 4
	"""
	return y * 4


tmp = input(" Input num >> ")
try:
	tmp = int(tmp)
	first = division(tmp)
	print(first)
	#ここで整数に変換しないと結果が異なる
	first = int(first)
	result = multiplication(first)
	print(result)
except (ValueError, TypeError):
	print(" Invalid Input")



