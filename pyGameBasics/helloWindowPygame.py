# 1. initialize all the modules inside of pygame module 
# 2. set a Window to display your game .  
# 3. Execute your game again and again and track events in every iteration

import pygame  

def getAndPrintWsize(): 
    mySize = pygame.display.get_window_size()  
    print(mySize) 

pygame.init() # initialise modules from pygame module

# check if the modules initialised successfully 
assert pygame.get_init() , "Pygame couldnt initialised successfully . Please try again later"


# Create a game screen by display.set_mode() method
wsize = (500,500) # (height , width)
pygame.display.set_mode(wsize) 

running = True 

while running : # While game is running ... 
    # getAndPrintWsize()
    for event in pygame.event.get(): # Track every event that made by player
        if event.type == pygame.QUIT: 
                running = False 
                # Close the application if player clicked to the "X" button
                # which is on top-left

