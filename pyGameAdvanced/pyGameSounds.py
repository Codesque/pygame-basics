import pygame 
from pygame import mixer  
import random

if __name__ == "__main__": 
    WIDTH , HEIGHT = (700,700)  
    SHOW_CUTE_CAT = False  
    pygame.init()

    window = pygame.display.set_mode((WIDTH , HEIGHT)) 
    pygame.display.set_caption("VERY CUTE CATS ^_^ , HOLD ON A MINUTE FOR THE NEXT IMAGE") 
    Icon = pygame.image.load("pyGameAdvanced/images/pixelCat.jpeg") 
    pygame.display.set_icon(Icon)  

    VERY_CUTE_CAT = pygame.USEREVENT + 1 
    pygame.time.set_timer(VERY_CUTE_CAT , 60 * 1000)
    clock = pygame.time.Clock() 
    mixer.init()  
    mixer.music.load("pyGameAdvanced/sounds/giant_roar.wav")  
    mixer.music.set_volume(0.7) 

    
    running = True   

    while running : 

        for e in pygame.event.get(): 

            if e.type == pygame.QUIT : 
                pygame.quit()  
                running = False 
                raise SystemExit  

            if e.type == VERY_CUTE_CAT :  
                SHOW_CUTE_CAT = True  
                mixer.music.play() 

        
        if SHOW_CUTE_CAT : 

            window.fill((0,0,0))  
            image = pygame.image.load("pyGameAdvanced/images/scaryHolyLady.jpeg").convert() 
            image = pygame.transform.scale(image , (WIDTH//2 , HEIGHT//2)) 
            window.blit(image , (WIDTH//4 , HEIGHT//4))  
            pygame.time.delay(10) 
            pygame.display.update()

        else : 
            window.fill((120,20,120)) 
            image = pygame.image.load("pyGameAdvanced/images/cuteCat.jpeg").convert() 
            image = pygame.transform.scale(image , (WIDTH//2 , HEIGHT//2))  
            window.blit(image , (WIDTH//4 , HEIGHT//4))   
            pygame.display.update() 

        

            


             



        
        

