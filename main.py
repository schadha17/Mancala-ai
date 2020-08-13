#!/usr/local/bin/python3

#import minmax_algo
#import Player
#import Board

from Global import *
import time
from Player import Player
from Player import Node

from Board import Board

# -- Functions for minmax algorithm -----

max_player = None
min_player = None

# --------- MAIN ------------------------------

pygame.init()	
pygame.font.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20) #30

choice_p1 = int(input("Enter player 1: (player - 1) (computer - 2)"))
choice_p2 = int(input("Enter player 2: (player - 1) (computer - 2)"))
plr1, plr2 = None, None

if(choice_p1 == 1):
	plr1 = Player("Human_1 (R)", 1, 1) #red
else: 
	plr1 = Player("Computer_1 (R)", 1, 2) #red

if(choice_p2 == 1):
	plr2 = Player("Human_2 (B)", 0, 1) #blue
else:
	plr2 = Player("Computer_2 (B)", 0, 2) #blue

plr1.set_player(plr1, plr2)
plr2.set_player(plr1, plr2)

control = Board(plr1, plr2, font)
pygame.display.set_caption('Mancala')
crashed = False

control.display_board()
control.update_game()
next_player = plr1

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

		#node = Node(plr1.stones_track, plr2.stones_track, plr1)
		#node.print_state()
	
		#event = pygame.event.get()
		rval = [False, False]
		for event in pygame.event.get():
			#print(event)	
			if(event.type == pygame.QUIT):
				crashed = True
			elif(event.type== pygame.MOUSEBUTTONDOWN): #or event.type == pygame.MOUSEBUTTONUP):
				#player = control.decide() #Decides which player needs to move
				if(next_player.type == 1):
					next_player = next_player.move(event.pos)
				else: #Computer makes a turn using AI algorithm
					next_player = next_player.move(None)
				
				control.refresh()
				
				new_node = Node(plr1.stones_track, plr2.stones_track, next_player)
				print("After :")
				new_node.print_state()
				print("-----------------")	
				rval = new_node.terminal()
				if(rval[0] == True): #Current game state represents end 
					crashed = True
		
		if(rval[0] == False):
			textsurface = control.myfont.render(next_player.name + " make your turn", False, (0, 0, 0))
		else:
			textsurface = control.myfont.render("Player " + str(rval[1]), False, (0, 0, 0))
		
		control.screen.blit(textsurface,(10,10))
		
		pygame.display.update() #update helps you update small things at a time
		#pygame.display.flip() #update helps you update small things at a time
		clock.tick(1) #fps
		if(rval[0] == True): time.sleep(5)
		
	pygame.quit()
	quit()

play_game()
