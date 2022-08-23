import pygame 
import random 

class SaveTheCat : 
 
    def __init__(self , wsize = (700 , 700)): 
        pygame.init() 
        assert pygame.get_init() , "Error" 
        self.width , self.height = wsize 
        self.window = pygame.display.set_mode(wsize) 
        self.cat_image = pygame.image.load("pyGameAdvanced/images/pixelCat.jpeg")  
        pygame.display.set_icon(self.cat_image) 
        pygame.display.set_caption("Save the cat")  
        self.bg = pygame.image.load("pyGameAdvanced/images/background0.jpeg") 
        self.bg = pygame.transform.smoothscale(self.bg , (self.width , self.height)) 

        self.stone_image = pygame.image.load("pyGameAdvanced/images/cucumber.jpeg") 
        self.stone_image = pygame.transform.smoothscale(self.stone_image , (self.width//20 , self.height//40 ))  

        self.pixel = 64 # size of a pixel block 

        self.running = True 
        self.clock =  pygame.time.Clock() 

        ax_x = (self.width - self.pixel)//2 
        ax_y = self.height - 100
        
        self.player1 = self.Player(ax_x , ax_y , self.cat_image) 

        ax_x = random.randint(0,(self.width - self.pixel)) 
        ax_y = 0
        
        self.stone1 = self.Stone( ax_x, ax_y , self.stone_image)

    class Player : 

        def __init__(self , x , y , apperance : pygame.image , resolution = (100 , 100)): 

            self.apperance = apperance  
            self.apperance = pygame.transform.scale(self.apperance , resolution )
            self.x = x 
            self.y = y  
            self.delta_x = 0 
            self.delta_y = 0  
            self.v0 , self.v = 5 , 5
            self.m0 , self.m = 3 , 3
            self.isJump = False   
            self.isLeft = True 
            self.isRight = False 

        def show(self , screen : pygame.display.set_mode): 
            if self.isRight and not self.isLeft : 
                rightApperance = pygame.transform.flip(self.apperance , True , False)
                screen.blit( rightApperance , (self.x , self.y)  )   
            else :  
                screen.blit( self.apperance , (self.x , self.y)  ) 



    class Stone : 
        def __init__(self , x , y , apprerance :pygame.image , resolution = (40,100) ): 
            
            self.apperance = apprerance 
            self.apperance = pygame.transform.scale(self.apperance , resolution)
            self.x = x 
            self.y = y  
            self.delta_x = 0 
            self.delta_y = 3

        def show(self , screen : pygame.display.set_mode): 
            screen.blit( self.apperance , (self.x , self.y)    )  



    def events(self , player : Player): 

        self.window.blit(self.bg , (0,0))
        
        for event in pygame.event.get(): 

            if event.type == pygame.QUIT: 
                self.running = False 
                pygame.quit() 
                raise SystemExit 

            if event.type == pygame.KEYDOWN: 

                if event.key == (pygame.K_LEFT or pygame.K_a) : 
                    player.delta_x -= 3 
                    player.isLeft = True 
                    player.isRight = False 

                
                if event.key == (pygame.K_RIGHT or pygame.K_d): 
                    player.delta_x += 3 
                    player.isLeft = False
                    player.isRight = True 
                
                
                if event.key == (pygame.K_UP or pygame.K_w) and not player.isJump:  
                    player.isJump = True    

            if event.type == pygame.KEYUP:  

                if event.key == (pygame.K_LEFT or pygame.K_a) : 
                    player.isLeft = True 
                    player.isRight = False 
                    player.delta_x = 0

                
                if event.key == (pygame.K_RIGHT or pygame.K_d): 
                    
                    player.isLeft = False 
                    player.isRight = True 
                    player.delta_x = 0    


    def applyJump(self , player : Player):  

        if player.isJump:  

            F = (1/2) * player.m * (player.v)**2 
            player.y -= F 
            player.v -= 1 
            if player.v < 0 : 
                player.m = -(player.m0) 

            if player.v == ((- player.v0) - 1): 
                player.isJump = False  
                player.m = player.m0 
                player.v = player.v0  

    def applyCrash(self , player : Player , stone : Stone):  
        if player.y < stone.y + self.pixel : # Checking Horizontal Collusion  

            if ((player.x > stone.x and player.x < (stone.x + self.pixel))) or ((player.x + self.pixel)> stone.x and (player.x + self.pixel) < (stone.x + self.pixel)) : 
                # Player is on the  right of the  stone and player is on the left of the (stone + border) OR... 
                # Player and it's pixel border is on the right of the stone and (player + border) is on the left of the (stone + border) 
                stone.y = self.height + 1000  # ????? 


    def applyBorders(self , player : Player):  

        if player.x >= self.width - self.pixel : 
            player.x = self.width - self.pixel 

        if player.x <= 0 : 
            player.x = 0  

    def applyBorders(self , stone : Stone) : 

        if stone.y > self.height and stone.y < self.height + 200 : 
            stone.y = 0 - self.pixel  
            stone.delta_y += random.randint(0 , 1)
            stone.x = random.randint(0 , (self.width - self.pixel)) 


    def applyEvents(self): 
        
        
        self.applyBorders(self.player1) 
        self.applyBorders(self.stone1) 
        self.applyJump(self.player1)
        
        self.player1.x += self.player1.delta_x 
        self.player1.y += self.player1.delta_y  

        self.stone1.y += self.stone1.delta_y
        
        self.player1.show(self.window)  
        self.stone1.show(self.window)   

        
        self.applyCrash(self.player1 , self.stone1)  

        pygame.time.delay(10)
        pygame.display.update()
        



if __name__ == "__main__": 

    game = SaveTheCat()  
    while game.running : 
        game.events(game.player1) 
        game.applyEvents() 



            



