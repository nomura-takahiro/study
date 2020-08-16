
# test8

#①
tmp = "カミュ"
for i in range(3):
	print(tmp[i])

#②
"""
tmp = input("What?  >> ")
tmp2 = input("Who?  >> ")
print("私は昨日{}を書いて、{}に送った!".format(tmp,tmp2))
"""

#③
text = "aldous Huxley was born in 1894."
print(text.capitalize())


#④
text = "どこで？　だれが？　いつ？"
print(text)
print(text.split("　"))


#⑤
text =["The","fox","jumped","over","the","fence","."]
print(" ".join(text).replace(" .","."))


#⑥
text = "A screaming comes across the sky."
print(text.replace("s","@"))


#⑦
text = "Hemingway"
print(text.index("m"))


#⑧
print("何でもは知らないわよ。'知っている'ことだけ。")


#⑨
text = "three"
print(text + text + text)
print(text * 3)


#⑩
text = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(text)
print(text[:text.index("、")+1])

