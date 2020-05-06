import pygame as pg
import davinciCode as dvcode

SIZE_X = 800
SIZE_Y = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (24, 120, 26)

size = [SIZE_X, SIZE_Y]
screen = pg.display.set_mode(size)
pg.display.set_caption("[Davinci Code The Game (Board Game) Reinforcement Learning Project] by Jaesung-Jun")
    
class Blocks():
    def draw_blocks(self, x, y, block, angle=0):
        image = pg.image.load("imgs/{}{}.png".format(block['num'], block['color'])).convert_alpha()
        image = pg.transform.scale(image, (50, 70))
        image = pg.transform.rotate(image, angle)
        screen.blit(image, (x, y))

def main():

    draw = Blocks()

    clock = pg.time.Clock()
    done = False

    players = 4
    player_list = [n for n in range(players)]
    first = dvcode.your_Order(players-1)
    print("first order of player : {}".format(player_list[first]))
    for i in range(len(player_list)):
        player_list[i] = dvcode.Player(player_list[i])

    game = dvcode.Game()
    #Hand out 26 blocks when game start
    for i in range(len(player_list)):
        game.random_Block_To_Player(player_list[i], 3)
        print("{}번 : {}".format(i, player_list[i].blocks))

    while not done:
        jocker = None
        jocker_block = None
        clock.tick(10)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done=True
            if event.type == pg.KEYUP:
                block = game.random_Block_Pick(player_list[0])
                if block['num'] == 'j':
                    jocker_block = block
                    while(True):
                        jocker = input("Where do you want to insert your jocker({}-{})?".format(1, len(player_list[0].blocks)))
                        if  int(jocker) > len(player_list[0].blocks) and int(jocker) < 0:
                            print("Jocker should be in range {}-{}".format(1, len(player_list[0].blocks)))
                        else:
                            print(jocker_block)
        screen.fill(BACKGROUND)

        player_blocks = []

        #player_blocks list
        for i in range(len(player_list)):
            player_list[i].blocks = player_list[i].sort_Blocks()
            if jocker != None:
                player_list[i].blocks.insert(int(jocker)-1, jocker_block)
            player_blocks.append(player_list[i].blocks)
        
        #Player 1
        for i in range(len(player_blocks[0])):
            draw.draw_blocks((((SIZE_X-250)/(len(player_blocks[0])+1))*(i+1))+90,SIZE_Y-150, player_blocks[0][i], 0)
        #Player 2
        for i in range(len(player_blocks[1])):
            draw.draw_blocks((((SIZE_X-250)/(len(player_blocks[1])+1))*(i+1))+90,SIZE_Y-750, player_blocks[1][i], -180)

        #Player 3
        for i in range(len(player_blocks[2])):
            draw.draw_blocks(SIZE_X-150,(((SIZE_Y-250)/(len(player_blocks[2])+1))*(i+1))+90, player_blocks[2][i], 90)
        #Player 4
        for i in range(len(player_blocks[3])):
            draw.draw_blocks(SIZE_X-750,(((SIZE_Y-250)/(len(player_blocks[3])+1))*(i+1))+90, player_blocks[3][i], -90)

        pg.display.update()

if __name__ == "__main__":
    main()