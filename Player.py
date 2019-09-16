##Player
from board import Board

class Player():
    #Player contructor called from game class
    def __init__(self, name, num_of_ships):
        self.name = name
        self.num_of_ships = num_of_ships
        self.lost = False
        self.total_ship_blocks = self.get_ship_blocks(num_of_ships)
        self.board = Board()

    #used by game class to determine if player has lost
    def has_lost(self):
            if self.total_ship_blocks == 0:
                self.lost = True
                print(self.name + "has lost")
                return True
            else:
                return False

    #calls board class to determine if ship is hit and returns information to game
    def be_attacked(self, x_pos: int, y_pos: int) -> bool:
        if board.attacked(self, x_pos, y_pos) == True and self.total_ship_blocks > 0:
            self.total_ship_blocks-=1
            print("You have hit the other player's ship!")
            return True
        else:
            print("Miss... Next player please")
            return False

    #calculates number of total ship blocks from number of ships choosen from user
    def get_ship_blocks(self, num_of_ships):
        sum = 0
        for i in range(1, num_of_ships+1):
            sum+=i
        return sum
