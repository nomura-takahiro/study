
import csv

with open("csv_test.csv","r") as f:
	# デリミタを","と指定してCSVファイルを読み込む
	r = csv.reader(f,delimiter=",")
	for row in r:
		# CSVファイル記載同様に","で連結した文字列として表示
		print(",".join(row))

		# これで表示するとリストで教示される
		# print(row)



