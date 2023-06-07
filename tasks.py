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
    #pygame.draw.line(screen, black, (0,300), (800, 300), 2) #draws a straight line
    #pygame.draw.line(screen, black, (0,0), (800, 600), 2) #draws a straight line
    #pygame.draw.lines(screen, black, True, [(50,50), (400, 550), (750, 50)], 2) #draws a straight line
    #pygame.draw.line(screen, black, (0,300), (800, 300), 2) 
    #pygame.draw.lines

    screen.blit(pygame.image.load('images/eu.jpg'), (7, 3))
    
    pygame.display.update()
pygame.quit()   