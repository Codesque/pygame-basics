from turtle import delay
import cv2
import pygame   
import random 
import sys


surface , caption ,gameIcon = None , None , None  
running = True 
def body(beforeRunning = None , afterRunning = None ):
    pygame.init() 
    assert pygame.get_init() , "PyGame Modules has'nt been initialised successfully please try again later "  
    running = True 
    if beforeRunning is not None :
        beforeRunning()
    while running : 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False  

        if afterRunning is not None : 
            afterRunning() 

def prepareDisplay(width , height ,gameIcon = None, method1=None, caption = "Pygame"): 
    global surface 
    size = (width , height)
    surface = pygame.display.set_mode(size) 
    caption = pygame.display.set_caption(caption)  
    if gameIcon is not None : 
        gameIcon = pygame.image.load(gameIcon) 
        pygame.display.set_icon(gameIcon) 

    if method1 is not None : 
        method1()   

def drawing_surface(window , bg_color = (0,0,0) , color1 = (255,0,0) , color2 = (255,255,255)): 
    
    window.fill(bg_color)   
    width , height = 400 , 400
    while width > 5 and height > 5 : 
            x = 250 - (width // 2) 
            y = 250 - (height // 2) 
            pygame.draw.rect(window ,color1 , pygame.Rect(x , y , width , height ) )  
            pygame.display.flip() 

            width = ( 9*width // 10 ) 
            height = ( 9*height // 10 )  

            x = 250 - (width // 2) 
            y = 250 - (height // 2) 
            pygame.draw.rect(window ,color2 , pygame.Rect(x , y , width , height ) )  
            pygame.display.flip()  

            width = ( 9*width // 10 ) 
            height = ( 9*height // 10 )   


def addingBlitting(window , bg_color = (0,0,0)):  
    
    
    window.fill(bg_color) 
    x0,y0 = 0 , 0 
    image = pygame.image.load("pyGameBasics/images/optical.jpg").convert_alpha()  
    image = pygame.transform.smoothscale(image, (50, 50))
        
    while x0 != 200 and y0 != 200 : 
        x = x0 
        y = y0 
        while x <= (450 - x0) : 
            window.blit(image , (x,y))  
            pygame.display.flip()
            x += 20 
        while y <= (450-y0) : 
            window.blit(image , (x,y)) 
            pygame.display.flip()
            y+= 20
        while x > x0 : 
            window.blit(image , (x,y))
            pygame.display.flip()  
            x -= 10 
        while y > y0 : 
            window.blit(image , (x,y)) 
            pygame.display.flip()
            y -= 20  

        x0 += 40
        y0 += 40 


def horrorGameUsing_time_wait(window , bg_color = (0,0,0) ,bg2_color = (255 , 0 , 0)): 
    window.fill(bg_color)    
    pygame.display.flip()
    image = pygame.image.load("pyGameBasics/images/scaryHolyLady.jpeg").convert_alpha() 
    image = pygame.transform.smoothscale(image ,(250,250)) 
    window.blit(image ,  (125,125) )
    pygame.time.wait(5000)
    # window.fill(bg2_color)  
      
    pygame.display.flip() 

def horrorGameUsing_time_get_ticks(window , bg_color = (0,0,0)): 
    window.fill(bg_color)  
    pygame.display.flip()   
    image = pygame.image.load("pyGameBasics/images/scaryHolyLady.jpeg").convert_alpha()
    image = pygame.transform.smoothscale(image , (400,400))
    while  running :
        
        # storing the time in ticks variable
        ticks=pygame.time.get_ticks()
        
        # printing the variable ticks
        print(ticks)
        
        # increasing the value of i by 1
        if ticks % 3 == 0 : 
            window.blit(image , (50,50)) 
            pygame.display.flip() 
        elif ticks > (1000 * 120) or not running: 
            pygame.quit() 
            sys.exit()
            break 
        else : 
            window.fill(bg_color) 
            pygame.display.flip()
        # pausing the script for 1 second
        
        pygame.time.wait(1000)  



def horrorGameUsing_time_delay(window , bg_color = (0,0,0)):  

    window.fill(bg_color)  
    pygame.display.flip()   
    image = pygame.image.load("pyGameBasics/images/scaryHolyLady.jpeg").convert_alpha()
    image = pygame.transform.smoothscale(image , (400,400))
    while  running :
        
        # storing the time in ticks variable
        ticks=pygame.time.get_ticks()
        
        # printing the variable ticks
        print(ticks)
        
        # increasing the value of i by 1
        if ticks % 3 == 0 : 
            window.blit(image , (50,50)) 
            pygame.display.flip() 
        elif ticks > (1000 * 120) or not running: 
            pygame.quit() 
            sys.exit()
            break 
        else : 
            window.fill(bg_color) 
            pygame.display.flip()
        # pausing the script for 1 second
        
        pygame.time.delay(1000) 


def usingClock(window , bg_color = (0,0,0)): 
    i=0
    
    # creating a clock object
    clock=pygame.time.Clock()
    
    # creating a loop for 5 iterations
    while i<5:
        
        # setting fps of program to max 1 per second
        clock.tick(1)
        
        # printing time used in the previous tick
        print(clock.get_time())
        
        # printing compute the clock framerate
        print(clock.get_fps())
        i=i+1

                
body(beforeRunning = prepareDisplay(500,500,"pyGameBasics/images/disco.ico"),
afterRunning = horrorGameUsing_time_get_ticks(surface))  


    

         


    
    
