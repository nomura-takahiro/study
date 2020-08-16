
##################
###  メソッド  ###
##################

#オブジェクトに付けて呼び出す

# 大文字に
print("Hello".upper())

# 特定文字を置換
print("Hello".replace("l","1"))


##################
###   リスト   ###
##################

#配列のようなもの
fruit = list()  # []
name = [] #list()と同じ
print(fruit)
print(name)

fruit = ["Apple","Orange"]
print(fruit)

# リスト最後に追加
fruit.append("Banana")
fruit.append("Peach")
print( ".append")
print(fruit)

_list = []
print(_list)

_list.append(100)
_list.append("Nomura")
_list.append(3.00)
_list.append("A")
print(_list)
#print(_list[0])
#print(_list[1])
#print(_list[2])
#print(_list[3])
#print(_list[4])  #何もないところの参照は例外

#_list[2]=3.0をTakahiroに書き換え
_list[2] = "Takahiro"
print(_list)

#リスト最後の要素を取り除く	
Pop = _list.pop()
print("Pop")
print(_list)
print(Pop)


name = ["Kikuchi"]
name2 = ["Saori"]
print("連結(+)")
print(name + name2)

#要素検索
print("Nomura" in _list)
print("Kikuchi" in _list)
print("Kikuchi" not in _list)
#notは以下でも同じだが、inが先に評価され、その後notが評価されるため、not inが推奨
print(not "Kikuchi" in _list)

#リストのサイズ(要素数)
print(len(_list))  #3
print(len(name))   #1


