import pygame

pygame.init()
width = 1000
hight = 600
x = width * 0.95
y = hight * 0.5
screen = pygame.display.set_mode((width, hight))  # flags=pygame.NOFRAME
pygame.display.set_caption("Imaginary game by Sergo Kotzima")
prev = pygame.image.load("images/previcon.png")
pygame.display.set_icon(prev)

char = pygame.image.load("images/charimage.png")
char = pygame.transform.scale(char, (100, 100))
def add_char_at_location(x, y):
 screen.blit(char, (x, y))

running = True
while running:

    screen.fill((114, 157, 224))
    add_char_at_location(30, 30)
    # screen.blit(char, (40, 100))
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:
        #         screen.fill((70, 44, 133))
        #     if event.key == pygame.K_2:
        #         screen.fill((114, 157, 224))



# kgkg
