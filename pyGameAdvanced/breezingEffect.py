import pygame 
import random 

WIDTH = 1400
HEIGHT = 700  
c1,c2,c3 = 255 , 0 , 0 # red color 

if __name__ == "__main__" :

    pygame.init()  
    
    
    window = pygame.display.set_mode((WIDTH , HEIGHT)) 
    Icon = pygame.image.load("pyGameAdvanced/images/disco.ico") 
    pygame.display.set_icon(Icon) 
    
    running = True  
    day = True 
    night = False  
    once = True 

    while running : 

        for e in pygame.event.get(): 

            if e.type == pygame.QUIT: 
                pygame.quit() 
                running = False 
                raise SystemExit  

            
            
        if day :    
            if c2 != 191 : 
                c2 += 1 

            elif c1 != 0 : 
                c1 -= 1 
                c3 += 1  
            else: 
                day = False 
                night = True  

        elif night :  
            
            if c2 != 0  and once : 
                c2 -= 1 

            elif c1 != 64 and once : 
                c1 += 1 

            else :  
                once = False 
                if  c3 != 0 :
                    c1 = max(c1 - 1 , 0) 
                    c3 = max(c3 - 3 , 0) 

                elif c2 == 0 and c3 == 0 : 
                    c1 += 1  
                    if c1 == 255 : 
                        day = True 
                        night = False  
                        once = True 

                 

        window.fill((c1,c2,c3)) 
        pygame.time.delay(10) 
        pygame.display.update() 

     

