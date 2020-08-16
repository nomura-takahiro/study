
# test9

#①
text = ["ウォーキング・デッド","アンとらーじゅ","ザ・ソプラノ図","ヴァンパイア・ダイアリー図"]
for idx in text:
	print(idx)


#②
for i in range(25,51):
	print(i)


#③
"""
for idx in text:
	print("{} index[{}]".format(idx,text.index(idx)))
"""

#④
num = [12,19,24,50,98,110,67,82,2]
while True:

	match_flg = 0

	ans = input("Input number (type 'q' to stop) >> ")

	if ans == 'q':
		print("End.")
		break
	try:
		ans = int(ans)
		for i in num:
			if i == ans:
				match_flg = 1
			else:
				continue

		if match_flg == 1:
			print("Correct Answer.")
		else:
			print("Incorrect Answer.")

	except:
		print("Invalid Input.")


#⑤
first = [8,19,148,4]
second = [9,1,33,83]

for i in first:
	for j in second:
		print(i * j)




