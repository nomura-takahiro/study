
################
###   辞書   ###
################

# 辞書はリスト/タプルとはまた別のオブジェクトを保存しておくための組み込みコンテナ
# 2つのオブジェクトを関連付けて保存するコンテナ
# 格納時、取得時に使用する「キー」
# 実際の値「バリュー」
# キーバリューペアで管理されている
# ※バリューでキーを取り出すことは出来ない
#   文字列かタプルはキーに使用できるが、リストと辞書はキーに出来ない


my_dict = dict()
# my_dict = {}
print(my_dict)  # {}


my_dict = {"name"    : "Nomura Takahiro",
		   "Birthday": "1994/1/15",
		   "height"  : "164cm",
		   "weight"  : "65kg" }
print(my_dict)

my_dict["name"] = "Kikuchi Saori"
print(my_dict)
print(my_dict["name"])


tmp = {}
print(tmp)

#辞書に追加
tmp["Kyoto"] = "Bazu"
print(tmp)

#辞書に追加
tmp["Ayase"] = "Jista"
print(tmp)
print(tmp["Kyoto"])

print("Kyoto" in tmp)

my_tuple = ("Saitama")
print(my_tuple)

#タプルをキーに辞書にバリューを追加
tmp[my_tuple] = "Nomura"
print(tmp)

#辞書から削除はdelでキー指定
del my_dict["weight"]
print(my_dict)





