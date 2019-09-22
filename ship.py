"""
Ship class for ship object
Contains enumerator for direction the ship is oriented from origin

"""

from enum import Enum

class Direction(Enum):
    """
    Simple enum for the direction a ship can be oriented.
    up (0), right (1), down (2), left (3)
    """
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Ship:

    """
    Ship creates a ship, initialized with a size, direction, and origin
    """
    # constructor - creates a ship of size(size), an origin and a given direction
    # assumes that edge cases are checked for (no negative indices)
    def __init__(self, size, origin, direction):
        """
        Creates a new Ship object
        :returns: returns none
        """
        self.size = size
        self.origin = origin
        self.direction = Direction(direction)

        self.List = []

    #returns indexes that the ship has occupied  
    def get_cells(self):
        """
        retrieves the locations of the ship
        :returns: returns list of tuples with the locations of the ships on the grid 
        """
        self.list=[self.origin]

        for i in range(1, self.size):
            if(self.direction == self.direction.LEFT):
                self.list.append((self.origin[0], self.origin[1]-i))
            elif(self.direction ==self.direction.RIGHT):
                self.list.append((self.origin[0], self.origin[1]+i))
            elif(self.direction ==self.direction.UP):
                self.list.append((self.origin[0]-i, self.origin[1]))
            elif(self.direction ==self.direction.DOWN):
                self.list.append((self.origin[0]+i, self.origin[1]))
        

        return self.list

