
#################################
#####    define function    #####
#################################

def add(x):
	return x + 2

def point(x):
	x + 2
	return  # この場合やreturnがない場合はNoneを返す

def total(x, y, z):
	return x + y + z


#################################
#####         coding        #####
#################################

x = 2
result = add(x)
print(result)  # 4
print(x)       # 2のまま

result = 0
result = point(x)
print(result)  # None
print(x)       # 2のまま

a = 1
b = 2
c = 3

result = total(a,b,c)
print(result)

string = "Nomura Takahiro"

result = len(string)  # 空白も含まれる
print(result)


print(str(100))  #str型のオブジェクトを返す

print(int('1'))  #int型のオブジェクトを返す
                 #整数文字列か浮動小数点しか受け取れない

print(float(100))  #float型のオブジェクトを返す
                   #数字文字列か整数型しか受け取れない


#age = input("Input your age >> ")
#print(age)


###############################
#####   オプション引数    #####
###############################

#関数起動時、引数がなければ使用される引数(デフォルト値)
#※引数があっても使用することはできる

def option(x=2):
	return x + x

print(option())   # 4
print(option(4))  # 8




