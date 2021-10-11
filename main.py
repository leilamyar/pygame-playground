import pygame, sys
from pygame import display
pygame.init()

BLACK = (0, 0, 0)
FPS = 60
SURF_WIDTH = 800
SURF_HEIGHT = 600
screen = pygame.display.set_mode((SURF_WIDTH, SURF_HEIGHT))
pygame.display.set_caption('My 1st game')

def moveCar(img, x, y):
    screen.blit(img, (x, y))

def main():
    # Init car
    carImg =  pygame.transform.scale(pygame.image.load("little_car.png"), (120, 70))
    # car = carImg.get_rect()
    xCar = (SURF_WIDTH * 0.45)
    yCar = (SURF_HEIGHT * 0.8)
    xChange = 0
    yChange = 0
    # carSpeed = 0
    
    # Init game
    playing = True
    clock = pygame.time.Clock()

    # Start game
    while playing:
        for event in pygame.event.get():
          # To end while loop (end game)
          if event.type == pygame.QUIT:
              playing = False
              pygame.quit()
              sys.exit()
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                  print("Left!")
                  xChange = -5
              elif event.key == pygame.K_RIGHT:
                  print("Right!")
                  xChange = 5
              elif event.key == pygame.K_DOWN:
                  print("Down!")
                  yChange = 5
              elif event.key == pygame.K_UP:
                  print("Up!")
                  yChange = -5
          if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                yChange = 0
                xChange = 0
              
        #Move the car
        screen.fill(BLACK)
        xCar += xChange
        yCar += yChange
        screen.blit(carImg, (xCar, yCar))
        pygame.display.update()

        clock.tick(FPS)
    pygame.quit()

main()