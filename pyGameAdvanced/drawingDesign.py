from turtle import bgcolor
import pygame 

if __name__ == "__main__": 

    pygame.init() 
    assert pygame.get_init() , "ERROR" 
    
    res = (500,500) 
    w , h = res
    screen = pygame.display.set_mode(res)  
    bg_color = (255,255,255) 
    screen.fill(bg_color) 
    
    
    rfw , rfh = 20,20
    x0 , y0 = w//2 - rfw//2 , h//2 - rfh//2
    rectFrame = pygame.rect.Rect(x0 , y0 ,rfw , rfh)  

    border_len = 10 

    rw , rh = rfw - border_len , rfh - border_len  
    rx0 , ry0 = w//2 - rfw//2 + border_len//2 , h//2 - rfh//2 + border_len//2  
    rectColor = pygame.rect.Rect(rx0 , ry0 , rw , rh) 

    frameColor = (0,0,0)
    activeColor = (255,0,0)
    pygame.draw.rect(screen ,frameColor ,rectFrame ,rfw ,0) 
    pygame.draw.rect(screen , activeColor , rectColor) 



    
    
    
    running = True   
    paint = False 
    mouseControl = False  
    clock = pygame.time.Clock()
    pygame.display.update()

    while running : 
        x , y = 0 , 0
        for event in pygame.event.get(): 

            if event.type == pygame.QUIT: 
                running = False 
                pygame.quit() 
                raise SystemExit   

            if event.type == pygame.KEYDOWN :  

                if event.key == pygame.K_0 : 
                    mouseControl = not(mouseControl) 

                elif not mouseControl : 

                    if event.key == pygame.K_UP or event.key == pygame.K_w: 
                        y -= 5

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                        y += 5 

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                        x -= 5

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                        x += 5
                    
                    if event.key == pygame.K_1 : 
                        activeColor = (255,0,0) # Red  

                    if event.key == pygame.K_c: 
                        paint = True

            if event.type == pygame.KEYUP and not mouseControl :  

                    if event.key == pygame.K_c: 
                        paint = False 

                    if event.key == pygame.K_UP: 
                        y += 0  

                    if event.key == pygame.K_DOWN: 
                        y += 0 

                    if event.key == pygame.K_LEFT: 
                        x += 0 

                    if event.key == pygame.K_RIGHT: 
                        y += 0

                    

                      

        
        rx0 += x 
        x0 += x 
        ry0 +=y 
        y0 += y 

         
        #rectFrame.move_ip(x , y)
        rectColor.move_ip(x,y) 
        pygame.display.update()  

        #screen.fill(frameColor , rectFrame) 
        screen.fill(activeColor , rectColor)

        if paint:
            pygame.draw.rect(screen , activeColor , rectColor ) 
            pygame.display.update() 

        



                
                

        
        pygame.display.update()



    

        


                

    
    