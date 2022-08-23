import pygame  
import random

class BouncyBall: 

    def __init__(self , wsize = (700,700)): 
        
        pygame.init() 
        assert pygame.get_init() , "PyModules Couldnt initialised successfully"
        
        
        self.width , self.height = wsize 
        self.window =  pygame.display.set_mode(wsize) 
        Icon = pygame.image.load("pyGameAdvanced/images/disco.ico") 
        pygame.display.set_icon(Icon)  
        pygame.display.set_caption("Bouncy Ball Example")

        self.bb_2radius = min(self.width//20 , self.height//20)  
        self.bb_x , self.bb_y = (random.randint(0,self.width) - self.bb_2radius//2 , random.randint(0,self.height) - self.bb_2radius//2) 
        self.bb_delta_x = 3 * random.choice((-1,1))
        self.bb_delta_y = 3
        self.bb_pixel = 24   

        
        self.running = True   
        self.bg_color = (255,255,0)


    def events(self): 
        for e in pygame.event.get(): 

            if e.type == pygame.QUIT: 
                self.running = False
                pygame.quit()   
                raise SystemExit   


    def applyBounce(self): 

        if self.bb_x + self.bb_pixel > self.width or self.bb_x <= 0 : 
            self.bb_delta_x *= -1  
            self.bg_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        if self.bb_y + self.bb_pixel > self.height or self.bb_y <= 0 : 
            self.bb_delta_y *= -1  
            self.bg_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


    def applyEvents(self): 
        self.applyBounce()  

        self.bb_x += self.bb_delta_x 
        self.bb_y += self.bb_delta_y 

        self.window.fill(self.bg_color)
        pygame.draw.circle(self.window ,(0,255,0) , [self.bb_x , self.bb_y] , self.bb_2radius) 

        pygame.time.delay(10) 
        pygame.display.update() 


if __name__ == "__main__": 
    game = BouncyBall() 
    while game.running : 
        game.events() 
        game.applyEvents()  
