
###########
##  set  ##
###########

#コンテナの1つ

#集合を扱う型（ミュータブル）

#重複した要素がない
#要素に順番がない

set1 = set([1,2,3])
set2 = set([1,2,3,2,2,3,1])
print(set1)

#set2は重複した要素があるため、それらは無視(まとめられ)され、表示結果はset1と同じになる
print(set2)

