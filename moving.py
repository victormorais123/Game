import pygame 

pygame.init()
length = (800, 600)
white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
positionBall = 0
velocity = 1
right = True
screen = pygame.display.set_mode(length) #moving the screen to the middle
running = True
while running:
    for event in pygame.event.get(): #func get captures all the events that happen on keyboard, moouse, etc
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #maps the key to the event type
            running = False
            
    screen.fill(white)
    pygame.draw.circle(screen,black, (positionBall, 300), 30) #draws a circle and others shapes

    if positionBall >= 800:
        right = False
        velocity = velocity + 1
    elif positionBall <= 0:
        right = True
        velocity = velocity + 1

    if right:
        positionBall = velocity + 1
    else:
        positionBall = velocity - 1

    

    pygame.display.update()
    clock.tick(60)
pygame.quit()   