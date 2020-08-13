import math

class Minmax():

	def __init__(self, variation):
		self.variation = variation #heuristic variation

	def static_evaluate
	#node represents player here	
	def minimax(self, node, depth, maximizingPlayer):
		if depth = 0 or node.terminal()
			return self.static_evaluate(node)

		if maximizingPlayer
			bestValue = -1 * math.inf
			for child in node.simulate_moves()
				# here is a small change
				if freeTurn(child):
					isMax = True
				else:
					isMax = False
					val = self.minimax(child, depth - 1, isMax)
					bestValue = max(bestValue, val)
			return bestValue

		else
			bestValue = math.inf
			for child in node.simulate_moves()
				# here is a small change
				if freeTurn(child):
					isMax = False
				else:
					isMax = True
					val = self.minimax(child, depth - 1, isMax)
					bestValue = min(bestValue, val)
			return bestValue


				
		
