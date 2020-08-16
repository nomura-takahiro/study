
def trans(str):
	"""
	Returns float(str)
	:param str : string
	return transfer str to float
	"""
	try:
		result = float(str)
		return result
	except (ValueError, TypeError):
		print(" Error : Invalid Input")


tmp = input(" Input num >> ")
#if (print(trans(tmp)) is None) :  #同値性の評価
if (print(trans(tmp)) == None) :   #同一性の評価
	print("func trans Error")
else:
	print(" func trans OK")



