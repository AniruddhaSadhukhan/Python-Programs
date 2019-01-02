""" 
Snake Game in Python using pygame
	by Aniruddha
	
	
"""

#game imports
from pygame import *
from sys import exit
from random import randrange
from time import sleep
import os


#check for initialising errors
check_errors = init()

if check_errors[1] > 0:
	print("[!] Sorry, Had {0} initialising errors, exiting ...".format(check_errors[1]))
	exit(-1)
else:
	print("[+] Pygame succesfully initialised!")

#Colors
red   = Color(255,0,0)		#gameover
blue  = Color(0,0,255)		#Writings and Pause
green = Color(0,255,0)		#snake
black = Color(0,0,0)		#score
white = Color(255,255,255) 	#background
brown = Color(165,42,42) 	#food

#Function to write text
def render_text(size, text, color, position):
    myFont = font.SysFont('monaco', size)
    font_surf = myFont.render(text, True, color)
    font_rect = font_surf.get_rect()
    font_rect.midtop = position
    playSurface.blit(font_surf, font_rect)

#Play Surface
os.environ['SDL_VIDEO_CENTERED'] = '1'
playSurface = display.set_mode((720,500))
display.set_caption("Snake Game by Aniruddha")
playSurface.fill(white)
render_text(100,'Snake Game',red,(360,50))
render_text(50,'by Aniruddha',red,(360,125))
render_text(40,"Press any key to Start",blue,(360,250))
render_text(30,"Enter Arrow Keys or a,w,s,d to control the snake",blue,(360,300))
render_text(30,"Enter Space to Pause/Resume",blue,(360, 330))
render_text(30,"Enter Escape to Quit",blue,(360,360))
display.flip()
start = False
sleep(2)
while not start:
	for events in event.get():
		if events.type == QUIT:	
			quit()	#pygame exit
			exit()	#console exit
		elif events.type == KEYDOWN:
			start = True





#FPS controller
fpsController = time.Clock()

#Important variables
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [randrange(2,71)*10,randrange(5,49)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0
level = 1

pause = False
game_running = True

try:
	with open("HighScore.txt",'r') as file:
		highscore = int(file.read())
except:
	highscore = 0
initial_highscore = highscore

#Reset Status for next match
def reset_stats():
	global game_running,pause,changeto,direction,snakePos,foodPos,foodSpawn,score,snakeBody
	snakePos = [100,50]
	snakeBody = [[100,50],[90,50],[80,50]]

	foodPos = [randrange(2,71)*10,randrange(5,49)*10]
	foodSpawn = True

	direction = 'RIGHT'
	changeto = direction

	score = 0
	level = 1
	
	pause = False
	game_running = True
	

#Quit or Restart after Completion Function
def Hold():
	global game_running
	while not game_running:
		for events in event.get():
			if events.type == QUIT:	
				quit()	#pygame exit
				exit()	#console exit
			elif events.type == KEYDOWN:
				if events.key == K_SPACE:
					reset_stats()
					game_running = True
				elif events.key == K_ESCAPE:
					event.post(event.Event(QUIT))



 
# Game Over function
def gameOver():
	game_running = False
	render_text(100,'Game Over !!!',red,(360,50))
	showScore(1)
	render_text(30,"Enter Space to Restart",blue,(360,350))
	render_text(30,"Enter Escape to Quit",blue,(360, 390))
	display.flip()
	Hold()
	
# Score function
def showScore(GO=0):
	if GO == 1:
		render_text(30,'Highest Score: {0}'.format(highscore),black,(360,210))
		render_text(30,'Score: {0}'.format(score),black,(360,180))
		render_text(30,'Level: {0}'.format(level),black,(360,150))
		if initial_highscore < highscore:
			try:
				render_text(50,'Congratulations!!! New High Score',red,(360,260))
				with open("HighScore.txt",'w') as file:
					file.write(str(highscore))
			except Exception as e:
				print(str(e))
	else:
		render_text(30,'Highest Score: {0}'.format(highscore),black,(120,10))
		render_text(30,'Score: {0}'.format(score),black,(360,10))
		render_text(30,'Level: {0}'.format(level),black,(640,10))


#Main Logic
def main():
	global game_running,pause,changeto,direction,snakePos,foodPos,foodSpawn,score,level,highscore,snakeBody
	while game_running:
		for events in event.get():
			if events.type == QUIT:	
				quit()	#pygame exit
				exit()	#console exit
			elif events.type == KEYDOWN:
				if events.key == K_RIGHT  or events.key == ord('d'):
					changeto = 'RIGHT'
				elif events.key == K_LEFT or events.key == ord('a'):
					changeto = 'LEFT'
				elif events.key == K_UP   or events.key == ord('w'):
					changeto = 'UP'
				elif events.key == K_DOWN or events.key == ord('w'):
					changeto = 'DOWN'
				elif events.key == K_ESCAPE:
					event.post(event.Event(QUIT))
				elif events.key == ord(' '):
					if pause == True:
						pause = False
					else:
						pause = True
	
		if pause == True:
			render_text(100,'Paused',blue,(360,120))
			display.flip()
			continue
		
		#Validation of direction
		if changeto == 'RIGHT'  and not direction == 'LEFT':
			direction = 'RIGHT'
		elif changeto == 'LEFT' and not direction == 'RIGHT':
			direction = 'LEFT'
		elif changeto == 'UP'   and not direction == 'DOWN':
			direction = 'UP'
		elif changeto == 'DOWN' and not direction == 'UP':
			direction = 'DOWN'
	
	
		#Changing position of snake
		if direction == 'RIGHT':
			snakePos[0] += 10
		elif direction == 'LEFT':
			snakePos[0] -= 10
		elif direction == 'UP':
			snakePos[1] -= 10
		elif direction == 'DOWN':
			snakePos[1] += 10
	
		#Snake body mechanism
		snakeBody.insert(0,list(snakePos))
		if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
			foodSpawn = False
			score += 1
			level = 1 + score//5
			if highscore < score:
				highscore = score
		else:
			snakeBody.pop()
	
		#Food Spawn
		if foodSpawn == False:
			foodPos = [randrange(2,71)*10,randrange(5,49)*10]
			foodSpawn = True
	
		#Draw Snakes and Foods
		playSurface.fill(white)
		draw.line(playSurface,black,(0,40),(720,40))
		for pos in snakeBody:
			draw.rect(playSurface,green,Rect(pos[0],pos[1],10,10))
	
		draw.rect(playSurface,brown,Rect(foodPos[0],foodPos[1],10,10))
	
	
		#Condition for Game Over
		if snakePos[0] >= 720 or snakePos[0] <= 0 or snakePos[1] >= 500 or snakePos[1] <= 40:
			game_running = False
	
		for block in snakeBody[1:]:
			if snakePos[0] == block[0] and snakePos[1] == block[1]:
				game_running = False
	
		showScore()
		display.flip()

		fpsController.tick(9+level)
	
	
while True:
	if game_running:
		main()
	else:
		gameOver()
		Hold()	
