import pygame  
import math 
class workingWithImages: 

    def __init__(self ,app , wsize = (500,500)) -> None:
        pygame.init() 
        assert pygame.get_init() , "Modules within pygame couldnt initialised successfully please try again later" 
        self.width , self.height = wsize   
        self.app = app    
        self.window = pygame.display.set_mode(wsize) 
        pygame.display.set_caption(self.app + " Example" )  
        Icon = pygame.image.load("pyGameBasics/images/disco.ico") 
        pygame.display.set_icon(Icon)
        self.running = True  
        if self.app == "scaleImage": 
            self.bg_color = (0,0,0)
            image = pygame.image.load("pyGameBasics/images/disco.ico") # this is a very small image 
            self.smallImage = image 
            self.scaledImage = pygame.transform.scale(image , (self.width//2 , self.height//2)) 
            self.position = (self.width//4 , self.height//4) 

        elif self.app == "rotateImage": 
            self.bg_color = (255,255,255) 
            image = pygame.image.load("pyGameBasics/images/cphoto0.jpg") 
            self.image = pygame.transform.scale(image , (self.width//2 , self.height//2)) 
            self.position = (self.width//4 , self.height//4)  

        elif self.app == "flipImage": 
            self.bg_color = (0,0,0) 
            image = pygame.image.load("pyGameBasics/images/gameIcon.jpeg") 
            self.image = pygame.transform.scale(image , (self.width//2 , self.height//2)) 
            self.position = (self.width//4 , self.height//4) 

        elif self.app == "dragImage": 
            self.bg_color = (255,255,0) 
            image = pygame.image.load("pyGameBasics/images/disco.ico")   
            self.image = image
            self.image = pygame.transform.scale(self.image , (self.width//4 , self.height//4)).convert() 
            self.position = (self.width//8 , self.height//8) 

            self.img_rect = self.image.get_rect() 
            self.img_rect.center = self.width//2 , self.height//2  
            self.moving = False 

        elif self.app == "rotateAndScaleImage":  

            # Modifying scaling and rotateting with these variables
            self.angle = 0 
            self.scale = 1
            
            
            # Take the Image 
            self.bg_color = (255,255,0)  
            self.image_original = pygame.image.load("pyGameBasics/images/disco.ico")
            self.image_original = pygame.transform.scale(self.image_original , (self.width//4 , self.height//4)).convert_alpha()

            # Draw a rectangle around the original image 
            self.image_original_rect = self.image_original.get_rect() 
            pygame.draw.rect(self.image_original , (255,0,0) , self.image_original_rect , 1)
            
            
            # Set the center and the position
            
            self.center = self.width//2 , self.height//2  
            self.mouse_position = pygame.mouse.get_pos()  


            # Store the original image in a new variable 
            self.img_copy = self.image_original  
            self.rect = self.img_copy.get_rect() 
            self.rect.center = self.center




            

            
              
            

    def body(self , events ,applyEvents, beforeEvent = None  ):  

        if beforeEvent is not None : 
            beforeEvent()
        while self.running:  
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.running = False 
                    pygame.quit() 
                    raise SystemExit
                
                events(event) # A method that includes other if statements for the event   


            applyEvents()    

    def scaleImage_events(self,event:pygame.event): 
        pass 

    def scaleImage_applyEvents(self): 
        
        self.window.fill(self.bg_color) 
        self.window.blit(self.smallImage , (((3 * self.width)//4) , ((3* self.height)//4) ))  
        self.window.blit(self.scaledImage , self.position)
        pygame.display.update()  


    def rotateImage_events(self , event : pygame.event): 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r: 
                self.image = pygame.transform.rotate(self.image , 90) 
            if event.key == pygame.K_t: 
                self.image = pygame.transform.rotate(self.image , -90)  


    def rotateImage_applyEvents(self): 
        self.window.fill(self.bg_color) 
        self.window.blit(self.image , self.position) 
        pygame.display.update()  

    def flipImage_events(self , event : pygame.event): 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_x: 
                self.image = pygame.transform.flip(self.image , True , False) 

            if event.key == pygame.K_y: 
                self.image = pygame.transform.flip(self.image , False , True)   

    def flipImage_applyEvents(self): 
        self.window.fill(self.bg_color) 
        self.window.blit(self.image , self.position) 
        pygame.display.update() 

    def dragImage_events(self , event: pygame.event):  

        if event.type == pygame.MOUSEBUTTONDOWN : 
            clicked = (event.button == 1)
            
            if clicked and self.img_rect.collidepoint(event.pos): 
                self.moving = True  

        if event.type == pygame.MOUSEBUTTONUP: 
            self.moving = False 


        if event.type == pygame.MOUSEMOTION and self.moving: 
            self.img_rect.move_ip(event.rel) 


    def dragImage_applyEvents(self): 
        self.window.fill(self.bg_color) 
        self.window.blit(self.image , self.img_rect) 

        pygame.draw.rect(self.window , (255,0,0) , self.img_rect , 3) 
        pygame.display.update() 


    def rotateAndScaleImage_events(self , event : pygame.event): 


        if event.type == pygame.MOUSEMOTION: 
                
            if event.buttons[0] :   
                self.mouse_position = event.pos 
                x = self.mouse_position[0] - self.center[0]
                y = self.mouse_position[1] - self.center[1]
                d = math.sqrt(x**2 + y**2) 
                self.angle = math.degrees( - math.atan2(y , x)) 
                self.scale = abs(5 * d / self.width) 
                self.img_copy = pygame.transform.rotozoom(self.image_original , self.angle , self.scale) 
                self.rect = self.img_copy.get_rect()
                self.rect.center = self.center


    def rotateAndScaleImage_applyEvents(self): 
        self.window.fill(self.bg_color) 
        self.window.blit(self.img_copy , self.rect)  

        pygame.draw.rect(self.window, pygame.color.Color("YELLOW"), self.rect, 3)
        pygame.draw.line(self.window, pygame.color.Color("RED"), self.center, self.mouse_position, 2)
        pygame.draw.circle(self.window, pygame.color.Color("RED"), self.center, 6, 1)
        pygame.draw.circle(self.window, pygame.color.Color("YELLOW"), self.mouse_position, 6, 2)


        #pygame.draw.rect(self.image , (255,0,0) , self.img_rect , 3) 
        pygame.display.update()



                 



    


if __name__ == "__main__": 
    # EXAMPLE1 : SCALE IMAGES WITH PYGAME 
        #game = workingWithImages("scaleImage") 
        #game.body(game.scaleImage_events , game.scaleImage_applyEvents)  
    # EXAMPLE2 : ROTATE IMAGE WITH PYGAME 
        # Press r and t to rotate the image 
        #game = workingWithImages("rotateImage") 
        #game.body(game.rotateImage_events , game.rotateImage_applyEvents)  
    # EXAMPLE3 : FLIPPING IMAGES WITH PYGAME  
        # Press x to flip in x axis , press y to flip in y axis 
        #game = workingWithImages("flipImage") 
        #game.body(game.flipImage_events , game.flipImage_applyEvents) 
    # EXAMPLE4 : DRAGGING IMAGES WITH PYGAME
        #game = workingWithImages("dragImage") 
        #game.body(game.dragImage_events , game.dragImage_applyEvents)  
    # EXAMPLE5 : 
    game = workingWithImages("rotateAndScaleImage") 
    game.body(game.rotateAndScaleImage_events , game.rotateAndScaleImage_applyEvents) 









    

    

            

        
