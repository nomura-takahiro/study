
#test7

#①
favorite_musician = [
		"宇多田ヒカル",
		"BUMP OF CHICKEN",
		"スキマスイッチ",
]
print(favorite_musician)


#②③
travel = [
	{
		"草津":(36.62,138.59),
		"熱海":(35.09,139.07),
		"黒部":(36.87,137.44),
		"玉造":(35.41,133.00),
	}
]

print(travel)
print(travel[0]["熱海"])


#④
place = input("行ったことのある旅行先を入れて >> ")
if place in travel[0]:
	print("行ったことあったよ")
	print(travel[0][place])
else:
	print("行ったことなかったよ")


#⑤
musician_list = {
		"宇多田ヒカル":["ぼくはくま","Traveling","桜流し","Colours","光","automatic","Beautiful World"],
		"BUMP OF CHICKEN":["車輪の唄","Ray","アルエ","涙のふるさと","カルマ"],
		"スキマスイッチ":["ボクノート","アイスクリームシンドローム","藍"],
}
print(musician_list)
print(musician_list["スキマスイッチ"])
print(musician_list["BUMP OF CHICKEN"])
print(musician_list["宇多田ヒカル"])

