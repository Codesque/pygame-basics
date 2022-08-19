import pygame  
import pyPaintDemo
class GameEvents: 

    """
    An event is an action that is performed by the user in order to get the desired result. 
    For instance, if a user clicks a button then it is known as a click event. 
    Now, all the events that are performed by the user are inserted into a queue known as an event queue. 
    Since it is a queue, it follows the First In First Out rule i.e. element inserted first will come out first. 
    In this case, when an event is created it is added to the back of the queue and when the event is processed 
    then it comes out from the front. Every element in this queue is associated with an attribute which is nothing but an integer 
    that represents what type of event it is.  Let us learn a few important attributes of the common event types.

    """ 

    """
    Owing to the fact that you have understood what an event in pygame is now let us dive deep into this topic. 
    It is essential to know that the processing of an event must be done within the main function. 
    This is because if in case if it is done, then there is a chance of having an input lag which can result in a poor user experience.
    The processing is done using pygame.event.get(). 
    This is a function that will return the list of events that can be processed one after another.

    """
    def __init__(self ,  wsize = (500,500) , bg_color = (0,0,0)): 
        pygame.init()  
        self.size = wsize
        assert pygame.get_init() , "Modules couldnt initialised correctly , please try again later"  
        self.window = pygame.display.set_mode(wsize)  
        pygame.display.set_caption("pyGameBasics/images/disco.ico")  
        self.window.fill(bg_color) 
        pygame.display.flip()  
        self.running = True
        

    def keyboardEvent(self): 
        while self.running: 

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.running = False 
                    pygame.quit() 
                
                elif event.type == pygame.KEYDOWN: # KEYDOWN refers to pushing a key  
                    # K_ = from keyboard >>>> K_a : from Keyboard , a is pushed 
                    if event.key == pygame.K_w:  
                        print("Character is jumping") 
                    elif event.key == pygame.K_s: 
                        print("Character is going down") 
                    elif event.key == pygame.K_a: 
                        print("Character is going left")  
                    elif event.key == pygame.K_d: 
                        print("Character is going right")   

            
            pygame.display.flip() 

    def mouseEvent(self): 
        while self.running : 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT : 
                    raise SystemExit 
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    # MouseDown and MouseUp has the same attributes which you can use it on your games : 
                    #   1. button:  It is an integer that represents the button that has been pressed.  The left button of the mouse is 
                    #represented by 1,for mouse-wheel the integer is 2, and integer 3 is when the right button of the mouse is pressed.  
                    #   2. pos: It is the absolute position of the mouse (x, y) when the user presses the mouse button  
                    if event.button == 1 : 
                        print("You have been clicking the Left Mouse Key") 
                    elif event.button == 3 : 
                        print("You have been clicking the Right Mouse Key") 
                    elif event.button == 2 : 
                        print("You have been clicking to your Mouse Wheel")   

                elif event.type == pygame.MOUSEMOTION: 
                    # Differently MOUSEMOTION has 3 attributes : 
                    #   1. buttons :  It is a tuple that represents whether the mouse buttons (left, mouse-wheel, right) are pressed or not.
                    #   2. pos     :  It is the absolute position (x, y) of the cursor in pixels. 
                    #   3. rel     :  It represents the relative position to the previous position (rel_x, rel_y) in pixels. 
                    isLeft , isWheel , isRight = event.buttons  
                    
                    print(event.pos)
                    
                    if isLeft :  
                        print("You only clicked to the Left mouse Key ") 
                    elif isRight : 
                        print("You only clicked to the right mouse key")  

                    
                      
                    if event.rel[0] > 0 :  
                        print("Mouse is moving right") 
                    elif event.rel[0] < 0 : 
                        print("Mouse is moving left ")  
                    if event.rel[1] < 0 : 
                        print("Mouse is moving up") 
                    elif event.rel[1] > 0 : 
                        print("Mouse is moving down") 
    


                        
                    


                     




            pygame.display.update()


                









if __name__ == "__main__": 
        # I am not gonna do event control in the main function because my aim is to learn concepts. 
        head = GameEvents()    
        head.mouseEvent() 
         
        


         
