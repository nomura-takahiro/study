
################
###  書式化  ###
################

# format()メソッドで、文字列に後で指定した文字列を挿入できる

name = "野村尭弘"
print("こんにちは{}".format(name))

#複数指定も可能
age = 26
print("{}は{}歳".format(name,age))


your_name = input("君の名は? >> ")
your_age  = input("何歳? >> ")
print("こんにちは{}。 {}歳なんだね。".format(your_name,your_age))


