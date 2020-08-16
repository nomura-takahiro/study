
###################
###   タプル    ###
###################

# 好きな順番でオブジェクトを保存しておけるコンテナ
# イミュータブル（変更不可）

my_tuple = tuple()
print(my_tuple)  # ()

my_tuple2 = ()
print(my_tuple2)

my_tuple = ("Nomura", 1994, 1, 15)
print(my_tuple)

#タプルの要素数が1つの場合は、最後に「,」が必要
#でないとPythonは数値演算の優先度を決めるための()だと認識してしまう
#※表示は出来るが、タプルとして認識はされないみたい
my_tuple2 = ("Takahiro",)  # ('Takahiro')と表示される
#my_tuple2 = ("Takahiro")  # Takahiroと表示される
print(my_tuple2)

#my_tuple[1] = "Kikuchi"  #変更しようとすると例外となる(TypeError)

#取り出し方はリストと同じ
print(my_tuple[1])

print("Nomura" in my_tuple)
print("Nomura" not in my_tuple)


