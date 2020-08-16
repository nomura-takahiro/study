
# War

from random import shuffle

# クラス

# Card
class Card:
	suits = ["spades", "hearts", "diamonds", "clubs"]

	values = [None, None,
			  "2", "3", "4", "5", "6", "7", "8", "9", "10",
			  "Jack", "Queen", "King", "Ace"]

	def __init__(self, v, s):
		""" スート(マーク)も整数値 """
		self.value = v
		self.suit = s

	# 以下特殊メソッド

	# 独自クラスで比較演算をするメソッド
	# __lt__：未満
	def __lt__(self, c2):
		if self.value < c2.value:
			return True

		if self.value == c2.value:
			if self.suit < c2.suit:
				return True
			else:
				return False

		return False

	# __gt__：より大きい
	def __gt__(self, c2):
		if self.value > c2.value:
			return True

		if self.value == c2.value:
			if self.suit > c2.suit:
				return True
			else:
				return False
		
		return False

	# object呼び出し時の返答
	def __repr__(self):
		v = self.values[self.value] + " of " \
			+ self.suits[self.suit]

		return v


# Deck
class Deck:
	def __init__(self):
		# カードリスト
		self.cards = []

		# カードの生成
		for i in range(2, 15):
			for j in range(4):
				self.cards.append(Card(i, j))

		# カードのシャッフル
		shuffle(self.cards)

	def rm_card(self):
		if len(self.cards) == 0:
			return
		return self.cards.pop()


# Player
class Player:
	def __init__(self, name):
		# 勝利数
		self.wins = 0
		# 所持しているカード
		self.card = None
		# Player名
		self.name = name


# Game
class Game:
	def __init__(self):
		name1 = input("Input your name (1) >> ")
		name2 = input("Input your name (2) >> ")
		self.deck = Deck()
		self.p1 = Player(name1)
		self.p2 = Player(name2)

	def wins(self, winner):
		w = "	This raund win {} !!"
		w = w.format(winner)
		print(w)

	def draw(self, p1n, p1c, p2n, p2c):
		d = "\n	{} is {}, {} is {} drawed"
		d = d.format(p1n, p1c, p2n, p2c)
		print(d)

	def play_game(self):
		cards = self.deck.cards
		print("Start War !")
		while len(cards) >= 2:
			m = "\nInput any Key. (q is end game) >> "
			response = input(m)
			if response == 'q':
				break

			p1c = self.deck.rm_card()
			p2c = self.deck.rm_card()
			p1n = self.p1.name
			p2n = self.p2.name

			self.draw(p1n, p1c, p2n, p2c)
			if p1c < p2c:
				self.p1.wins += 1
				self.wins(self.p1.name)
			else:
				self.p2.wins += 1
				self.wins(self.p2.name)

			win = self.winner(self.p1, self.p2)
			print("	Game end : {} winner !".format(win))

	def winner(self, p1, p2):
		if p1.wins > p2.wins:
			return p1.name

		if p1.wins < p2.wins:
			return p2.name

		return "draw !"



# 実処理
"""
card1 = Card(10,2)
card2 = Card(11,3)
print(card1 < card2)
print(card1 > card2)
print(card1)
print(card2)
deck = Deck()
for card in deck.cards:
	print(card)
"""

game = Game()
game.play_game()




