
###############
###  index  ###
###############

# 文字を探す

name = "Nomura"
#index()に指定した文字のindex値を返す
print(name.index("m"))

#大文字小文字は分けられて認識される
try:
	print(name.index("N"))   #OK
	print(name.index("n"))   #NG
except:
	print("Not find.")


