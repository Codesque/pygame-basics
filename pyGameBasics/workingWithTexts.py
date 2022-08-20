import time
import pygame  
class workingWithTexts : 
    def __init__(self ,app, wsize = (500,500) , bg_color = (255,255,255)) -> None:
         
        self.bg_color = bg_color 
        self.app = app
        # initialise moduls from pygame 
        pygame.init() 
        assert pygame.get_init() , "Modules couldnt initialised successfully from pygame"  

        # initialise fonts from pygame 
        pygame.font.init() 
        if not pygame.font.get_init(): 
            print("Fonts couldnt initialised successfully from pygame")  

        # Set caption and display screen 
        self.wsize = wsize 
        self.width , self.height = wsize  
        self.window = pygame.display.set_mode(self.wsize)  
        pygame.display.set_caption("Text Examples")  
        
        # load the Icon from images file 
        Icon = pygame.image.load("pyGameBasics/images/disco.ico")  
        pygame.display.set_icon(Icon) 

        # Run the game and adjust the workflow 
        self.running = True  

        if self.app == "printText": 
            # printText 1. Save the fonts 
            self.fonts = {} 
            self.fonts["freesanbold"] = pygame.font.SysFont('freesanbold.ttf' , 50 ) 
            self.fonts["chalkduster"] = pygame.font.SysFont('chalkduster.ttf' , 40)  

            # printText 2. Create some text by using these fonts 
            self.text1 = self.fonts["freesanbold"].render("Hello World" , True , (255,0,0)) 
            self.text2 = self.fonts["chalkduster"].render("Alright my dear Earth !" , True , (0,255,0)) 

            # printText 3. Create a rectangular object for the text surface object   
            self.textrect1 = self.text1.get_rect() 
            self.textrect2 = self.text2.get_rect() 

            # printText 4. Setting center for texts  
            self.textrect1.center = (self.width//2 , self.height//2) 
            self.textrect2.center =  ((self.width//2) , (self.height//2)+100)  

        if self.app == "cursorInput": 
            self.text = "Hello World!" 
            self.font = pygame.font.SysFont(None , 40) 
            self.img = self.font.render(self.text , True ,(0,255,0)) 

            self.rect = self.img.get_rect() 
            self.rect.topleft = (20,20)
            self.cursor = pygame.Rect(self.rect.topright , (3,self.rect.height))  


        if self.app == "inputBox": 
            self.clock = pygame.time.Clock() 
            self.base_font = pygame.font.SysFont(None , 40)  
            self.user_text = '' 

            self.input_rect = pygame.Rect(self.width//2 , self.height//2 , 140 ,32) 
            self.color_active = pygame.Color(255,0,0) 
            self.color_pasive = pygame.Color(0,0,255) 
            self.color = self.color_pasive
            self.active = False
            



    def body(self , events  , applyEvents  , beforeEvents = None): 
        
        while self.running: 
            if beforeEvents is not None : 
                beforeEvents()
            for event in pygame.event.get(): 
                events(event)  

            applyEvents() 



    def printText_beforeEvents(self): 
        if self.app == "printText":
            self.window.fill(self.bg_color) 
            self.window.blit(self.text1 , self.textrect1) 
            self.window.blit(self.text2,self.textrect2) 




    def printText_events(self , event : pygame.event): 
        if  event.type == pygame.QUIT: 
            self.running = False 
            pygame.quit() 
            raise SystemExit 

    def printText_applyEvents(self): 
        pygame.display.update()  


    def cursorInput_events(self , event : pygame.event): 

        if event.type == pygame.QUIT:  
            self.running = False
            pygame.quit() 
            raise SystemExit 

        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_BACKSPACE:  

                if len(self.text) > 0 : 

                    self.text = self.text[:-1] 
            
            else: 
                self.text += event.unicode

            
            self.img = self.font.render(self.text , True , (0,255,0))  
            self.rect.size = self.img.get_size() 
            self.cursor.topleft = self.rect.topright 


    def cursorInput_applyEvents(self): 
        
        # Add background color to the window screen
        self.window.fill((0,0,0)) 
        self.window.blit(self.img ,self.rect) 

        # cursor is made to blink after every 0.5 sec
        if time.time() % 1 > 0.5 : 
            pygame.draw.rect(self.window ,(255,255,255) , self.cursor)   

        pygame.display.update() 



    def inputBox_events(self , event: pygame.event): 
        
        if event.type == pygame.QUIT: 
            self.running = False 
            pygame.quit() 
            raise SystemExit 

        if event.type == pygame.MOUSEBUTTONDOWN : 
            if self.input_rect.collidepoint(event.pos) : 
                active = True 

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_BACKSPACE: 
                self.user_text = self.user_text[:-1] 

            else : 
                self.user_text += event.unicode 

    def inputBox_applyEvents(self): 
        self.window.fill(self.bg_color) 

        if self.active: 
            self.color = self.color_active 

        else : 
            self.color = self.color_pasive 

        pygame.draw.rect(self.window , self.color , self.input_rect) 

        # rendering the text 
        text_surface = self.base_font.render(self.user_text , True , (0,255,0)) 
        self.window.blit(text_surface , (self.input_rect.x + 5 , self.input_rect.y + 5)) 
        self.input_rect.w = max(100 , text_surface.get_width() + 10) 
        pygame.display.flip() 
        self.clock.tick(60) 




    









if __name__ == "__main__": 
    #EXAMPLE_1 : PRINTTEXT
        #game = workingWithTexts("printText")
        #game.body(game.printText_events , game.printText_applyEvents , game.printText_beforeEvents)  

    #EXAMPLE_2 :  
        #game = workingWithTexts("cursorInput") 
        #game.body(game.cursorInput_events , game.cursorInput_applyEvents , game.printText_beforeEvents)  

    #EXAMPLE_3 : 
    game = workingWithTexts("inputBox") 
    game.body(game.inputBox_events , game.inputBox_applyEvents) 

    




        
