
"""
Da vinci code The game (Board Game)

13 White Blocks (1-11 + Jocker)
13 Black Blocks
"""

import random
import time
import davinciCode as dvcode

#First Order return
def your_Order(howmanyplayers):
    turn = random.randint(0, howmanyplayers)
    return turn

class Player:
    def __init__(self, p_num):
        self.p_num = p_num
        self.blocks = []
    
    def show_Blocks(self):
        return self.blocks
    
    def sort_Blocks(self):
        temp = []
        for i in range(len(self.blocks)):
            if "10" in str(self.blocks[i]['num']):
                temp.append("{}{}".format( str(self.blocks[i]['num']).replace("10", "x"), 
                                        self.blocks[i]['color']))
            elif "11" in str(self.blocks[i]['num']):
                temp.append("{}{}".format(str(self.blocks[i]['num']).replace("11", "y"), 
                                        self.blocks[i]['color']))
            elif "12" in str(self.blocks[i]['num']):
                temp.append("{}{}".format(str(self.blocks[i]['num']).replace("12", "z"),
                                        self.blocks[i]['color']))
            else:
                temp.append("{}{}".format(self.blocks[i]['num'], self.blocks[i]['color']))
        temp = sorted(temp)
        for i in range(len(temp)):
            if "x" in temp[i]:
                temp[i] = temp[i].replace("x", "10")
            elif "y" in temp[i]:
                temp[i] = temp[i].replace("y", "11")
            elif "z" in temp[i]:
                temp[i] = temp[i].replace("z", "12")
            if temp[i][:-1] != "j":
                self.blocks[i] = {'color':temp[i][-1:], 'num':int(temp[i][:-1])}
            else:
                #self.blocks[i] = {'color':temp[i][-1:], 'num':temp[i][:-1]}
                continue
        return self.blocks

class Game:

    black_blocks = []
    white_blocks = []

    #Game Instance Created
    def __init__(self):

        print("Game Start!")
        time.sleep(1)
        self.black_blocks = [{'color':'b', 'num':0}, {'color':'b', 'num':1}, {'color':'b', 'num':2}, {'color':'b', 'num':3}, {'color':'b', 'num':4},
                        {'color':'b', 'num':5}, {'color':'b', 'num':6}, {'color':'b', 'num':7}, {'color':'b', 'num':8}, {'color':'b', 'num':9},
                        {'color':'b', 'num':10}, {'color':'b', 'num':11}, {'color':'b', 'num':'j'}]

        self.white_blocks = [{'color':'w', 'num':0}, {'color':'w', 'num':1}, 
                        {'color':'w', 'num':2}, {'color':'w', 'num':3}, {'color':'w', 'num':4}, {'color':'w', 'num':5}, {'color':'w', 'num':6}, 
                        {'color':'w', 'num':7}, {'color':'w', 'num':8}, {'color':'w', 'num':9}, {'color':'w', 'num':10}, {'color':'w', 'num':11}, 
                        {'color':'w', 'num':'j'}]

        self.blocks = self.black_blocks + self.white_blocks
    #Hand out 26 blocks when game start
    def random_Block_To_Player(self, player, howmany):
        for i in range(howmany):
            while(True):
                random.shuffle(self.blocks)
                if self.blocks[0]['num'] != 'j':
                    player.blocks.append(self.blocks[0])
                    del self.blocks[0]
                    break

    def random_Block_Pick(self, player):
        if len(self.blocks) != 0:
            random.shuffle(self.blocks)
            player.blocks.append(self.blocks[0])
            ret_block = self.blocks[0]
            del self.blocks[0]
            return ret_block
    def how_Many_Blocks(self):
        return len(self.blocks)

"""
if __name__ == '__main__':
    
    while(True):
        players = int(input("How many Players(2-4)?"))
        if players > 1 and players < 5:
            print("OK.")
           
            break
        else:
            print("Please select number between 2 and 4.")

    players = 4
    player_list = [n for n in range(players)]
    first = your_Order(players-1)
    print("first order of player : {}".format(player_list[first]))

    for i in range(len(player_list)):
        player_list[i] = Player(player_list[i])
    #player_list[0]: num 0, player_list[1]: num 1, player_list[2]: num 2, player_list[3]: num 3

    game = Game()
    #Hand out 26 blocks when game start
    for i in range(len(player_list)):
        game.random_Block_To_Player(player_list[i], 3)
        print("{}번 : {}".format(i, player_list[i].blocks))
    print(player_list[0].show_Blocks())
    print(player_list[0].sort_Blocks())
    game.random_Block_Pick(player_list[0])
    print(player_list[0].show_Blocks())"""