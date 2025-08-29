import pygame
pygame.init()
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("First Game screen")
screen.fill((135, 206, 235))

# Load the image
image = pygame.image.load('forza.png')

image_rect = image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
screen.blit(image, image_rect)

done = False

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
            done = True  
  
    pygame.display.flip()  