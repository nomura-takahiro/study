
#exception = 10 / 0
#print(exception)

#y = 1
#pythonでは変数は半角空白、タブもだめ
# x = 0

#tryは何か処理(int()や自作関数など)の処理結果に対して、
#結果が例外となるかどうかの判定をするものっぽい
#try内に記載している処理の中で、exceptに指定している例外が起きたら、except側の処理へ移行する処理みたい

a = input("first >> ")
b = input("second >> ")
a = int(a)
b = int(b)
try:
	print(a / b)
except ZeroDivisionError:
	# 例外となった場合に以下を表示する
	print("b cannot be zero")


#整数を期待し、文字列など整数以外の入力で例外となる場合
x = input("third >> ")
y = input("force >> ")
x = int(x)
y = int(y)

try:
	#以下を外に出して、入力が文字列の場合、int()で例外となるため、try内にする必要がある
	#x = input("third >> ")
	#y = input("force >> ")
	#x = int(x)
	#y = int(y)
	print(x / y)
except(ZeroDivisionError, ValueError):
	print("Invalid Input")

#except節内で、try内で定義する変数を使用することはNG
#except内に行く前に例外が起きた場合、別の例外となる
try:
	10 /0
	z = "先に例外が発生"
except ZeroDivisionError:
	print(z)


