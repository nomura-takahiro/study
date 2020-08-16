
##################################
###   コンテナの中のコンテナ   ###
##################################

#コンテナの中にコンテナを入れることも可能
#※ただしタプルなどのイミュータブルなコンテナにリストなどのミュータブルなものを格納するとイミュータブルとなるため、
#  辞書のキーとしては使えなくなる 

container = []

name = ["Nomura Takahiro","Kobayashi Tomohiro","Finato Takatugu"]
come_from = ["Kanagawa","Saitama","Nagoya"]

print(container)

container.append(name)
container.append(come_from)

print(container)
print(container[0])
print(container[1])


my_dict = dict()
my_dict = {
		"name": ("Nomura","Takahiro"),

		"hobby":[
			"パソコン",
			"アニメ",
			"将棋",
		],

		"param":{
			"height":164,
			"weight":65,
		}
}

print(my_dict)
print(my_dict["name"])
print(my_dict["hobby"])
print(my_dict["param"])


