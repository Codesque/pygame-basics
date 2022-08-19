from turtle import bgcolor
import pygame 

class drawWithPygame:  
    def __init__(self , gameName : str , window_width : int , window_height : int , bg_color = (255,255,255)): 
        self.gameName = gameName  
        self.w_width = window_width 
        self.w_height = window_height 
        self.bg_color = bg_color
        self.running = True  
        self.eventType = None  
        self.window = None  
        self.rects = {} 
        self.circles = {}  
        self.polygons = {}


    def run(self , head = None , body = None ): 
        pygame.init()
        assert pygame.get_init() , "INITIALIZATIONError : Couldn't initialise modules from pygame successfully please try again"
        if head is not None :
            head()
        while self.running: 
            for event in pygame.event.get(): 
                self.eventType = event
                if event.type == pygame.QUIT: 
                    self.running = False  
            if body is not None: 
                body()  

    def miscellaneous(self , caption = "I have no caption :( How is it suppose to be a game" , iconPath = None):  
        
        if iconPath is not None :
            Icon = pygame.image.load(iconPath)  #pyGameBasics/images/disco.ico
            pygame.display.set_icon(Icon) 

        pygame.display.set_caption(caption) 
        self.window = pygame.display.set_mode((self.w_width , self.w_height) , pygame.RESIZABLE)  
        pygame.display.flip()  

    def drawingRectangle(self ,x,y,width , height ,color1 = (255,0,0) , border_length = 2): 
         
        
        self.rects[(x,y)] = (width , height)
        self.window.fill(self.bg_color)  
        pygame.draw.rect(self.window , color1 , [ x - (width // 2),y - (height//2) , width , height] , 2  ) 
        # Draws the surface object to the screen.
        pygame.display.update() 

    def drawingCircle(self , x , y , radius , color1 = (0,255,0) , border_length = 2): 
        pygame.display.update()
        self.window.fill(self.bg_color) 
        self.circles[(x,y)] = pygame.draw.circle(self.window , color1 , [x , y] , radius , border_length) 
        pygame.display.update() 

    def drawingPolygon(self , points : list , color1 = (0,0,255) , border_length = 10):  
        self.window.fill(self.bg_color) 
        for index , point in enumerate(points) : 
            if isinstance(point , tuple): 
                points[index] = list(point)  

        print(points)

        self.polygons[str(points)]= pygame.draw.polygon(self.window , color1 , points , border_length ) 
        pygame.display.update()  

    def drawingLine(self , start : tuple , end : tuple ,  color1 = (0,0,0) , border_length = 5): 
        self.window.fill(self.bg_color)  
        pygame.draw.line(self.window , color1 , list(start) ,list(end) ,border_length ) 
        pygame.display.update()  


    def drawingJapanFlag(self): 
        self.bg_color = (0,0,0) 
        self.window.fill(self.bg_color) 
        pygame.draw.rect(self.window,(255,255,255),[(self.w_width//2)-200 , (self.w_height//2)-200 ,400 , 400  ]) 
        pygame.display.update() 
        pygame.draw.circle(self.window ,(255,0,0) ,[ (self.w_width//2 ), (self.w_height//2)],150) 
        pygame.display.update()




if __name__ == "__main__": 
    #polyPoints = [[300, 300], [100, 400],[100, 300]] to draw a polygon , these are the cordinates that you can use
    game = drawWithPygame("Snake" , 500 , 500)  
    game.run(game.miscellaneous(iconPath="pyGameBasics/images/disco.ico") , 
    game.drawingJapanFlag() 
    )   

    """
    Put Those to body() part to see their application : 
    game.drawingRectangle((game.w_width//2) , (game.w_height//2) , 100 , 100 ) 
    game.drawingCircle((game.w_width//2) , (game.w_height//2) , 100) 
    game.drawingPolygon(polyPoints) 
    game.drawingLine(((game.w_width // 2 ) - 100, (game.w_height//2) - 100)  ,((game.w_width // 2 ) + 100, (game.w_height//2) + 100)) 
    
    
    """



     


    

    



        
    
    
             
        




