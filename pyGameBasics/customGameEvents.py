import pygame 
class CustomEvent: 
    def __init__(self , wsize = (500,500)): 
        pygame.init() 
        assert pygame.get_init() , "Modules from pygame couldnt initialised successfully"  
        self.wsize = wsize
        
        # 1. Setting up the screen and timer 
        self.window = pygame.display.set_mode(wsize) 
        self.timer = pygame.time.Clock() 

        pygame.display.set_caption("Custom Events") 
        
        # 2. Defining colors
        self.colors = {} 
        self.colors["WHITE"] = (255,255,255) 
        self.colors["RED"] = (255,0,0) 
        self.colors["GREEN"] = (0,255,0) 
        self.colors["BLUE"] = (0,0,255)  

        # 3. Keep track of active variable 
        self.bg_active_color = self.colors["WHITE"] 
        self.window.fill(self.bg_active_color)  

        # 4. Custom user event to change color 
        self.CHANGE_COLOR = pygame.USEREVENT + 1 

        # 5. Custom user event to inflate defalte box 
        self.ON_BOX = pygame.USEREVENT + 2 

        # 6. Creating rectangle 
        self.rect = pygame.Rect((225,225,50,50)) 
        self.shouldGrow = True 

        # 7. posting a event after changing color in every 500 miliseconds 
        pygame.time.set_timer(self.CHANGE_COLOR ,500) 
        self.running = True  
        """ 
        Broadcasting the event periodically by using PyGame timers. 
        Here, we’ll be using another method to publish the event by using set_timer() function, 
        which takes two parameters, a user event name and time interval in milliseconds.

        """


    def body(self):
        while self.running: 
            for event in pygame.event.get(): 
                if event.type == self.CHANGE_COLOR: 
                    if self.bg_active_color == self.colors["GREEN"] : 
                        self.window.fill(self.colors["GREEN"])  
                        self.bg_active_color = self.colors["WHITE"] 
                    elif self.bg_active_color == self.colors["WHITE"] :  
                        self.window.fill(self.colors["WHITE"]) 
                        self.bg_active_color = self.colors["GREEN"]  

                if event.type == self.ON_BOX: 
                    if self.shouldGrow: 
                        self.rect.inflate_ip(3,3) 
                        self.shouldGrow = self.rect.width < 75 
                    else : 
                        self.rect.inflate_ip(-3,-3) 
                        self.shouldGrow = self.rect.width < 50 

                if event.type == pygame.QUIT: 
                    self.running = False  
                    pygame.quit()
                    raise SystemExit 

            # 8. Posting event when the cursor is on the top  
            if self.rect.collidepoint(pygame.mouse.get_pos()) : 
                # rect.collidepoint function basiclly returns if the cordinates of mouse comprises with the rectangle  
                pygame.event.post(pygame.event.Event(self.ON_BOX))  
                """
                We can directly post our events using pygame.event.post() method. 
                This method adds our event to the end of the events on the queue. 
                In order to execute this, 
                we need to convert our event to Pygame’s event type inorder to match the attributes of the post method and avoid errors.
                
                """
            
            pygame.draw.rect(self.window , self.colors["RED"] , self.rect) 

            pygame.display.update() 

            #9. Setting frame per second
            self.timer.tick(30)   
                # This is for a nice shot , because if we dont slow the time , animation  looks like robotic a bit
            

if __name__ == "__main__":  
    game = CustomEvent()  
    game.body() 


                    

        
         



        
