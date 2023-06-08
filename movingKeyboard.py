
import pygame 

pygame.init()
length = (800, 600)
white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode(length) #moving the screen to the middle
running = True

while running:
    for event in pygame.event.get(): #func get captures all the events that happen on keyboard, moouse, etc
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #maps the key to the event type
            running = False
            
    screen.fill(white)
 
    pygame.display.update()
pygame.quit()