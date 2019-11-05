import pygame
import time

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
		car(x, y)

		# check for boundary crash
		if x > (display_width - car_width) or x < 0: # < 0 happens on the left and > width happens on the right of window
			crash()
		pygame.display.update()
		clock.tick(60)  # 60 frames/second

game_loop()
pygame.quit()
quit()