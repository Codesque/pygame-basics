from multiprocessing.connection import wait
import pygame  
import time
def createAnIcon(fpath): 
    Icon = pygame.image.load(fpath) 
    pygame.display.set_icon(Icon) 

pygame.init() 
assert pygame.get_init() , "Pygame module couldn't initialised successfully" 
surface = pygame.display.set_mode((500,500) , pygame.RESIZABLE)   
createAnIcon('pyGameBasics/images/gameIcon.jpeg')
surfaceColour = (255,0,0)
pygame.display.set_caption("This game has a caption")   
surface.fill(surfaceColour)  
time.sleep(10) # wait 10 seconds and then fill the surface with the intended colour
pygame.display.flip()
running = True  
while running: 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False  


pygame.quit() # dont forget this
