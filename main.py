import pygame as pyg ,random as rand, sys,time
from pygame.locals import *
from objects import Bullet,Tank,Enemy

pyg.init()


win_size = [600,600] 

win = pyg.display.set_mode(win_size)
pyg.display.set_caption("tank fire ")





player = Tank(300,300,20,20,'purple')

enemy_list = []

def newEnemy():
    colors = ['red','green','yellow','blue','skyblue','pink','navy','orange','Crimson','Coral','SlateGray','Silver']
    color=rand.choices(colors)[0]
    enemy_list.append(Enemy(rand.randint(0, 600), rand.randint(0, 300), 20, 20,color))


for  i in range(3):
    newEnemy()
# game variables

fire = True
timer = pyg.time.Clock()
fps = 60
while fire:
	win.fill([0,0,0])
	timer.tick(fps)

	# event handling
	for event in pyg.event.get():
		if event.type == QUIT:
			fire = False
	key_pressed = pyg.key.get_pressed()
	if key_pressed[K_ESCAPE]:
		fire = False
	player.update(key_pressed,win)
	player.shoot()

	for enemy in enemy_list:
		enemy.update(win)
		enemy.outomove(win)
		enemy.shoot(win)

	pyg.display.update()
pyg.quit()

print("GAME OVER [+1]")