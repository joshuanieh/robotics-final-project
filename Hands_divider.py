class Hands_divider:
	#cards is in the form ['S13', 'H5', 'C3', 'D9', ...]
	#S deotes Spade, H denotes Heart, D denote Diamond, C denotes Club
	def __init__(self, cards):
		if len(cards) != 13:
			raise Exception("There should be 13 cards.")
		self.suit_spade = [False for i in range(13)]
		self.suit_heart = [False for i in range(13)]
		self.suit_diamond = [False for i in range(13)]
		self.suit_club = [False for i in range(13)]
		self.hands = []
		self.suit_correspondence = {'S': self.suit_spade, 'H': self.suit_heart, 'D': self.suit_diamond, 'C': self.suit_club}
		self.valid_checker(cards)
		
	def valid_checker(self, cards):
		for card in cards:
			try:
				if int(card[1:]) <= 13 or int(card[1:]) >= 1:				
					value = int(card[1:]) - 1 
				else:
					raise Exception(f'invalid value on card "{card}"')
			except ValueError:
				raise Exception(f'invalid value on card "{card}"')

			try:
				suit = self.suit_correspondence[card[0]]
			except KeyError:
				raise Exception(f'invalid suit on card "{card}"')

			if suit[value]:
				raise Exception(f'duplicated card "{card}"')
			suit[value] = True

	def last_hand_checker(self):
		if len(self.hands) == 10:
			for key, suit in self.suit_correspondence.items():
				for i, card in enumerate(suit):
					if card:
						self.hands += [f'{key}{i+1}']
						suit[i] = False
			return True
		return False

	def empty_suit_updator(self):
		for suit in self.suit_correspondence.values():
			empty = True
			for card in suit:
				if card:
					empty = False
					break
			if empty:
				suit = []

	def straight_flush_handler(self):
		hands = []
		def handle(key, hands):
			count = 0
			for i, card in enumerate(self.suit_correspondence[key]):
				if card == True:
					count += 1
					if count == 5:
						print(f'Straight Flush from {key}{i-3}')
						for j in range(5):
							hands += [f'{key}{i-3+j}']
							self.suit_correspondence[key][i-j] = False
				else:
					count = 0

		for key in self.suit_correspondence:
			handle(key, hands)

		#handle two straight flushes
		if len(hands) == 5:
			self.hands = hands
		elif len(hands) == 10:
			if self.card_comparator(hands[4], hands[9]) == 0:
				self.hands = hands
			else:
				self.hands = hands[5:] + hands[:5]

	def four_of_a_Kind_handler(self):
		pass

	def full_house_handler(self):
		pass

	def flush_handler(self):
		pass

	def straight_handler(self):
		pass

	def three_of_a_kind_handler(self):
		pass

	def pairs_handler(self):
		pass

	def high_card_handler(self):
		pass

	def card_comparator(self, card1, card2):
		if int(card1[1:]) > int(card2[1:]):
			return 0
		elif int(card1[1:]) < int(card2[1:]):
			return 1
		else:
			return 0 if card1[0] > card2[0] else 1

	def divide(self):
		self.straight_flush_handler()
		if self.last_hand_checker():
			self.hands.reverse()
			return self.hands
		self.empty_suit_updator()
		# self.four_of_a_Kind_handler()
		# self.full_house_handler()
		# self.flush_handler()
		# self.straight_handler()
		# self.three_of_a_kind_handler()
		'''
		These two can be combined
		self.two_pairs_handler()
		self.one_pair_handler()
		'''
		# self.pairs_handler()
		# self.high_card_handler()

	def display_cards(self):
		for key, suit in self.suit_correspondence.items():
			for i, card in enumerate(suit):
				if card == True:
					print(f'{key}{i+1}', end=' ')
		print()

if __name__ == '__main__':
	# cards_divider = Hands_divider(['S13', 'H5', 'C3', 'D9', 'S2', 'H10', 'C8', 'D7', 'S1', 'S3', 'D5', 'H12', 'H11'])
	cards_divider = Hands_divider(['H13', 'H5', 'C3', 'H9', 'S2', 'H10', 'C8', 'S5', 'S1', 'S3', 'S4', 'H12', 'H11'])
	cards_divider.display_cards()
	print(cards_divider.divide())
	cards_divider.display_cards()
