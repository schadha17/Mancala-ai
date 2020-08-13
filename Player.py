from Global import *
import math
import time
from termcolor import colored

#Node stores current state of the game along with player whose move is next
class Node():
	def __init__(self, p1_map, p2_map, player):
		self.p1_map = p1_map
		self.p2_map = p2_map
		self.player = player

	def static_evaluate(self, max_player, heur):
		
		if(heur == 1):
			#Heuristic 1
			p1_stones = self.p1_map[6] + self.p1_map[12] 
			p2_stones = self.p2_map[6] + self.p2_map[12]

			if(max_player.color == 1):
				return p1_stones - p2_stones
			else:
				return p2_stones - p1_stones
		else:
			p1_empty_cups = 0
			p2_empty_cups = 0
			
			#Heursitic 2

			for key in self.p1_map:
				if(key == 6 or key == 12): continue
				if(self.p1_map[key] == 0): p1_empty_cups += 1
				if(self.p2_map[key] == 0): p2_empty_cups += 1
				
			if(self.player.color == 1):
				return p1_empty_cups
			else:
				return p2_empty_cups	
		
	#Determines if state is a terminal state	
	def terminal(self):
		flag1 = True
		flag2 = True

		p1_map = self.p1_map
		p2_map = self.p2_map

		for key in p1_map:
			if(key ==  6 or key == 12):
				continue
			if(p1_map[key] != 0):
				flag1 = False
			
			if(p2_map[key] != 0):
				flag2 = False
			
		winner = 1 if((p1_map[6] + p1_map[12]) > (p2_map[6] + p2_map[12])) else 2
		return [(flag1 or flag2), winner]
			
	#Next possible moves from current state
	def simulate_moves(self):
		#print("Initial state ")
		#print("p1 ", self.p1_map)
		#print("p2 ", self.p2_map)
		
		#self.print_state()

		moves = []
		cur_player_map = None
	
		if(self.player.color == 1): cur_player_map = self.p1_map
		else: cur_player_map = self.p2_map
		
		for keys in sorted(cur_player_map):
			if(keys == 6 or keys == 12): continue #Skip mancalas
			if(cur_player_map[keys] != 0):

				rval = self.player.make_move(keys, self.p1_map, self.p2_map)
				#print("Self State after move")
				#self.print_state()	
				updated_p1_map = rval[0]
				updated_p2_map = rval[1] 
				player = rval[2]

				new_node = Node(updated_p1_map, updated_p2_map, player)
				moves.append(new_node)
		#print("Moves for next state ")
		'''
		for move in moves:
			print("p1 map ", move.p1_map)
			print("p2 map ", move.p2_map)
			move.print_state()
			#print("\n ")
		'''
		#print("Moves are ", moves)
		#print("-------------------------------------------------")
		return moves 

	def print_state(self):
		#skip = [(0, 0), (0, 1), (0, 2), (0, 5), (0, 6), (0, 7), (1, 0), (1, 1), (1,2), (1,5), (1,6), (1,7), (1, 8),]	
		#skip = [0,1,2,5,6,7,8]
			
		print("\t      " + str(self.p2_map[12]))
		print("\t    "+ colored(str(self.p2_map[1]), 'green') + " | " + colored(str(self.p2_map[11]), 'green'))
		print("\t    "+ colored(str(self.p2_map[2]), 'green') + " | " + colored(str(self.p2_map[10]), 'green'))
		print(str(self.p1_map[12]) + " | " + colored(str(self.p1_map[11]), 'red') + " | " + colored(str(self.p1_map[10]), 'red')  + " | " + colored(str(self.p1_map[9]), 'red') + " | " + colored(str(self.p2_map[9]), 'green') + ' | ' + colored(str(self.p1_map[8]), 'red') + " | " + colored(str(self.p1_map[7]), 'red') + " | " + colored(str(self.p1_map[6]), 'white'))
		print(" " + " | " + colored(str(self.p1_map[1]), 'red') + " | " + colored(str(self.p1_map[2]), 'red')  + " | " + colored(str(self.p2_map[3]), 'green') + " | " + colored(str(self.p1_map[3]), 'red') + " | " + colored(str(self.p1_map[4]), 'red') + " | " + colored(str(self.p1_map[5]), 'red') + " | ")
		print("\t    " + colored(str(self.p2_map[4]), 'green') + " | " + colored(str(self.p2_map[8]), 'green'))
		print("\t    " + colored(str(self.p2_map[5]), 'green') + " | " + colored(str(self.p2_map[7]), 'green'))
		print("\t      " + str(self.p2_map[6]))
		#print("\n")
		
		#print("\t\t\t" + str(
	
class Player():
	def __init__(self,name, color, player_type):
		self.name = name
		self.color = color
		self.cups_map = {}
		self.stones_track = {} #Tracks number of stones in cups and mancalas
		self.type = player_type

		#self.cur = p1 if self.color == 1 else p2
		#self.other = p2 if self.color == 1 else p1

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

	def set_player(self,p1, p2):
		self.cur_player = p1 if self.color == 1 else p2
		self.other_player = p2 if self.color == 1 else p1

	#node represents state of the board here	
	def minimax(self, node, depth, max_player, heur):
		
		if depth == 0 or node.terminal()[0]:
			return [node.static_evaluate(max_player, heur), node]
			
		if max_player == node.player:
			bestValue = -1 * math.inf
			best_state = None

			for child in node.simulate_moves():
				val = self.minimax(child, depth - 1, max_player, heur)
				self.num_nodes += 1
				if(val[0] > bestValue):
					bestValue = val[0]
					best_state = child
			return [bestValue, best_state]

		else:
			bestValue = math.inf
			best_state = None
			for child in node.simulate_moves():
				val = self.minimax(child, depth - 1, max_player, heur)
				self.num_nodes += 1
				if(val[0] < bestValue):
					bestValue = val[0] 
					best_state = child
			return [bestValue, best_state]

	def minimax_alpha_beta(self, alpha, beta, node, depth, max_player, heur):
		
		if depth == 0 or node.terminal()[0]:
			return [node.static_evaluate(max_player, heur), node]
			
		if max_player == node.player:
			bestValue = -1 * math.inf
			best_state = None

			for child in node.simulate_moves():
				val = self.minimax_alpha_beta(alpha, beta, child, depth - 1, max_player, heur)
				self.num_nodes += 1
				if(val[0] > bestValue):
					bestValue = val[0]
					best_state = child

				alpha = max(alpha, val[0])
				if(beta <= alpha): break

			return [bestValue, best_state]

		else:
			bestValue = math.inf
			best_state = None
			for child in node.simulate_moves():
				val = self.minimax_alpha_beta(alpha, beta, child, depth - 1, max_player, heur)
				self.num_nodes += 1
				if(val[0] < bestValue):
					bestValue = val[0] 
					best_state = child
				
				beta = min(beta, val[0])
				if(beta <= alpha): break
			return [bestValue, best_state]


	def make_move(self, location, p1_map, p2_map):
		rval = []
		
		player_map = None
		other_map = None

		if(self.color == 1): 
			player_map = p1_map.copy()
			other_map = p2_map.copy()
		else: 
			player_map = p2_map.copy()
			other_map = p1_map.copy()
		
		stones = player_map[location] #starting cup
		#print("Num stones at location ", location, "are: ", stones)

		player_map[location] = 0
		location = location + 1

		while(stones != 0):
			if(location > 12): location = location - 12 #moving index into bounds

			player_map[location] = player_map[location] + 1
			stones = stones - 1
			location = location + 1
		
		location -= 1 #To find last location that was inserted on
		#print("Last location is ", location)
			
		if(location == 6 or location == 12): #last stone placed in mancala
			if(self.color == 1): return [player_map, p2_map, self.cur_player]
			else: return [p1_map, player_map, self.cur_player] 
		
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
		if(player_map[location] == 1): #last stone placed in a cup that was empty
			
			other_player_stones = 0
			player_map[location] = 0
			cur_loc_stone = 1

			if(self.color == 0): #p2
				if(location == 3):
					other_player_stones = other_map[3] + other_map[9]
					other_map[9] = 0
					other_map[3] = 0

				elif(location == 8):
					other_player_stones = other_map[3]
					other_map[3] = 0
				else:
					cur_loc_stone = 0
					player_map[location] = 1

			else: #control.p1 is current player
				if(location == 2):
					other_player_stones = other_map[3]
					other_map[3] = 0

				elif(location == 3):
					other_player_stones = other_map[8]
					other_map[8] = 0

				elif(location == 9):
					other_player_stones = other_map[3]
					other_map[3] = 0
					other_player_stones +=  other_map[9]
					other_map[9] = 0
				else:
					cur_loc_stone = 0
					player_map[location] = 1

			#Add stones to closest mancala
			if(location > 5): player_map[12] = player_map[12] + other_player_stones + cur_loc_stone
			else: player_map[6] = player_map[6] + other_player_stones + cur_loc_stone
		
		if(self.color == 1): return [player_map, other_map, self.other_player]
		else: return [other_map, player_map, self.other_player] 

	def move(self, position):
			
		if(self.type == 1): #Human Player	
			#print("--------------")
			#print("Color: ", self.color)
		
			#print("Current player ", self.cur_player.color)
			#print("Other player ", self.other_player.color)
			#cur = self.cur_player
			#other = self.other_player

			# Calculates location of the starting cup
			location = 0
			min_distance = float('inf')
			
			#Finding which cup was pressed by user
			for i in range(len(self.cups)):
				distance = (self.cups[i][0] - position[0]) ** 2 + (self.cups[i][1] - position[1]) ** 2
				if distance < min_distance:
					location = i
					min_distance = distance
			#print("cup location ", location)

			 #top match the keys for map
			if(location < 5): location += 1
			else: location += 2

			# ---- zz 

		p1_map, p2_map = None, None

		if(self.cur_player.color == 1):
			p1_map = self.cur_player.stones_track.copy()	
			p2_map = self.other_player.stones_track.copy()
		else:
			p1_map = self.other_player.stones_track.copy()
			p2_map = self.cur_player.stones_track.copy()
		
		print("Turn: ", self.name)
		print("Before: ")
		new_node = Node(p1_map, p2_map, self.cur_player)
		new_node.print_state()
	
		if(self.type == 1): #Human
			rval = self.make_move(location, p1_map, p2_map)	
			if(self.color == 1):
				self.stones_track = rval[0]
				self.other_player.stones_track = rval[1] 
			else:
				self.stones_track = rval[1]
				self.other_player.stones_track = rval[0]
				
			return rval[2]
			
		else: #Computer
			#print("INITIAL ------")
			#print("p1 map ", p1_map)
			#print("p2 map ", p2_map)

			#new_node = Node(p1_map, p2_map, self.cur_player)
			#new_node.print_state()
			
			depth = 7
			if(self.cur_player.color == 1):
				heuristic = 1
			else:
				heuristic = 2
			self.num_nodes = 0
			start_time = time.time()
			
			#rval = self.minimax(new_node, depth, self.cur_player, heuristic)
			rval = self.minimax_alpha_beta( (-1 * math.inf), math.inf, new_node, depth, self.cur_player, heuristic)
			end_time = time.time()
			print("Time taken ", end_time - start_time)
			print("Number of Nodes ", self.num_nodes)
			
			if(self.color == 1):
				self.stones_track = rval[1].p1_map
				self.other_player.stones_track = rval[1].p2_map
			else:
				self.stones_track = rval[1].p2_map
				self.other_player.stones_track = rval[1].p1_map

			#print("Next turn ", rval[1].player.name)
			#print("Next turn ", self.other_player.name)
			#print("----------")
			#return self.other_player
			return rval[1].player
			
			'''	
			#Temp
			print("Simulate Moves")
			p1_map = {1:5,2:5,3:5,4:4,5:4,6:0,7:4,8:4,9:4,10:4,11:0,12:1}
			p2_map = {1:4,2:4,3:4,4:4,5:4,6:0,7:4,8:4,9:4,10:4,11:4,12:0}
			new_node = Node(p1_map, p2_map, self.cur_player) 
			moves = new_node.simulate_moves()
			for move in moves: 
				move.print_state()
				#print("Turn ", move.player.name)
				#print("\tGoing deep............")
				#for mynode in move.simulate_moves():
				#	print("INITIAL STATE ")
				#	move.print_state()
				#	mynode.print_state()
				#	print("Turn ", mynode.player.name)
				#print("\tGoing deep ends.........")
				#print("----------")
			'''
			return self.other_player
			
		
