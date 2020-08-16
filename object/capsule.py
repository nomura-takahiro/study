
# カプセル化

# カプセル化の2つの概念

# 1.オブジェクトによって複数の変数（状態保持）とメソッド（状態変更、状態を利用した計算など）をまとめること
class Rectangle:
	def __init__(self, w, l):
		# インスタンス変数としてwidthとlenを保持
		self.width = w
		self.len = l

	def area(self):
		# areaメソッドでインスタンス変数を使用して面積を算出する
		return self.width * self.len


# 2.データをクラス内に隠ぺいして外から見えないようにすること
class Data:
	def __init__(self):
		self.nums = [1,2,3,4,5]

	def change_data(self, index, n):
		self.nums[index] = n

data_one = Data()
# 1つの変更手段としては直接データを書き換えること
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
# もう一つの手段はメソッドを呼び出すこと
data_two.change_data(0, 200)
print(data_two.nums)





