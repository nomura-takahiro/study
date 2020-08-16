
# ファイル内に日本語などの「非アスキー」文字が含まれる可能性があるので、
# 基本的には読み込み時は文字コード指定をしておいたほうがいい

file_list = []

with open("test.txt","r",encoding="utf-8") as f:
	file_list.append(f.read())

print(file_list)

i = 0
j = len(file_list)

while i < j:
	print(file_list[i])
	i += 1


