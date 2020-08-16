
# test11

import os
import csv

#①
file_path = os.path.join("/home","nomura","HOME_TOP","WORK","C","sdp","sdp_text.txt")
#print(file_path)

with open(file_path,"r",encoding="utf-8") as f:
	print(f.read())
	

#②
"""
text = input(" What your name ? >> ")
with open("output.txt","a") as w:
	w.write(text)
	w.write("\n")
"""

#③
_list = [
		["Top Gun","Risky Business","Minority Report"],
		["Titanic","The Revenant","Inception"],
		["Training Day","Man on Fire","Flight"]
		]

with open("test11.csv","a",newline='') as f:
	# writer:デミリタ(区切り文字)を","に指定
	w = csv.writer(f, delimiter=",")
	# writerow:引数にリストを受け取り、CSVファイルに書き込む
	for i in _list:
		w.writerow(i)


#④
ja_list = 	[
			["ウルフ・オブ・ウォールストリート","ライフ","マイレージ・マイライフ"],
			["銀魂","クラナド","天元突破グレンラガン"],
			["ワンピース","鬼滅の刃","トリコ"]
			]

with open("test11.csv", "a", encoding="utf-8") as f:
	w = csv.writer(f, delimiter=",")
	for i in ja_list:
		w.writerow(i)



