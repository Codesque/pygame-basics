import pygame 
import random   


COLOR = (255,80,0) 
SURFACE_COLOR = (255,255,255) 
WIDTH = 900 
HEIGHT = 600

class Sprite(pygame.sprite.Sprite): 

    def __init__(self, color , width , height) -> None:
        super().__init__() 
        self.image = pygame.Surface([width , height]) 
        self.rect = self.image.get_rect() 
        self.image.fill(SURFACE_COLOR) 
        self.image.set_colorkey(COLOR) 

        pygame.draw.rect(self.image , color , pygame.Rect(0,0,width , height )) 


    def moveLeft(self , pixels): 
        self.rect.x -= pixels 

    def moveRight(self , pixels): 
        self.rect.x += pixels 

    def moveForward(self , speed): 
        self.rect.y -= speed * (speed/10) 

    def moveBackward(self , speed): 
        self.rect.y += speed * (speed/10) 

    
if __name__ == "__main__" :  

    pygame.init() 
    assert pygame.get_init() , "Error"  
    wsize = (WIDTH , HEIGHT) 
    window = pygame.display.set_mode(wsize) 
    pygame.display.set_caption("Control Sprites example") 
    Icon = pygame.image.load("pyGameAdvanced/images/disco.ico") 
    pygame.display.set_icon(Icon) 
    GREEN = (0,255,0)


    all_sprite_list = pygame.sprite.Group()  

    playerW , playerH = 50 , 75
    player = Sprite(GREEN , playerW , playerH) 
    player.rect.x = (WIDTH - playerW)//2 
    player.rect.y = (HEIGHT - playerH)//2 


    all_sprite_list.add(player) 

    running = True  
    clock = pygame.time.Clock() 
    while running : 

        for e in pygame.event.get(): 

            if e.type == pygame.QUIT: 
                pygame.quit() 
                running = False 
                raise SystemExit
            

        keys = pygame.key.get_pressed() 

        if keys[pygame.K_UP] or keys[pygame.K_w]:  
            player.moveForward(10)  

        if keys[pygame.K_DOWN] or keys[pygame.K_s]: 
            player.moveBackward(10) 

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: 
            player.moveLeft(10) 

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
            player.moveRight(10) 




            

        
        all_sprite_list.update() 
        window.fill(SURFACE_COLOR) 
        all_sprite_list.draw(window) 
        pygame.display.update()
        clock.tick(60)  




     
