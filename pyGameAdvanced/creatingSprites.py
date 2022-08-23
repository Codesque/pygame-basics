import pygame 
import random 

class createSprites :  

    SURF_COLOR = (255,255,255) 
    COLOR = (120,120,0)

    def __init__(self , wsize = (700,700)): 
        pygame.init() 
        assert pygame.get_init() , "Error"   
        self.width , self.height = wsize 
        self.window = pygame.display.set_mode(wsize) 
        Icon = pygame.image.load("pyGameAdvanced/images/disco.ico")  
        pygame.display.set_icon(Icon)  
        pygame.display.set_caption("Creating Sprites")
        self.bg_color = (255,255,0)   
        self.RED = (255,0,0)  
        self.all_sprites_list  = []
        self.running = True 
        self.clock = pygame.time.Clock()

    class Sprite(pygame.sprite.Sprite): 
        
        

        
        def __init__(self , color , height , width ) -> None:

            
            super().__init__() 

            self.image = pygame.Surface([width , height]) 
            self.rect = self.image.get_rect() 
            self.image.fill((0,0,0)) # Surface color
            self.image.fill((0,0,255)) # color 

            pygame.draw.rect(self.image , color , pygame.Rect(0,0,width , height))  

    def createObjects(self):  

        self.all_sprites_list = pygame.sprite.Group() 

        object_ = self.Sprite(self.RED , 20 , 30)  
        object_.rect.x = 200 
        object_.rect.y = 300 

        self.all_sprites_list.add(object_) 

    
    def events(self): 
        for e in pygame.event.get(): 

            if e.type == pygame.QUIT: 
                pygame.quit() 
                self.running = False 
                raise SystemExit 

    
    def applyEvents(self): 
        self.all_sprites_list.update() 
        self.window.fill((0,0,0)) 
        self.all_sprites_list.draw(self.window) 
        pygame.display.flip()  
        self.clock.tick(60)



if __name__ =="__main__": 
    game = createSprites()  
    game.createObjects()
    while game.running: 
        game.events() 
        game.applyEvents()



        


        



