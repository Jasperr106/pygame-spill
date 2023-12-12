import pygame
import sys

pygame.init()

SCREEN_W = 550
SCREEN_H = 550
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))

clock = pygame.time.Clock()

turn_x = True

class O():
    def __init__(self, x ,y):
        self.image = pygame.image.load("t_o.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        SCREEN.blit(self.image, self.rect)

class X():
    def __init__(self, x ,y):
        self.image = pygame.image.load("t_x.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        SCREEN.blit(self.image, self.rect)

sprite = []

grid = pygame.image.load("grid_t.png")

grid_rect = grid.get_rect()
grid_rect.center = SCREEN_W/2, SCREEN_H/2

grid_points_x = []
grid_points_y = []
x_value = 45
y_value = 45
g_height, g_width = grid.get_height() - 30, grid.get_width() - 30


for i in range(3):
    y_value += (g_height/3) + 15
    grid_points_y.append((y_value))

for i in range(3):
    x_value += g_width / 3 + 15
    grid_points_x.append((x_value))
    print("ok")

def closest(list,value):  
    closest = list[min(range(len(list)), key = lambda i: abs(list[i]-value))]
    return list.index(closest), closest

pressed_squares = []


run = True
while run:
    mouse_pos = pygame.mouse.get_pos()
    SCREEN.fill("white")

    x = X(mouse_pos[0], mouse_pos[1])
    o = O(mouse_pos[0], mouse_pos[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, x_pos = closest(grid_points_x, mouse_pos[0])
            y, y_pos = closest(grid_points_y,mouse_pos[1])
            grid_buffer = (SCREEN_W - grid.get_width()) / 2

            if not mouse_pos[0] > grid.get_width() + grid_buffer and not grid_buffer > mouse_pos[0] and not mouse_pos[1] > grid_buffer + grid.get_height() and not grid_buffer > mouse_pos[1]:
                if (round(x),round(y)) not in pressed_squares:
                    if turn_x:
                        sprite.append(X(x_pos,y_pos))
                        turn_x = False
                        pressed_squares.append((x,y))
                    else:
                        sprite.append(O(x_pos,y_pos))
                        turn_x = True
                        pressed_squares.append((x,y))
    for sprites in sprite:
        sprites.update()

    SCREEN.blit(grid,grid_rect)
    pygame.display.update()
