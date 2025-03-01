"""
Contains BoardWindow class and AI_Window class.
For medium-level AI, It fires randomly until it hit a ship then fires
in orthogonally adjacent spaces to find other hits until a ship is sunk
"""

from functools import reduce
import arcade
from board import CellStatus
from player import Player
import random

# This sets the WIDTH and HEIGHT of each grid location
CELL_WIDTH = 80
CELL_HEIGHT = 80

# This sets the margin between each cell
MARGIN = 5
OFFSET = 30
first = True
special = False

class BoardWindow(arcade.View):
    """
    View for the main game phase (displaying boards and shooting shots)
    """

    def __init__(self, width: int, height: int, title: str, player: Player, on_end, is_own_board: bool):
        """
        Initialize Board Window

        :param: width (int): Width of window
        :param: height (int): Height of window
        :param: title (str): Title for Window
        :param: player (Player): Player data this board shows
        :param: on_end (Function): Function to call when a turn ends
        :param: is_own_board (Bool): Is this board owned by the player it refers to
        :return: None
        :pre: Player has been initalized with ships already placed
        """

        super().__init__()
        self.shape_list = None
        self.player = player
        self.on_end = on_end
        self.is_own_board = is_own_board
        self.width = width
        self.height = height

        arcade.set_background_color(arcade.color.BLACK)
        self.recreate_grid()

    def recreate_grid(self):
        """
        Rebuild grid based on updated player data

        :returns: None
        :post: self.shape_list is updated to reflect the changing player board underneath
        """

        self.shape_list = arcade.ShapeElementList()
        grid = self.player.board.get_board_view()[0]
        for row in range(8):
            for column in range(8):
                if grid[row][column] == CellStatus.EMPTY:
                    color = arcade.color.WHITE
                elif grid[row][column] == CellStatus.MISS:
                    color = arcade.color.GRAY
                elif grid[row][column] == CellStatus.HIT:
                    color = arcade.color.RED
                x = (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                y = (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2
                current_rect = arcade.create_rectangle_filled(x + OFFSET, y, CELL_WIDTH, CELL_HEIGHT, color)
                self.shape_list.append(current_rect)

    def on_draw(self):
        """
        Renders the class to the screen
        """

        arcade.start_render()
        self.shape_list.draw()
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        numbers.reverse()
        for i in range(8):
            arcade.draw_text(letters[i], (i * 80) + 70, self.width - 20, arcade.color.WHITE)
            arcade.draw_text(numbers[i], 15, (i * 80) + 70, arcade.color.WHITE)
        if self.is_own_board:
            for row in range(8):
                for column in range(8):
                    # Flatmap the list of ship positions, since we don't care which ship has which cell
                    if (row, column) in reduce(list.__add__, self.player.board.get_board_view()[1]):
                        x = (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                        y = (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2
                        arcade.draw_text("X", x + (OFFSET / 2), y - (OFFSET / 2), arcade.color.BLACK, 32)

    def on_mouse_press(self, x, y, _, __):
        """
        Handles user shooting at a grid cell including playing sounds

        :param: x (int): x location of the click
        :param: y (int): y location of the click
        :returns: None

        :post: Could end turn if the press was valid
        """
        global special
        if self.is_own_board:
            return

        # Change the x/y screen coordinates to grid coordinates
        column = (x - OFFSET) // (CELL_WIDTH + MARGIN)
        row = (y) // (CELL_HEIGHT + MARGIN)
        grid = self.player.board.get_board_view()[0]

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        if row < 8 and column < 8 and row >= 0 and column >= 0:
            # if TAB trigger special shots then it will fire special shots otherwise no
            if special == False:
                if self.player.be_attacked(row, column):
                    arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                else:
                    arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                self.recreate_grid()
                self.on_end()
            elif special == True:
                # set special shots to normal
                special = False
                if self.player.be_attacked(row, column):
                    arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                else:
                    arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                if row + 1 < 8 and column < 8 and row >= 0 and column >= 0 and grid[row + 1][
                    column] == CellStatus.EMPTY:
                    if self.player.be_attacked(row + 1, column):
                        arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                    else:
                        arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                if row < 8 and column + 1 < 8 and row >= 0 and column >= 0 and grid[row][
                    column + 1] == CellStatus.EMPTY:
                    if self.player.be_attacked(row, column + 1):
                        arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                    else:
                        arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                if row < 8 and column < 8 and row - 1 >= 0 and column >= 0 and grid[row - 1][
                    column] == CellStatus.EMPTY:
                    if self.player.be_attacked(row - 1, column):
                        arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                    else:
                        arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                if row < 8 and column < 8 and row >= 0 and column - 1 >= 0 and grid[row][
                    column - 1] == CellStatus.EMPTY:
                    if self.player.be_attacked(row, column - 1):
                        arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                    else:
                        arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                    # Four Head
                if row + 1 < 8 and column + 1 < 8 and row >= 0 and column >= 0 and grid[row + 1][
                    column + 1] == CellStatus.EMPTY:
                    if self.player.be_attacked(row + 1, column + 1):
                        arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                    else:
                        arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                if row < 8 and column + 1 < 8 and row - 1 >= 0 and column >= 0 and grid[row - 1][
                    column + 1] == CellStatus.EMPTY:
                    if self.player.be_attacked(row - 1, column + 1):
                        arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                    else:
                        arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                if row + 1 < 8 and column < 8 and row >= 0 and column - 1 >= 0 and grid[row + 1][
                    column - 1] == CellStatus.EMPTY:
                    if self.player.be_attacked(row + 1, column - 1):
                        arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                    else:
                        arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                if row < 8 and column < 8 and row - 1 >= 0 and column - 1 >= 0 and grid[row - 1][
                    column - 1] == CellStatus.EMPTY:
                    if self.player.be_attacked(row - 1, column - 1):
                        arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))
                    else:
                        arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                self.recreate_grid()
                self.on_end()

    def on_key_press(self, key, modifiers):
        global special
        if key == arcade.key.TAB:
            special = True


class AI_window(arcade.View):
    """
    View for the main game phase (displaying boards and shooting shots)
    """

    def __init__(self, width: int, height: int, title: str, player: Player, on_end, is_own_board: bool):
        """
        Initialize Board Window

        :param: shape_list: the list of shape based on aracde build-in function
        :param: first: the variable to the players who shot first
        :param: width (int): Width of window
        :param: height (int): Height of window
        :param: player (Player): Player data this board shows
        :param: on_end (Function): Function to call when a turn ends
        :param: is_own_board (Bool): Is this board owned by the player it refers to
        :return: None
        :pre: Player1 has been initalized with ships already placed as well as easy-level AI's
        :post: easy-level AI's window initalized
        """

        super().__init__()
        self.shape_list = None
        self.player = player
        self.is_own_board = is_own_board
        self.width = width
        self.height = height
        self.on_end = on_end
        arcade.set_background_color(arcade.color.BLACK)
        self.press()

    def recreate_grid(self):
        """
        Rebuild grid based on updated player data

        :returns: None
        :pre: shape_.list
        :post: self.shape_list is updated to reflect the changing player board underneath
        """

        self.shape_list = arcade.ShapeElementList()
        grid = self.player.board.get_board_view()[0]
        for row in range(8):
            for column in range(8):
                if grid[row][column] == CellStatus.EMPTY:
                    color = arcade.color.WHITE
                elif grid[row][column] == CellStatus.MISS:
                    color = arcade.color.GRAY

                elif grid[row][column] == CellStatus.HIT:
                    color = arcade.color.RED
                x = (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                y = (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2
                current_rect = arcade.create_rectangle_filled(x + OFFSET, y, CELL_WIDTH, CELL_HEIGHT, color)
                self.shape_list.append(current_rect)

    def on_draw(self):
        """
        :param: none
        :pre: AI's board must be initalized already
        :post: Renders the AI class to the screen
        """

        arcade.start_render()
        self.shape_list.draw()
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        numbers.reverse()
        for i in range(8):
            arcade.draw_text(letters[i], (i * 80) + 70, self.width - 20, arcade.color.WHITE)
            arcade.draw_text(numbers[i], 15, (i * 80) + 70, arcade.color.WHITE)
        if self.is_own_board:
            for row in range(8):
                for column in range(8):
                    # Flatmap the list of ship positions, since we don't care which ship has which cell
                    if (row, column) in reduce(list.__add__, self.player.board.get_board_view()[1]):
                        x = (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                        y = (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2
                        arcade.draw_text("X", x + (OFFSET / 2), y - (OFFSET / 2), arcade.color.BLACK, 32)

    def press(self):
        """
        Handles AI shooting at a grid cell including playing sounds
        :returns: None

        :post: Allow user to shot first instead of AI
        """
        # Allow user to shot first
        global first
        if first == True:
            first = False
            self.recreate_grid()
        else:
            grid = self.player.board.get_board_view()[0]
            row = random.randint(0, 7)
            column = random.randint(0, 7)
            while grid[row][column] != CellStatus.EMPTY:
                row = random.randint(0, 7)
                column = random.randint(0, 7)
            for i in range(0,8):
                for j in range(0,8):
                    if grid[i][j] == CellStatus.HIT:
                        if i != 0 and grid[i-1][j] == CellStatus.EMPTY:
                            row = i - 1
                            column = j
                            break
                        elif j != 7 and grid[i][j+1] == CellStatus.EMPTY:
                            row = i
                            column = j + 1
                            break
                        elif i != 7 and grid[i+1][j] == CellStatus.EMPTY:
                            row = i + 1
                            column = j
                            break
                        elif j != 0 and grid[i][j-1] == CellStatus.EMPTY:
                            row = i
                            column = j - 1
                            break
                else:
                    continue
                break

            print(f"Grid coordinates: ({row}, {column})")

            if row < 8 and column < 8 and row >= 0 and column >= 0:
                if self.player.be_attacked(row, column):
                    arcade.play_sound(arcade.load_sound('./sounds/hit.m4a'))

                else:
                    arcade.play_sound(arcade.load_sound('./sounds/miss.m4a'))
                self.recreate_grid()
