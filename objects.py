import pygame as pyg ,random
from pygame.locals import *


# classes
win_size = [600,600] 
# xabdadda classkeeda waaye
class Bullet:
	def __init__(self,x,y,width,height,color,RIGHT,LEFT,UP,DOWN):
		if DOWN:
			y+=20+5
		elif RIGHT or LEFT:
			y+=15
			if RIGHT:
				x+10
			else:
				x -=5
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.speed = 5
		self.off = False
		self.RIGHT = RIGHT
		self.LEFT = LEFT
		self.UP = UP
		self.DOWN = DOWN
	def update(self,win):
		self.bullet = pyg.draw.rect(win,self.color,[self.x , self.y , self.width , self.height])

		# qeybtaan waxay xaddidesa mesha uu ujeedo tangiga kadibna xabdda dhinacaas buu iridayaa
# ----------------------------------
		if self.UP:
			self.y-=self.speed
		elif self.DOWN:
			self.y+=self.speed
		elif self.RIGHT:
			self.x+=self.speed
		elif self.LEFT:
			self.x -= self.speed

	def off_screen(self):
		if self.y == 150:
			self.y = 150
	def collision(self):
		return self.bullet

# waa taangiga  aad ciyaari karto
class Tank:
	def __init__(self,x,y,width,height,color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.speed = 2
		self.bullets = []
		self.shoot_time = 0
		self.UP = True
		self.DOWN = False
		self.LEFT = False
		self.RIGHT = False

	def update(self,key_pressed,win):
		self.win = win
		UP = [self.x+5,self.y-10,self.width/2,self.height/2]
		DOWN = [self.x+5,self.y-10+20+10,self.width/2,self.height/2]
		RIGHT = [self.x+5+10+5,self.y-10+10+5,self.width/2,self.height/2]
		LEFT = [self.x+5+10+5-30,self.y-10+10+5,self.width/2,self.height/2]
		
		self.key_pressed = key_pressed

		self.tank = pyg.draw.rect(win,self.color,[self.x,self.y,self.width,self.height])
		
		if self.UP:
			pyg.draw.rect(win,'red',UP)
		elif self.DOWN:
			pyg.draw.rect(win,'red',DOWN)
		elif self.RIGHT:
			pyg.draw.rect(win,'red',RIGHT)
		elif self.LEFT:
			pyg.draw.rect(win,'red',LEFT)
		# -------------------------------------------------	
		# falaraha laga dheelo midii la taabtay baa lahubinaya kadibna falcelin suubinaa
		if self.key_pressed[K_RIGHT] and self.x <=win_size[0]-30-3:
			self.RIGHT = True
			self.LEFT = False
			self.UP = False
			self.DOWN = False
			self.x +=self.speed
		elif self.key_pressed[K_LEFT] and self.x >=13:
			self.LEFT = True
			self.RIGHT = False
			self.UP = False
			self.DOWN = False

			self.x -=self.speed
		elif self.key_pressed[K_DOWN] and self.y <=win_size[1]-30-3:
			self.DOWN = True
			self.UP = False
			self.RIGHT = False
			self.LEFT = False
			self.y +=self.speed
		elif self.key_pressed[K_UP] and self.y >=13:
			self.UP = True
			self.DOWN = False
			self.RIGHT = False
			self.LEFT = False

			self.y -=self.speed

	def shoot(self):
		self.shoot_time +=1
		if self.key_pressed[K_SPACE] and self.shoot_time >=25:
			bullet = Bullet(self.x+5,self.y-10,self.width/2,self.height/2,'red',self.RIGHT,self.LEFT,self.UP,self.DOWN)
			self.bullets.append(bullet)
			self.shoot_time = 0

		for e_bullet in self.bullets:
			e_bullet.update(self.win)
			e_bullet.off_screen()
class Enemy:
	def __init__(self,x,y,width,height,color):
		self.color = color
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.shooting = False
		self.speed = 1
		self.steps = 0
		self.count = 0
		self.bullets = []
		self.shoot_time = 0
		self.directions = {
			"right":False,
			"left":False,
			"up":False,
			"down":False
		}

		directions = ['right','up','down','left']
		self.random_direction = random.choices(directions);
		for dirc in self.directions:
			if dirc == self.random_direction[0]:
				dirc = True
			else:
				dirc = False
	def update(self,win):
		self.enm = pyg.draw.rect(win,self.color,[self.x,self.y,self.width,self.height])
	def outomove(self,win):
		UP = [self.x+5,self.y-10,self.width/2,self.height/2]
		DOWN = [self.x+5,self.y-10+20+10,self.width/2,self.height/2]
		RIGHT = [self.x+5+10+5,self.y-10+10+5,self.width/2,self.height/2]
		LEFT = [self.x+5+10+5-30,self.y-10+10+5,self.width/2,self.height/2]				

		for direction in self.directions:
#		 or  or self.y >=600-20 or self.y<=0
			if self.directions[direction]:
				if direction == 'right' and self.x <=600-20:
					self.x +=self.speed
				elif direction == 'left' and self.x >=0:
					self.x-=self.speed
				elif direction == 'up' and self.y >=0:
					self.y-=self.speed
				elif direction == 'down' and self.y <=600-20:
					self.y+=self.speed
			self.count+=1


		if self.count >=100:
			self.steps+=1
			self.count = 0
		

		if self.steps >= random.randint(3,13): #checking if off-screen
			directions = ['right','up','down','left']
			self.random_direction = random.choices(directions);
			self.steps = 0
			for direction in self.directions:
				if direction == self.random_direction[0]:
					self.directions[direction] = True
				else:
					self.directions[direction] = False
			self.shooting = True		
		if self.random_direction[0] == 'up':
			pyg.draw.rect(win,'purple',UP)
		elif self.random_direction[0] == 'down':
			pyg.draw.rect(win,'purple',DOWN)
		elif self.random_direction[0] == 'right':
			pyg.draw.rect(win,'purple',RIGHT)
		elif self.random_direction[0] == 'left':
			pyg.draw.rect(win,'purple',LEFT)

	def shoot(self,win):
		self.win = win
		self.shoot_time +=1
		if self.shoot_time >=25 and self.shooting:
			bullet = Bullet(self.x+5,self.y-10,self.width/3,self.height/2,'red',self.directions['right'],self.directions['left'],self.directions['up'],self.directions['down'])
			self.bullets.append(bullet)
			self.shoot_time = 0

		for e_bullet in self.bullets:
			e_bullet.update(self.win)
			e_bullet.off_screen()
		
		
		# -------------------------------------------------	
			
