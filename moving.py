import pygame 

pygame.init()
length = (800, 600)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
flappy = pygame.image.load("images/flappy.png")
background = pygame.image.load("images/ceu.jpeg")
clock = pygame.time.Clock()
posXredBall = 400
posYredBall = 400
movingBallHX = 0
movingBallWY = 0
pygame.display.set_icon(flappy) #icon of the screen
screen = pygame.display.set_mode(length) #moving the screen to the middle
pygame.display.set_caption("Flappy Bird do VIctor") #title of the screen
running = True
while running:
    for event in pygame.event.get(): #func get captures all the events that happen on keyboard, moouse, etc
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #maps the key to the event type
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            movingBallHX = -5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            movingBallHX = +5
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            movingBallHX = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            movingBallHX = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            movingBallWY = -5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            movingBallWY = +5
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
            movingBallWY = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            movingBallWY = 0
            
    screen.fill(white)
    if posXredBall < 0:
        posXredBall = 0
    elif posXredBall > 800:
        posXredBall = 800
    else:
        posXredBall += movingBallHX
    
    if posYredBall < 0:
        posYredBall = 0
    elif posYredBall > 600:
        posYredBall = 600
    else:
        posYredBall += movingBallWY
    screen.blit(background, (0,0))
    screen.blit(flappy, (posXredBall, posYredBall))
    #pygame.draw.circle(screen, red, (posXredBall, posYredBall), 30) #draws a circle and others shapes

    pygame.display.update()
    clock.tick(60)
pygame.quit()   