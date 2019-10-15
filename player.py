"""
Player module containing the Player class. Manages if the player has lost or not.
"""
from board import Board


class Player():
    # Player contructor called from game class
    def __init__(self, num_of_ships):
        """
        Constructs a player object
        :param: num_of_ships (int): gives us the player's shape
        :return: returns none

        :pre: The calling class knows how many ships the users want to play with
        """
        self.num_of_ships = num_of_ships
        self.lost = False
        self.total_ship_blocks = ((num_of_ships) * (num_of_ships + 1)) / 2
        self.board = Board()

    # used by game class to determine if player has lost
    def has_lost(self):
        """
        Lets game know when player has lost
        :return: returns bool - loss status
        
        :post: Game now knows whether or not the player has lost
        """
        if self.total_ship_blocks == 0:
            self.lost = True

            return True
        else:
            return False

    # calls board class to determine if ship is hit and returns information to game
    def be_attacked(self, x_pos: int, y_pos: int) -> bool:
        """
        Decrements amount of ship blocks available when player is attacked
        :param: x_pos (int): the x position of the mouse click
        :param: y_pos (int): the y position of the mouse click
        :return: bool - true if hit, false if not

        :post: Game now knows whether or not the player has been attacked
        """
        print(self.total_ship_blocks)
        if self.board.attacked(x_pos, y_pos) == True and self.total_ship_blocks > 0:
            self.total_ship_blocks -= 1
            print("You have hit the other player's ship!")
            return True
        else:
            print("Miss... Next player please")
            return False

    # calculates number of total ship blocks from number of ships choosen from user
    def get_ship_blocks(self, num_of_ships):
        """
        Calculates amount of ship blocks available to player
        :param: num_of_ships (int): how many ships the player has
        :return: int - amount of ship blocks player has

        :post: Returns how many unhit ship cells the player has
        """
        sum = 0
        for i in range(1, num_of_ships + 1):
            sum += i
        return sum
