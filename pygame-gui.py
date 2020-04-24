import pygame as pg

pg.init()

SIZE_X = 900
SIZE_Y = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (24, 120, 26)

size = [SIZE_X, SIZE_Y]
screen = pg.display.set_mode(size)
pg.display.set_caption("[Davinci Code The Game (Board Game) Reinforcement Learning Project] by Jaesung-Jun")
    
class Blocks():
    def draw_blocks(self, x, y, block):
        image = pg.image.load("imgs/{}{}.png".format(block['num'], block['color'])).convert_alpha()
        screen.blit(image, (x, y))

def main():

   
    draw = Blocks()

    clock = pg.time.Clock()
    done = False

    while not done:
        clock.tick(10)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done=True
        screen.fill(BACKGROUND)

        block = [{'color':'w', 'num':10}, {'color':'w', 'num':9}, {'color':'w', 'num':8}, {'color':'w', 'num':7}]
        for i in range(len(block)):
            draw.draw_blocks(SIZE_X/(i+1),SIZE_Y-200, block[i])
            
        pg.display.update()

if __name__ == "__main__":
    main()