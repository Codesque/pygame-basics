import pygame 
class movingAnObject: 
    def __init__(self , wsize = (500,500)): 
        pygame.init() 
        assert pygame.get_init() , "ERROR" 
        Icon = pygame.image.load("pyGameAdvanced/images/disco.ico" ) 
        pygame.display.set_icon(Icon) 

        self.width , self.height = wsize 
        self.window = pygame.display.set_mode(wsize)  

        pygame.display.set_caption("Moving An Object Example") 
        
        
        self.move_x , self.move_y = 0,0
        # Crutial part : 
        self.current_x = self.width//2 
        self.current_y = self.height//2  
        

        self.velocity = 0.3 

        charSize = (15,15) 
        self.c_width , self.c_height = charSize
        self.running = True  

    
    def events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT : 
                self.running = False 
                pygame.quit() 
                raise SystemExit  


            if event.type == pygame.KEYDOWN : 
                

                if event.key == pygame.K_LEFT and self.current_x > 0 : 
                    self.move_x -= self.velocity  
                    

                elif event.key == pygame.K_RIGHT and self.current_x < self.width - self.c_width: 
                    self.move_x += self.velocity  
                    

                elif event.key == pygame.K_UP and self.current_y > 0 : 
                    self.move_y -= self.velocity  
                    

                elif event.key == pygame.K_DOWN and self.current_y < self.height - self.c_height: 
                    self.move_y += self.velocity   

                
                       

            if event.type == pygame.KEYUP:  

                if event.key == pygame.K_LEFT and self.current_x > 0 : 
                    self.move_x = 0

                elif event.key == pygame.K_RIGHT and self.current_x < self.width - self.c_width: 
                    self.move_x = 0

                elif event.key == pygame.K_UP and self.current_y > 0 : 
                    self.move_y = 0

                elif event.key == pygame.K_DOWN and self.current_y < self.height - self.c_height: 
                    self.move_y = 0
                 


    def applyEvents(self): 
        self.window.fill((0,0,0)) 
        self.current_x += self.move_x
        self.current_y += self.move_y 
        if self.current_x < 0 : 
            self.current_x = self.width - self.c_width 
        if self.current_y < 0 : 
            self.current_y = self.height - self.c_height 
        if self.current_x > self.width - self.c_width : 
            self.current_x = 0 
        if self.current_y > self.height - self.c_height : 
            self.current_y = 0
        
        rect = pygame.draw.rect(self.window , (255,0,0) , [self.current_x , self.current_y , self.c_width , self.c_height]) 
        pygame.display.update()  




if __name__ == "__main__": 
    game = movingAnObject() 
    while game.running : 
        game.events()  
        game.applyEvents() 

    