
import csv

with open("csv_test.csv","a",newline='') as f:
	# writer:デミリタ(区切り文字)を","に指定
	w = csv.writer(f, delimiter=",")
	# writerow:引数にリストを受け取り、CSVファイルに書き込む
	w.writerow(["one","two","three"])
	w.writerow(["four","five","six"])


