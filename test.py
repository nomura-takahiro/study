#!/usr/bin/python3

import string
import time
import datetime

print("=========================================================================")
print("文字列操作")

#普通の出力
test_str = "\nHello World"
print(test_str)

#文字列は「'」でも「"」でも両方可
print('strings')
print("strings")

#ファイルに書き出し
file_p = open("log.txt","a")
test_str = time.time()
test_date = datetime.datetime.now()
print(test_str,"\n",test_date,file=file_p)

#複数行
test_str = """
test_1
test_2
"""
print(test_str)

#文字列連結( += も可)
test_str = "Fight "
test_str = test_str + "dayo !"
test_str = test_str + "\n"
print(test_str)

#複数回実行
test_str = "気合だ " * 3
test_str += "\n"
print(test_str)

#文字列へ変換
test_int = 100
print(test_int)
print(str(test_int))
#上記str変数を使っていたためstr関数が使えなかった

#文字列置換
test_str = "ぺがあっぽよ"
test_str += "\n"
print(test_str.replace("ぽ","ぱ"))

#文字列分割
print(test_str.split("っ"))

#文字列桁揃え
test_str = "1234"
print(test_str.rjust(10,"0"))
print(test_str.rjust(20,"?"))

#文字列検索(先頭)
test_str = "Nomura Takahiro"
print(test_str.startswith("Nomura"))		#True
print(test_str.startswith("Takahiro"))  #False

#文字列検索(文字列内)
print("N" in test_str)  #True
print("D" in test_str)  #False

#文字列の大文字小文字変換
print(test_str.upper())
print(test_str.lower())

#先頭・末尾の削除
test_str = test_str.lstrip("Nomura")
print(test_str)
test_str = "Nomura Takahiro"
test_str = test_str.rstrip("Takahiro")
print(test_str)

print("=========================================================================")
print("数値\n")

#数値変換
test_str = "100"
print(int(test_str) + 10)

#浮動小数
test_str = "100.5"
print(float(test_str) + 10)

#複素数
test_complex = 100 + 5j
print(test_complex)
print(test_complex.real) #実数
print(test_complex.imag) #虚数


print("=========================================================================")
print("配列\n")

print("タプル")
print("任意の数の要素を持てる配列")
print("作成後に要素の追加削除は出来ない")

def get_today():
 
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)
 
    return value
 
 
test_tuple = get_today()
 
print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])

print("")

print("リスト")
print("任意の数の要素を持てる配列")
print("作成後に要素の追加削除が可能")
test_list_1 = ['python', '-', 'izm', '.', 'com']
print(test_list_1)
 
print('--------------------------------')
 
for i in test_list_1:
    print(i)

print("")

#要素の追加
test_list_1 = []
print(test_list_1)
 
print('--------------------------------')
 
test_list_1.append('python')
test_list_1.append('-')
test_list_1.append('izm')
test_list_1.append('.')
test_list_1.append('com')
 
print(test_list_1)

print("")

t_list_1 = ['python', 'izm', 'com']
print(test_list_1)
 
print('--------------------------------')
 
test_list_1.insert(1, '-')
test_list_1.insert(3, '.')
 
print(test_list_1)
 
test_list_1.insert(0, 'http://www.')
 
print(test_list_1)

print("")

print("ディクショナリ")
print("任意の数の要素を持てる配列")
print("kye と valueを一要素とする")
print("作成後の追加削除は可能")
print("1つのディクショナリの中で同じkyeは持てない")

print("")

print("セット")
print("任意の数の要素を持てる配列")
print("作成後の追加削除は可能")
print("1つのセットの中で重複した要素は持てない")

print("")






