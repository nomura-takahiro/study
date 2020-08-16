
#################
###   slice   ###
#################

#リストや文字列の開始：終了indexを指定できる

food = ["protain","banana","saba","egg","tomato"]

#終了index値の1つ手前までを指定できる
print(food[0:3]) # "saba"まで(2)

#文字列の場合は1文字ずつのindexとなる
name = "Nomura Takahiro"
print(name[0:8]) #Nomura T まで

#開始、終了を省略もできる
print(name[:2])  #先頭から1まで
print(name[7:])  #7から最後まで
print(name[:])   #先頭から最後まで



