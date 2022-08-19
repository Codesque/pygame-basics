import sys
import pygame
class pyPaintDemo : 

    def __init__(self , caption : str  ,size = (500,500) ): 
        self.caption = caption  
        self.width , self.height = size 
        self.window = None 
        self.circle_positions = [] 
        self.circle_radius = 50 
        self.color = (0,0,255) 
        self.bg_color = (255,255,255) 
        self.running = True  


    def prepareDisplayScreen(self): 
        pygame.init() 
        assert pygame.get_init() , "Pygame modules couldnt initialised successfully please try again later" 
        self.window = pygame.display.set_mode((self.width , self.height)) 
        pygame.display.set_caption(self.caption , "pyPaint")  
        self.window.fill(self.bg_color)


    def body(self): 
        while self.running : 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.running = False 
                    pygame.quit() 
                
                elif event.type == pygame.MOUSEBUTTONDOWN:  
                    position = event.pos 
                    self.circle_positions.append(position) 



            for position in self.circle_positions: 
                try:
                    pygame.draw.circle(self.window , self.color ,position , self.circle_radius) 
                except: 
                    print("Hello")


            pygame.display.update() 

if __name__ == "__main__":  
    import pygame
    game = pyPaintDemo("pyPaintDemo") 
    game.prepareDisplayScreen() 
    game.body()

                    
        
