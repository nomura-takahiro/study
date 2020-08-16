
# test13

def print_data(list1, list2):
	print(list1.len)
	print(list2.len)

def print_calc(calc1, calc2):
	print(calc1.calc_perimeter())
	print(calc2.calc_perimeter())


# ③
class Shape:
	def __init__(self):
		pass

	def What_am_i(self):
		print("I am a shape.")


#①
class Rectangle(Shape):
	def __init__(self, l):
		self.len = l

	def calc_perimeter(self):
		#return (self.len[0] + self.len[1] + self.len[2] + self.len[3] )
		total = 0
		for i in self.len:
			total += i
		
		return total


class Square(Shape):
	def __init__(self, l):
		self.len = l

	def calc_perimeter(self):
		#return (self.len[0] + self.len[1] + self.len[2] + self.len[3] )
		total = 0
		for i in self.len:
			total += i
		
		return total

	# ②
	def change_size(self, index, new_size):
		self.len[index] = new_size


# ④
class Horse:
	def __init__(self, name, owner):
		self.name = name
		self.owner = owner

class Rider:
	def __init__(self, name):
		self.name = name


rect_list = [5,10,20,30]
squa_list = [1,4,8,16]

rectangle = Rectangle(rect_list)
square = Square(squa_list)

print_data(rectangle, square)
print_calc(rectangle, square)

square.change_size(0,2)

print_data(rectangle, square)
print_calc(rectangle, square)

rectangle.What_am_i()
square.What_am_i()


rider = Rider("Nomura Takahiro")
horse = Horse("Haruurara",rider)
print(horse.name)

#Riderオブジェクトのアドレスを表示する
print(horse.owner) 

print(horse.owner.name)



