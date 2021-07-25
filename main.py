from board import Board
from mine import Mine
import pygame

def draw_board(screen, game, w, h):
    green = (0,180,120)
    blue = (0,0,255)

    #width of the borders in pixels
    BRDR_WTH = (w / game.WIDTH) / 20
    y_brdr = pygame.Rect(BRDR_WTH, 0, BRDR_WTH, BRDR_WTH)
    x_brdr = pygame.Rect(0, BRDR_WTH, BRDR_WTH, BRDR_WTH)

    rec_wth = (w / game.WIDTH) - BRDR_WTH
    rec_hgt = (h / game.HEIGHT) - BRDR_WTH

    #draw each space on the board
    for i in range(0, game.WIDTH):
        pos = pygame.Rect(BRDR_WTH, BRDR_WTH + ((rec_hgt + BRDR_WTH) * i), rec_wth, rec_hgt)
    
        for j in range(0, game.HEIGHT):
            color = green if game.grid[i][j].revealed else blue
            pygame.draw.rect(screen, color, pos)
            pos.move_ip(pos.width + BRDR_WTH, 0)

def main():
    pygame.init()
    running = True

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.mouse.set_visible(True)
    game = Board(0,0)

    screen.fill((255,255,255))

    while running:
        draw_board(screen, game, SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            # #has the mouse been pressed?
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     screen.fill((255,255,255))
            #     pygame.draw.circle(screen, (0,0,255), (250,250), 75)
            #     pygame.display.flip()
        

    pygame.quit()

main()