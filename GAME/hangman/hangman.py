
import random

def hangman(word):
	# ハングマン
	# 引数の単語を充てるゲーム

	# 間違えた回数
	wrong = 0
	stages = ["",
			  "____________       ",
			  "|                  ",
			  "|          |       ",
			  "|          O       ",
			  "|         /|/      ",
			  "|         | |      ",
			  "|                  ",
			 ]

	# 正解となる単語を1文字ずつにリスト化
	rletters = list(word)
	# 単語の文字数分アンダーバー
	board = ["_ "] * len(word)
	win = False
	print("\nハングマンへようこそ!")
	print("1文字ずつ入力して正解の単語を導き出してね。")
	print("英単語の場合は大文字と小文字は区別されるよ。")

	# ゲーム処理

	# 絵が完成するまでループ
	while wrong < len(stages) -1 :
		print("\n")
		msg = "1文字予想してね >> "
		char = input(msg)

		# 入力文字が正解に含まれるかチェック
		if char in rletters:
			# 正解単語内に含まれていれば以下処理
			# 入力された文字のindex値を求める
			cind = rletters.index(char)
			# アンダーバーの箇所を入力文字で上書き
			board[cind] = char
			# 入力文字の箇所を'$'に上書き
			rletters[cind] = '$'
		else:
			wrong += 1

		# 現在の正解状況を表示
		#print("".join(board))

		e = wrong + 1
		# 間違えた回数分のハングマンを表示する
		print("\n".join(stages[0:e]))
		print("\n")
		# 正解している入力文字を連結して表示
		print("".join(board))

		# 未正解箇所がないかチェック
		if "_ " not in board:
			print("You Win !\n")
			print("".join(board))
			win = True
			break

	# ループ終了段階で勝ち負けの判定
	if not win:
		print("\n".join(stages[0:wrong + 1]))
		print("You Lose..")
		print("Answer {}".format(word))


# 正解となる単語を入力
#answer = input(" 好きな単語を入れて >>  ")
ans_list = ["Nomura","Takahiro","Kikuchi","Saori"]

# 登録しているリストからランダムにindex値を取得
ind = random.randint( 0, (len(ans_list) - 1) )
hangman(ans_list[ind])


