class Player():
	def __init__(self,name, color):
		self.name = name
		self.color = color
		self.cups_map = {}
		self.stones_track = {} #Tracks number of stones in cups and mancalas

		#4 Stones for each cup (k,v) such that k -> index of cup, v -> number of stones
		for i in range(1, 13):
			if(i == 6 or i == 12):
				self.stones_track[i] = 0
			else:
				self.stones_track[i] = 4
			#self.cups_map[i] = 4

		#self.mancala_map = {0:0, 1:0}
	
		if(color == 1):	
			#self.mancala = [(75, 250), (425, 250)]
			self.mancala = [(400, 200, 50, 100), (50, 200, 50, 100)]
			self.cups = [(125, 275), (175, 275), (325, 275), (375, 275), (375, 225), (325, 225), (175, 225), (125, 225)]
			#edge case (2 middle red circles)
			self.cups.insert(2, (275, 275))
			self.cups.insert(7, (225, 225))

		else:
			#self.mancala = [(250, 75), (250, 425)]
			self.mancala = [(200, 400, 100, 50), (200, 50, 100, 50) ]
			self.cups = [(275, 125), (275, 175), (275, 325), (275, 375), (225, 375), (225, 325), (225, 175), (225, 125)]
			self.cups = self.cups[::-1]
			self.cups.insert(2, (225, 275))
			self.cups.insert(7, (275, 225))
	
	def print_state(self):
		print("stones control.p1: ", control.p1.stones_track)
		print("stones p2: ", p2.stones_track)

	def move(self, position):
		
		print("--------------")
		print("Color: ", self.color)
		self.print_state()
	
		cur_player = control.p1 if self.color == 1 else p2 
		other_player = 	p2 if self.color == 1 else control.p1

		# Calculates the starting cup
		location = 0
		min_distance = float('inf')
		
		#Finding which cup was pressed by user
		for i in range(len(self.cups)):
			distance = (self.cups[i][0] - position[0]) ** 2 + (self.cups[i][1] - position[1]) ** 2
			if distance < min_distance:
				location = i
				min_distance = distance
		print("cup location ", location)

		 #top match the keys for map
		if(location < 5):
			location += 1
		else:
			location += 2

		stones = self.stones_track[location] #starting cup
		print("Num stones at location ", location, "are: ", stones)

		self.stones_track[location] = 0
		location = location + 1
		while(stones != 0):
			if(location > 12):
				location = location - 12 #moving index into bounds

			self.stones_track[location] = self.stones_track[location] + 1
			stones = stones - 1
			location = location + 1
		
		location -= 1 #To find last location that was inserted on
	
		print("Last location is ", location)
		#return p2
			
		if(location == 6 or location == 12): #last stone placed in mancala
			return cur_player
			#return control.p1 if self.color == 1 else p2 #For the current player to make a move again
		#else:
		#	return other_player
			#return p2 if self.color == 1 else control.p1 #Next player's turn
		
		''' CASE WHERE LAST STONE IS PLACED IN AN EMPTY CUP
		#RED
		1,4,5,6,7 -> null	
		2 -> 3
		3 -> 8
		9 -> 3,9

		#BLUE
		3 -> 3,9
		8 -> 3
		
		'''
		if(self.stones_track[location] == 1): #last stone placed in a cup that was empty
			
			other_player_stones = 0
			self.stones_track[location] = 0
			cur_loc_stone = 1
			#other_player = control.p1 if self.color == 0 else p2

			if(self.color == 0): #p2
				if(location == 3):
					other_player_stones = control.p1.stones_track[3] + control.p1.stones_track[9]
					control.p1.stones_track[9] = 0
					control.p1.stones_track[3] = 0

				elif(location == 8):
					other_player_stones = control.p1.stones_track[3]
					control.p1.stones_track[3] = 0
				else:
					cur_loc_stone = 0

			else: #control.p1 is current player
				if(location == 2):
					other_player_stones = p2.stones_track[3]
					p2.stones_track[3] = 0

				elif(location == 3):
					other_player_stones = p2.stones_track[8]
					p2.stones_track[8] = 0

				elif(location == 9):
					other_player_stones = p2.stones_track[3]
					p2.stones_track[3] = 0
					other_player_stones +=  p2.stones_track[9]
					p2.stones_track[9] = 0
				else:
					cur_loc_stone = 0

			#Add stones to closest mancala
			if(location > 5): self.stones_track[12] = self.stones_track[12] + other_player_stones + cur_loc_stone
			else: self.stones_track[6] = self.stones_track[6] + other_player_stones + cur_loc_stone
		
		self.print_state()
		return other_player
	
