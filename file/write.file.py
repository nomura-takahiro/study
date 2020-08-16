
import datetime

# 現在日時を取得
dt_now = datetime.datetime.now()
trans_time = dt_now.strftime('%Y/%m/%d %H:%M:%S')

#st = open("test.txt","r")
#st = open("test.txt","r+")
#st = open("test.txt","w")
#st = open("test.txt","w+")
st = open("test.txt","a")
st.write(trans_time)
st.write(" Writtend.\n")

# 日本語文字列を書き込む場合はopen()の第3引数に文字コードを指定
# open("test.txt","a","encoding="utf-8")

st.close()

# ファイル全体を文字列として読み込み
# read()

# ファイル全体をリストとして読み込み
# readlines()

# ファイルを1行ずつ読み込み
# readline()

# リストを書き込み
# writelines()

# 空ファイル作成
# pass文

# ファイルが存在しない場合のみ書き込み
# 新規作成用でファイルオープン：mode='x'
# ファイルの存在を確認してからオープン

# テキストファイルの書き込み(追記・挿入
# 末尾に追記：mode='a'
# 先頭・途中に挿入
#  mode='r+'
#  readlines() / insert()






