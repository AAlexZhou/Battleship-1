"""
Board module containing the Board class and
an enum for the states that a cell on the board can be in, CellStatus.
"""
from enum import Enum
from typing import List, Tuple
from ship import Ship, Direction


class CellStatus(Enum):
    """
    Simple enum for the state a cell on the board can be in.
    Empty (0), missed a ship (1), hit a ship (2)
    """
    EMPTY = 0
    MISS = 1
    HIT = 2


class Board:
    """
    Board encapsulates a player's view of their own board
    """

    def __init__(self):
        """
        Constructs a new Board object. Manages user setup of their board.
        :return: returns none.
        """
        self.hits = [[CellStatus.EMPTY] * 8 for _ in range(0, 8)]
        self.ships = []

    def place_ships(self, length, origin, direction):
        """
        Handles board setup for placing ships
        :return: returns none.

        :pre: length, origin, and direction are valid
        :post: Appends a ship with the specified fields to the self.ships list
        """

        self.ships.append(Ship(length, origin, direction))

    def attacked(self, x_pos: int, y_pos: int) -> bool:
        """
        Handles when the current board is attacked by another player

        :param: x_pos (int): x position of where the shot is fired (0 indexed)
        :param: y_pos (int): y position of where the shot is fired (0 indexed)
        :return: returns whether the shot hit a ship or not
        """
        if (x_pos < 0) or (x_pos > 7) or (y_pos < 0) or (y_pos > 7):
            raise ValueError('Invalid Position')
        elif self.hits[x_pos][y_pos] != CellStatus.EMPTY:
            raise ValueError('Position has already been attacked')
        for ship in self.ships:
            if (x_pos, y_pos) in ship.get_cells():
                self.hits[x_pos][y_pos] = CellStatus.HIT
                return True
        self.hits[x_pos][y_pos] = CellStatus.MISS
        return False

    def until_sunk(self, x_pos: int, y_pos: int) -> bool:
        while(until_sunk == False):
                if(self.hits[x_pos-1][y_pos]==CellStatus.HIT):
                    return False
                    until_sunk(self,x_pos-1,y_pos)
                elif(self.hits[x_pos+1][y_pos]==CellStatus.HIT):
                    return False
                    until_sunk(self,x_pos+1,y_pos)
                elif(self.hits[x_pos][y_pos-1]==CellStatus.HIT):
                    return False
                    until_sunk(self,x_pos,y_pos-1)
                elif(self.hits[x_pos][y_pos+1]==CellStatus.HIT):
                    return False
                    until_sunk(self,x_pos,y_pos+1)
                else:
                    return True


    def get_board_view(self) -> (List[List[CellStatus]], List[List[Tuple[int, int]]]):
        """
        Shows the view of the board for the current player.

        :return: tuple of two lists where the first element is the full board with
        all hits or misses and the second element is where ships are located
        """

        return (self.hits, [ship.get_cells() for ship in self.ships])

    def search(self, x_pos: int, y_pos: int) -> bool:
        """
        Handles when the current board is attacked by another player

        :param: x_pos (int): x position of where the shot is fired (0 indexed)
        :param: y_pos (int): y position of where the shot is fired (0 indexed)
        :return: returns whether the shot hit a ship or not
        """
        for ship in self.ships:
            if (x_pos, y_pos) in ship.get_cells():
                return True
        return False