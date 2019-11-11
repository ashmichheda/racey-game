import pygame
import time
import random

# pygame is an instance. .init func loads all the modules associated with pygame
pygame.init()


display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
car_width = 75

gameDisplay = pygame.display.set_mode((display_width, display_height)) # 800 --> width, 600 --> height
pygame.display.set_caption("A bit Racey Game")


# We define a clock, which basically times things for us,
# In this case, its frames/second
clock = pygame.time.Clock()


carImage = pygame.image.load("race-car.png")
carImage = pygame.transform.scale(carImage, (70, 90))


def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
	gameDisplay.blit(carImage, (x, y)) # blit() -- draws image to the screen.



def crash():
	messageDisplay('You Crashed')


def messageDisplay(text):
	font = pygame.font.Font('freesansbold.ttf', 115)
	gameDisplay.blit(font.render(text, True, (0, 0, 0)), (0, 0))
	pygame.display.update()
	time.sleep(2)

	game_loop()


def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	x_change = 0


	# object directions and properties
	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100


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

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change
		gameDisplay.fill(white)


		# things(thingx, thingy, thingw, thingh, color):
		things(thing_startx, thing_starty, thing_width,  thing_height, black)
		thing_starty += thing_speed



		car(x, y)

		# check for boundary crash
		if x > (display_width - car_width) or x < 0: # < 0 happens on the left and > width happens on the right of window
			crash()

		# check for object went off the screen for repeating the next object
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			# random between 0 to display_width range
			thing_startx = random.randrange(0, display_width)


		# Logic for car crash
		if y < thing_starty+thing_height:
			#print('Y Crossover!!')
			# Logic for car crash
			if x + car_width > thing_startx and x < thing_startx + thing_width:
				crash()



		pygame.display.update()
		clock.tick(60)  # 60 frames/second

game_loop()
pygame.quit()
quit()