import pygame
pygame.init()
swidth, sheight = 400, 300

display_surface = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("adding image and background")
background_image=pygame.transform.scale(
    pygame.image.load('background.png').convert(),(swidth,sheight))


penguin_image=pygame.transform.scale(pygame.image.load('hello penguin.png').convert_alpha(),(200,200))
penguin_rect=penguin_image.get_rect(center=(swidth//2,sheight//2-30))

text=pygame.font.Font(None, 36).render('hello world', True, pygame.Color('black'))
text_rect=text.get_rect(center=(swidth//2,sheight+110))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image,penguin_rect)
        display_surface.blit(text,text_rect)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()

if __name__=="__main__":
    game_loop()