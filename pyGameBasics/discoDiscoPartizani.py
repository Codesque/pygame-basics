import pygame  
import random 

pygame.init() 
window = pygame.display.set_mode((500,500))  
pygame.display.set_caption("Disco Disco Partizani") 
Icon = pygame.image.load("pyGameBasics/images/disco.ico")   
pygame.display.set_icon(Icon)      
running = True  
r , g , b = 0 , 0 , 0
# random.randint(0,255) 
color = (r,g,b) 
while running : 

    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT : 
            running = False 
    
    
    window.fill(color)  
    pygame.display.flip() 
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))  
    pygame.display.flip() 
    image = pygame.image.load("pyGameBasics/images/disco.ico")
    window.blit(image , (random.randint(0,500),random.randint(0,500)))  
    # pygame.Surface.set_colorkey (image, [255,255,255]) 
    # Convert the [255,255,255] coloured pixels into transparent 

    # pygame.draw.rect(sample_surface, color, pygame.Rect(30, 30, 60, 60))
    # Draws a rectangle 
    pygame.display.flip()
