import pygame 

class jumpingObject : 

    def __init__(self , wsize= (500,500)): 
        

        pygame.init() 
        pygame.get_init , "ERROR" 


        self.width , self.height = wsize 
        self.window = pygame.display.set_mode( wsize )   
        Icon = pygame.image.load("pyGameAdvanced/images/disco.ico") 
        pygame.display.set_icon(Icon)  

        self.thickness = 20
        self.ground = pygame.draw.rect(self.window , (255,0,0) , [self.width//2 , self.height - self.thickness , 100 , self.thickness]) 

        char_size = (20,20)
        self.char_width , self.char_height = char_size 
        
        self.char_fnet = 0
        self.char_v = 5
        self.char_neg_v = -(self.char_v)
        self.char_m = 1
        self.char_neg_m = -(self.char_m)
        self.char_x0 , self.char_y0 = self.width//2 , self.height-self.thickness-self.char_width 
        self.char_xt , self.char_yt = 0 , 0 # xt = x temporary , yt = y temporary
        self.bg_color = (0,0,0) 
        self.char_isJump = False 
        self.running = True 


    def events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
                pygame.quit() 
                raise SystemExit 

            
            if event.type == pygame.KEYDOWN: 
                
                if event.key == pygame.K_LEFT: 
                    self.char_xt -= self.char_v
                elif event.key == pygame.K_RIGHT: 
                    self.char_xt +=  self.char_v 

                elif event.key == pygame.K_UP and not self.char_isJump: 
                    self.char_isJump = True 

            if event.type == pygame.KEYUP : 
                if event.key == pygame.K_LEFT: 
                    self.char_xt = 0
                elif event.key == pygame.K_RIGHT: 
                    self.char_xt =  0 

                
    def applyJump(self): 
        if self.char_isJump: 

            self.char_fnet = (1/2) * self.char_m * (self.char_v**2) 
            self.char_y0 -= self.char_fnet 
            self.char_v = self.char_v  - 1 

            if self.char_v <  0 :  
                self.char_m = self.char_neg_m

            if self.char_v == ( self.char_neg_v - 1  ): 
                self.char_isJump = False 
                self.char_v = abs(self.char_neg_v) 
                self.char_m = abs(self.char_neg_m) 

    def applyEvents(self):  

        
        self.char_x0 += self.char_xt 
        self.char_y0 += self.char_yt  
        self.applyJump()

        self.window.fill(self.bg_color) 
        pygame.draw.rect(self.window , (255,0,0) , [self.char_x0 , self.char_y0 , self.char_width , self.char_height])  

        pygame.time.delay(10)
        pygame.display.update()




if __name__ == "__main__": 
    game = jumpingObject()  
    while game.running :  
        game.events() 
        game.applyEvents() 


