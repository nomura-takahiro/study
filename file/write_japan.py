
# ファイルクローズ防止の1つの構文

import datetime
dt_now = datetime.datetime.now()
trans_time = dt_now.strftime('%Y/%m/%d %H:%M:%S')


# ファイルオブジェクトを"f"に割り当て、処理実行後自動的にファイルを閉じる
with open("test.txt","a",encoding="utf-8") as f:
	f.write(trans_time)
	f.write(" with Opneから書き込んでいます.\n")



