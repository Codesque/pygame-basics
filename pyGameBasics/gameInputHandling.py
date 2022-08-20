import pygame 

class HandleInputs: 

    def __init__(self , wsize , caption = "Character Moving" , bg_color = (255,255,255) ) -> pygame: 
        pygame.init() 
        assert pygame.get_init() , "Pygame modules couldnt initialised correctly  please try again later" 
        self.wsize = wsize   
        self.bg_color = bg_color
        self.wWidth , self.wHeight = self.wsize 
        self.window = pygame.display.set_mode(self.wsize) 
        pygame.display.set_caption(caption)   
        self.character = pygame.image.load("pyGameBasics/images/gameIcon.jpeg").convert_alpha() 
        self.char_size = (self.wWidth//5 , self.wHeight//5) 
        self.char_width , self.char_height = self.char_size 
        self.character = pygame.transform.smoothscale(self.character , self.char_size ) 
        self.running = True   

        # For Mouse Input Handling
        self.clicks = [False , False , False] 
        self.mouseCordinate = [] 

        # For Keyboard Input Handling 
        self.char_x_move , self.char_y_move = 0,0 
        self.char_x , self.char_y = (((self.wWidth - self.char_width) // 2) , ((self.wHeight - self.char_height)//2)) 



    def body(self , events , applyEvents): 
        
        
        while self.running : 
            self.mouseCordinate  = pygame.mouse.get_pos()
              
            for event in pygame.event.get(): 
                events(event) 
            
            applyEvents()  

    def handleMouseInputs(self , event : pygame.event):  

        if event.type == pygame.QUIT : 
            pygame.quit() 
            raise SystemExit
        
        if event.type == pygame.MOUSEBUTTONDOWN :  

            if event.button == 1 : # When the left mouse key is clicked , change the character's apperance  
                self.clicks[0] = True   # self.clicks = [left_key_pressed , wheel_pressed , right_key_pressed]
                self.character = pygame.image.load("pyGameBasics/images/cphoto0.jpg").convert_alpha() 
                self.character = pygame.transform.smoothscale(self.character , ( (self.wWidth//5) , (self.wHeight//5) ) )  
                pygame.display.update() 

            if event.button == 2 : # When wheel is pressed  make the character bigger 
                self.clicks[1] = True   # self.clicks = [left_key_pressed , wheel_pressed , right_key_pressed] 
                pygame.transform.scale(self.character , ((self.wWidth//2),(self.wHeight//2))) 
                pygame.display.update() 

            if event.button == 3 : # When the right mouse key is clicked , change the character's apperance back to normal 
                self.clicks[2] = True 
                self.character = pygame.image.load("pyGameBasics/images/gameIcon.jpeg").convert_alpha() 
                self.character = pygame.transform.smoothscale(self.character , ( (self.wWidth//5) , (self.wHeight//5) ) )  
                pygame.display.update()    

        if event.type == pygame.MOUSEBUTTONUP : 
            if event.button == 1 : 
                self.clicks[0] = False   
                pygame.display.update() 

            if event.button == 3 : 
                self.clicks[2] = False 
                pygame.display.update()


    def applyMouse(self): 
        self.window.fill(self.bg_color) 
        self.window.blit(self.character , self.mouseCordinate ) 
        pygame.display.update()  


    def handleKeyboardInputs(self , event : pygame.event): 

        if event.type == pygame.QUIT: 
            pygame.quit() 
            raise SystemExit
        
        
        if event.type == pygame.KEYDOWN :  

            # left and right is the same as mathmetical cordinate system , left = - , right = + 
            # But up and down is reverse , up = - , down = +
            if event.key == pygame.K_w or event.key == pygame.K_UP : 
                self.char_y_move = -0.3   

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT: 
                self.char_x_move = -0.3 

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN: 
                self.char_y_move = 0.3 

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT: 
                self.char_x_move = 0.3 

            elif event.key == pygame.K_LCTRL : 
                
                self.character = pygame.image.load("pyGameBasics/images/cphoto0.jpg").convert_alpha() 
                self.character = pygame.transform.smoothscale(self.character , ( (self.wWidth//5) , (self.wHeight//5) ) )  
                pygame.display.update()  

            elif event.key == pygame.K_BACKSPACE :  
                self.character = pygame.image.load("pyGameBasics/images/gameIcon.jpeg").convert_alpha()
                self.character = pygame.transform.smoothscale(self.character , ( (self.wWidth//5) , (self.wHeight//5) ) )  
                pygame.display.update()  


        if event.type == pygame.KEYUP: #it should stop to go any further when we dont press the button 

            if event.key == pygame.K_UP or event.key == pygame.K_w : 
                self.char_y_move = 0 
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                self.char_y_move = 0 
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                self.char_x_move = 0 
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                self.char_x_move = 0 

    def applyKeyboard(self): 

        self.char_x += self.char_x_move 
        self.char_y += self.char_y_move  

        self.window.fill(self.bg_color) 
        self.window.blit(self.character , (self.char_x , self.char_y))  
        pygame.display.update()





if __name__ == "__main__": 
    game = HandleInputs((500,500)) # Game window will be 500 x 500 
    #game.body(game.handleMouseInputs , game.applyMouse)   example 1 
    game.body(game.handleKeyboardInputs , game.applyKeyboard)  
    



                
                

                 








        