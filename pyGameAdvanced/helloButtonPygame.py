from turtle import width
import pygame 

if __name__ == "__main__": 

    pygame.init() 
    assert pygame.get_init() , "Pymodules couldnt initialised successfully please try again later"  
    pygame.font.init() 
    resolution = (500 , 500) 
    screen = pygame.display.set_mode(resolution)   
    color = {}  
    font = {}
    color["whi"] = (255,255,255) 
    color["yel"] = (255,255,0) 
    color["red"] = (255,0,0)  
    color["gre"] = (0,100,0)  
    color["bla"] = (0,0,0) 
    font["cor"] = pygame.font.SysFont("Corbel" , 15 , True) 

    w = screen.get_width()  
    h = screen.get_height()  

    text = font["cor"].render("Hello", False , color["gre"])  

    running = True  
    while running: 

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
                pygame.quit() 
                raise SystemExit  
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                
                # If you type to "Hello I am a button" button , it triggers the game to quit
                if w//2 < mouse[0] < (w//2 + 140)  and h//2 < mouse[1] < (h//2 + 40):  
                    pygame.quit() 
                    raise SystemExit  

        screen.fill(color["yel"])  

        if w//2 < mouse[0] < (w//2 + 140)  and h//2 < mouse[1] < (h//2 + 40): 

            pygame.draw.rect(screen , color["bla"] ,[w/2 , h/2 , 140 , 40]) 
            pygame.draw.rect(screen , color["whi"] , [(w/2) + 5 , (h/2) + 5  , 130 , 30] , 1)  
            text =  font["cor"].render("quit" , False , color["whi"])

        else : 
            pygame.draw.rect(screen , color["whi"] , [w/2 , h/2 , 140 , 40 ]) 
            pygame.draw.rect(screen , color["gre"] , [(w/2) + 5 , (h/2) + 5  , 130 , 30] , 1)   
            text = font["cor"].render("Hello", False , color["gre"])

        screen.blit(text ,(w/2 + 60 , h/2 - 10 + 20)) 
        pygame.display.update()


            



        


    
    

    

