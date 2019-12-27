import pygame
import time
import random

# pygame is an instance. .init func loads all the modules associated with pygame
pygame.init()


display_width = 800
display_height = 600


pause = False

black = (0, 0, 0)
white = (255, 255, 255)

# Button colors
red = (180, 0, 0)
green = (0, 180, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)


block_color = (55, 120, 255)

car_width = 75

gameDisplay = pygame.display.set_mode((display_width, display_height)) # 800 --> width, 600 --> height
pygame.display.set_caption("A bit Racey Game")


# We define a clock, which basically times things for us,
# In this case, its frames/second
clock = pygame.time.Clock()


carImage = pygame.image.load("race-car.png")
carImage = pygame.transform.scale(carImage, (70, 90))


# how many objects dodged
def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: "+str(count), True, black) # Puts it on the screen
	gameDisplay.blit(text, (0, 0))



def things(thingx, thingy, thingw, thingh, block_color):
	pygame.draw.rect(gameDisplay, block_color, [thingx, thingy, thingw, thingh])


def car(x, y):
	gameDisplay.blit(carImage, (x, y)) # blit() -- draws image to the screen.


def quit_game():
	pygame.quit()
	quit()

def crash():



	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)

		largeText = pygame.font.Font('freesansbold.ttf', 115)
		gameDisplay.blit(largeText.render("You Crashed!", True, (0, 0, 0)), (20, 30))

		button("Play Again", 150, 450, 150, 50, green, bright_green, game_loop)
		button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

		pygame.display.update()
		clock.tick(15)


def button(msg, x, y, w, h, inactiveColor, activeColor, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	# print(click) # gets left, right and middle clicks (1, 0, 0) <--left, (0, 1, 0) <--middle, (0, 0, 1) <--right
	# print(mouse)

	if (x + w) > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, activeColor, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()

	else:
		pygame.draw.rect(gameDisplay, inactiveColor, (x, y, w, h))

	smallText = pygame.font.Font("freesansbold.ttf", 20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ((x + (w / 2)), (y + (h / 2)))
	gameDisplay.blit(textSurf, textRect)



def unpause():

	global pause
	pause = False



def paused():

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		gameDisplay.blit(largeText.render("Paused", True, (0, 0, 0)), (100, 100))

		button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
		button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)


		pygame.display.update()
		clock.tick(15)




def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		gameDisplay.blit(largeText.render("A bit Racey", True, (0, 0, 0)), (100, 100))

		button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
		button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)


		pygame.display.update()
		clock.tick(15)


def messageDisplay(text):
	font = pygame.font.Font('freesansbold.ttf', 115)
	gameDisplay.blit(font.render(text, True, (0, 0, 0)), (0, 0))
	pygame.display.update()
	time.sleep(2)

	game_loop()


def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()


def game_loop():

	global pause
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	x_change = 0


	# object directions and properties
	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	# Starting speed of the object
	thing_speed = 4
	thing_width = 100
	thing_height = 100

	dodged = 0
	thing_count = 1


	gameExit = False
	while not gameExit:

		for event in pygame.event.get():
			# event gets (for eg. where is the mouse they are pressing, pressing any key etc..
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
					x_change = 5
				if event.key == pygame.K_p:
					pause = True
					paused()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change
		gameDisplay.fill(white)


		# things(thingx, thingy, thingw, thingh, color):
		things(thing_startx, thing_starty, thing_width,  thing_height, block_color)
		thing_starty += thing_speed



		car(x, y)
		things_dodged(dodged)

		# check for boundary crash
		if x > (display_width - car_width) or x < 0: # < 0 happens on the left and > width happens on the right of window
			crash()

		# check for object went off the screen for repeating the next object
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			# random between 0 to display_width range
			thing_startx = random.randrange(0, display_width)
			dodged += 1
			thing_speed += 0.5

			# Increasing width of object after every successful dodge, for difficulty
			thing_width += (dodged * 1)


		# Logic for car crash
		if y < thing_starty+thing_height:
			#print('Y Crossover!!')
			# Logic for car crash
			if x + car_width > thing_startx and x < thing_startx + thing_width:
				crash()



		pygame.display.update()
		clock.tick(60)  # 60 frames/second

game_intro()
game_loop()
pygame.quit()
quit()
