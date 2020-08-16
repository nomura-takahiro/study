
##################
###   文字列   ###
##################

#文字列はイミュータブルらしい
#基本的には文字列を変更する場合は新規文字列とする
#※replace()メソッドを使えば変更可能

name = "nomura"
print(name[0])
print(name[1])

#Pythonの場合、マイナス値をindexとした場合、最後尾から参照する
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])


#連結
print("Nomu" + "ra" + "Takahi" + "ro")

#掛け算
print("Nomura"*3)

#大文字変換
print("nomura".upper())

#小文字変換
print("NOMURA".lower())

#最初の文字を大文字
print("nomura".capitalize() + "takahiro".capitalize())


