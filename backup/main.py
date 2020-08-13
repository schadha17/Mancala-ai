#!/usr/local/bin/python3

import pygame
#import minmax_algo
from Player import Player

pygame.init()

class Game():
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.dimensions = (500, 500)
		self.player_bit = 1 #for tracking player turns
		#Window
		self.screen = pygame.display.set_mode((self.dimensions[0], self.dimensions[1]))
		self.myfont = pygame.font.SysFont(None, 20) #30
	
	def display_board(self):

		self.screen.fill(white)
		
		# -------- DRAWING LINES --------
		#Horizontal lines	
		pygame.draw.line(self.screen, black, (100, 250), (400, 250))
		pygame.draw.line(self.screen, black, (50, 200), (450, 200))
		pygame.draw.line(self.screen, black, (50, 300), (450, 300))
		#bottom horizontal
		pygame.draw.line(self.screen, black, (200, 350), (300, 350))
		pygame.draw.line(self.screen, black, (200, 400), (300, 400))
		pygame.draw.line(self.screen, black, (200, 450), (300, 450))
		#top horizontal
		pygame.draw.line(self.screen, black, (200, 150), (300, 150))
		pygame.draw.line(self.screen, black, (200, 100), (300, 100))
		pygame.draw.line(self.screen, black, (200, 50), (300, 50))

		#Vertical lines
		pygame.draw.line(self.screen, black, (250, 100), (250, 400))
		pygame.draw.line(self.screen, black, (200, 50), (200, 450))
		pygame.draw.line(self.screen, black, (300, 50), (300, 450))
		#Left vertical
		pygame.draw.line(self.screen, black, (150, 200), (150, 300))
		pygame.draw.line(self.screen, black, (100, 200), (100, 300))
		pygame.draw.line(self.screen, black, (50, 200), (50, 300))
		#Right vertical
		pygame.draw.line(self.screen, black, (300, 200), (300, 300))
		pygame.draw.line(self.screen, black, (350, 200), (350, 300))
		pygame.draw.line(self.screen, black, (400, 200), (400, 300))
		pygame.draw.line(self.screen, black, (450, 200), (450, 300))

		#size = (50, 200, 50, 100)
		#pygame.draw.ellipse(self.screen, red, size, width=1)
		#size = (400, 200, 50, 100)
		#pygame.draw.ellipse(self.screen, red, size, width=1)		

		for i in range(2):
			pygame.draw.ellipse(self.screen, red, self.p1.mancala[i], width=1)
			pygame.draw.ellipse(self.screen, blue, self.p2.mancala[i], width=1)

		#size = (200, 50, 100, 50)
		#pygame.draw.ellipse(self.screen, blue, size, width=1)
		#size = (200, 400, 100, 50)
		#pygame.draw.ellipse(self.screen, blue, size, width=1)

		for i in range(10):
			pygame.draw.circle(self.screen, red, self.p1.cups[i], 25, width=1)
			pygame.draw.circle(self.screen, blue, self.p2.cups[i], 25, width=1)
			
	def update_game(self):
		for i in (self.p1.stones_track.keys()):
		
			#text = str(i) + "," + str(self.p1.stones_track[i])	
			text = str(self.p1.stones_track[i])	
			text_r = self.myfont.render(text, False, red)
			
			#text = str(i) + "," + str(self.p2.stones_track[i])	
			text = str(self.p2.stones_track[i])	
			text_b = self.myfont.render(text, False, blue)
			
			if(i == 6 or i == 12):
				idx = int((i / 6) - 1)
				loc = self.p1.mancala[idx]
				self.screen.blit(text_r, (loc[0] + 25, loc[1] + 25))
				loc = self.p2.mancala[idx]
				self.screen.blit(text_b, (loc[0] + 25, loc[1] + 25))
			else:
				if(i > 5): offset = 2
				else: offset = 1

				self.screen.blit(text_r, self.p1.cups[i-offset])
				self.screen.blit(text_b, self.p2.cups[i-offset])
		'''		
		for i in range(2):
			text_r = self.myfont.render(str(self.p1.mancala_map[i]), False, red)
			loc = self.p1.mancala[i]
			self.screen.blit(text_r, (loc[0] + 25, loc[1] + 25))

			text_b = self.myfont.render(str(self.p2.mancala_map[i]), False, blue)
			loc = self.p2.mancala[i]
			self.screen.blit(text_b, (loc[0] + 25, loc[1] + 25))
		'''
	def refresh(self):
		self.display_board()
		self.update_game()
	
	def decide(self):
		if(self.player_bit == 1):
			self.player_bit = 0
			return self.p1
		else:
			self.player_bit = 1
			return self.p2
				
pygame.font.init()
#Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
bg = (238, 217, 182)

pygame.display.set_caption('Mancala')
clock = pygame.time.Clock()
crashed = False

p1 = Player("Player1", 1) #red
p2 = Player("Player2", 0) #blue

control = Game(p1, p2)
control.display_board()
control.update_game()

next_player = p1
# --------- MAIN ------------------------------

def play_game():
	global crashed
	global next_player
	control.update_game()

	while not crashed:
		
		#event = pygame.event.get()
		#for event in pygame.event.get():
		#	#if(event.type == pygame.QUIT):
		#		crashed = True
		#	print("z") 
		
		#pygame.display.update() #update helps you update small things at a time
		
		#event = pygame.event.get()

		for event in pygame.event.get():
			#print(event)	
			if(event.type == pygame.QUIT):
				crashed = True
			elif(event.type== pygame.MOUSEBUTTONDOWN): #or event.type == pygame.MOUSEBUTTONUP):
				#player = control.decide() #Decides which player needs to move
				next_player = next_player.move(event.pos)
				control.refresh()
		'''
		if(control.player_bit == 1):
			player_name = p1.name
		else:
			player_name = p2.name
		'''	
		textsurface = control.myfont.render(next_player.name + " make your turn", False, (0, 0, 0))
		control.screen.blit(textsurface,(10,10))
		
		pygame.display.update() #update helps you update small things at a time
		clock.tick(1) #fps
		
	pygame.quit()
	quit()

play_game()
