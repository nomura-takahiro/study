
################
###  ループ  ###
################

#for
text = "Nomura"
#デフォルトで in XXXに指定したものから1要素ずつを取り出すっぽい
for char in text:
	print(char)

tmp = ["Nomura","Baz","Jista"]
#リストの1要素ずつを出力
for li in tmp:
	print(li)

#ミュータブルなものなら更新ができる
i = 0
for li in tmp:
	new = tmp[i]
	new = new.upper()
	tmp[i] = new
	i += 1
print(tmp)

#上記方法でもいいが、下の方式がメジャーらしい
tmp = ["Nomura","Baz","Jista"]
for i, new in enumerate(tmp): #こうすることでindex値のインクリメントが不要
	new = tmp[i]
	new = new.upper()
	tmp[i] = new
print(tmp)


tmp2 = {"Red":"Apple",
	   "Yello":"Banana",
	   "Green":"Melon"
	  }
#辞書の場合、キーを取り出す
for fruit in tmp2:
	print(fruit)

#range
#for i in range(10):
for i in range(0,10): #本来range()は引数2つらしい
	print(i)

for i in range(len(tmp)):
	print(tmp[i])


#========================================================================================================================

################
###  while   ###
################

x = 10
while x > 0:
	print(x)
	x-= 1

print("End.")


x = 10
while x > 0:
	print(x)
	break
	x-= 1
print("End.")

#ある処理を繰り返す
qs = ["What your name? >> ",
	  "What your age?  >> ",
	  "What your birth? >>" 
	 ]
"""
idx = 0
print("Type [q] to stop.")
while True:
	ans = input(qs[idx])
	if ans == "q":
		break
	# %演算で右辺より左辺が小さい場合は、結果は左辺が使われる
	idx = (idx + 1) % len(qs)
"""

index = 0
for index in range(10):
	if index == (5):
		continue
	print(index)

