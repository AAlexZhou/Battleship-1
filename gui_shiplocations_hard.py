"""""
Handles placing ships in its own View.
Heavily modified version of http://arcade.academy/examples/array_backed_grid_buffered.html#array-backed-grid-buffered
"""""

import arcade
from game import Game
from board import Board
from ship import Ship, Direction
from player import Player
from aigame_hard import aiGame_hard
import random

# Set how many rows and columns we will have
ROW_COUNT = 8
COLUMN_COUNT = 8
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 80
HEIGHT = 80
# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5
# handles offset of screen to allow for space for text and axis
OFFSET_AXIS_LABEL = 30
OFFSET_BUTTON = 100
# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + OFFSET_AXIS_LABEL
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN + OFFSET_AXIS_LABEL + OFFSET_BUTTON
SCREEN_TITLE = "Ship Placement"


class ShipPlacementView_hard(arcade.View):
    """
    View for placing ships on a board
    """

    def __init__(self, player: Player):
        """
        Application constructor.
        :param: width(int) - width of window
        :param: height(int) - height of window
        :param: title (string) - title of window
        :pre: The NumberShips class has been run and the users selected how many ships they want to play with
        """
        super().__init__()
        # initialized global variables
        self.player = player
        self.shape_list = None
        self.length_of_ship = player.num_of_ships
        self.selected = False
        self.row = 0
        self.column = 0
        self.direction = Direction.RIGHT
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell
        self.recreate_grid()

    def on_show(self):
        """
        Sets background color to black
        :post: The View has a background color
        """
        # set background color to black
        arcade.set_background_color(arcade.color.BLACK)

    def recreate_grid(self):
        """
        Redraws grid after event.
        :post: The grid has now update after an event
        """
        self.shape_list = arcade.ShapeElementList()
        # draws each grid box and assigns color based on 2Darray value
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # if grid box is white 2Darray value will be 0
                if self.grid[row][column] == 0:
                    color = arcade.color.WHITE
                # if grid box is red 2Darray value will be 1
                else:
                    color = arcade.color.RED
                # calculates value of x and y coordinates from screen inputs
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                # updates current list values holding grid
                current_rect = arcade.create_rectangle_filled(x + OFFSET_AXIS_LABEL, y, WIDTH, HEIGHT, color)
                self.shape_list.append(current_rect)

    def on_draw(self):
        """
        Initial screen view.
        :post: The grid and text are now on the screen
        """
        arcade.start_render()
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        numbers.reverse()
        for i in range(8):
            arcade.draw_text(letters[i], (i * WIDTH) + 70, SCREEN_WIDTH - 20, arcade.color.WHITE)
            arcade.draw_text(numbers[i], OFFSET_AXIS_LABEL / 2, (i * HEIGHT) + 70, arcade.color.WHITE)
        self.shape_list.draw()
        arcade.draw_text("Press SPACE to rotate, ENTER to lock in the ship", SCREEN_WIDTH / 1.9, 730,
                         arcade.color.WHITE, 28, anchor_x="center")
        if self.length_of_ship == 0:
            dummy_view = DummyView()
            DummyView.players.append(self.player)
            self.window.show_view(dummy_view)
        arcade.draw_text("Ship", 750, 725, arcade.color.WHITE, 15, anchor_x="center")
        arcade.draw_text("Orientation:", 750, 700, arcade.color.WHITE, 15, anchor_x="center")
        if self.direction == Direction.RIGHT:
            arcade.draw_text("Horizontal", 750, 675, arcade.color.WHITE, 15, anchor_x="center")
        else:
            arcade.draw_text("Vertical", 750, 675, arcade.color.WHITE, 15, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        :param: x (int) - x location of mouse press
        :param: y (int) - y location of mouse press
        :param: button (button) - button of mouse press
        :param: modifiers - life cycle method
        :post: Checks to see if a grid cell was pressed and places a ship accordingly
        """
        # Change the x/y screen coordinates to grid coordinates
        self.column = (x - OFFSET_AXIS_LABEL) // (WIDTH + MARGIN)
        self.row = y // (HEIGHT + MARGIN)
        if self.column >= 8 or self.row >= 8 or self.column < 0 or self.row < 0:
            return

        row = self.row
        column = self.column
        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
        # Make sure initial mouse press is on grid
        if row < ROW_COUNT and column < COLUMN_COUNT:
            i = 0
            # allows selection of location of ship to be horizontal
            if self.direction == Direction.RIGHT:
                # if grid cell is white with no ship currently placed, change grid cells to selected based on
                # ship length, origin, and direction and then change setting to ship is successfully selected
                if self.grid[row][column] == 0 and not self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (
                                column + self.length_of_ship - 1) < COLUMN_COUNT:
                            self.grid[row][column + i] = 1
                            self.selected = True
                        else:
                            print(f"invalid placement")
                            self.selected = False
                            break
                # if grid cell is red and ship is selected make current selection ship cells white again and changed
                # selection back to not selection elif self.grid[row][column] == 1 and self.selected: for i in range(
                # self.length_of_ship): if row < ROW_COUNT and column < COLUMN_COUNT and (column +
                # self.length_of_ship - 1) < COLUMN_COUNT: self.grid[row][column + i] = 0 self.selected = False else:
                # print(f"offscreen redo") self.selected = False break if grid cell selected is white and a ship
                # location has already been selected then do not select another ship
                elif self.grid[row][column] == 0 and self.selected:
                    print(f"ship already selected")
                # if grid cell selected is red and a ship location has not been selected then a
                # ship already occupies that location and another grid cell must be selected
                elif self.grid[row][column] == 1 and not self.selected:
                    print(f"there is already a ship in this space")
            # allows selection of location of ship to be vertical
            elif self.direction == Direction.DOWN:
                # if grid cell is white with no ship currently placed, change grid cells to selected based on
                # ship length, origin, and direction and then change setting to ship is successfully selected
                if self.grid[row][column] == 0 and not self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (row - self.length_of_ship + 1) > -1:
                            self.grid[row - i][column] = 1
                            self.selected = True
                        else:
                            print(f"invalid placement")
                            self.selected = False
                            break
                # if grid cell is red and ship is selected make current selection ship cells white again and
                # changed selection back to not selection
                elif self.grid[row][column] == 1 and self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (row - self.length_of_ship + 1) > -1:
                            self.grid[row - i][column] = 0
                            self.selected = False
                        else:
                            print(f"invalid placement")
                            self.selected = False
                            break
                # if grid cell selected is white and a ship location has already been selected
                # then do not select another ship
                elif self.grid[row][column] == 0 and self.selected:
                    print(f"ship already selected")
                # if grid cell selected is red and a ship location has not been selected then a
                # ship already occupies that location and another grid cell must be selected
                elif self.grid[row][column] == 1 and not self.selected:
                    print(f"there is already a ship in this space")
        # redraw grid
        self.recreate_grid()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        :param: key (key) - key pressed
        :param: modifiers - life cycle method
        :post: The ship's location is now locked on the board or the ships orientation is changed
        """
        # sets the location of first ship in board class when enter key is pressed and then remaining
        # ships as they are looped through
        if key == arcade.key.ENTER:
            if self.selected:
                self.selected = False
                print(self.row, self.column)
                self.player.board.place_ships(self.length_of_ship, (self.row, self.column), self.direction)
                # loops through the remaining ships in decreasing length
                if self.length_of_ship > 0:
                    self.length_of_ship = self.length_of_ship - 1
                    self.row = 0
                    self.column = 0
                    print(self.player.board.get_board_view()[1])

            else:
                if self.length_of_ship == 0:
                    print(f"All ships placed")
                else:
                    print(f"please place ship")
        # allows the orientation of the ship placement to change between horizontal and vertical
        # when space bar is pushed and a ship is not currently selected
        if key == arcade.key.SPACE and not self.selected:
            print(f"space")
            if self.direction == Direction.RIGHT:
                self.direction = Direction.DOWN
                print(self.direction)
            elif self.direction == Direction.DOWN:
                self.direction = Direction.RIGHT
                print(self.direction)
        # is space bar is pushed while ship is selected, then orientation is not
        elif key == arcade.key.SPACE and self.selected:
            print(f"cannot change direction while ship is selected")


class DummyView(arcade.View):
    """
    Tells the players to switch between turns and hands off control to Game
    """

    iterations = 0
    players = []
    has_ran = False

    def __init__(self):
        """
        Constructor - calls parent class and increments iterations
        :pre: The ShipPlacementView class has been run and the player has finished placing all their ships
        """
        super().__init__()
        DummyView.iterations += 1

    def on_show(self):
        """
        sets background color to black
        :post: The View has a background color
        """
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        """
        draws text on new window
        :post: The text is now on the screen
        """
        arcade.start_render()
        if DummyView.iterations == 2:
            arcade.draw_text("Starting Game", 200, 450, arcade.color.WHITE, 54)
            arcade.draw_text("Click when Player 1 is ready to play", 180, 400, arcade.color.WHITE, 25)
        else:
            arcade.draw_text("Next Player TURN", 140, 450, arcade.color.WHITE, 54)
            arcade.draw_text("Click when next player is ready", 180, 400, arcade.color.WHITE, 25)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever mouse is pressed.
        :param: key (key) - key pressed
        :param: modifiers - life cycle method
        :post: Checks to see if the mouse was pressed and advances the game state if it was
        """
        player2 = Player(DummyView.players[0].num_of_ships)
        next_player_ships_placement = AI_place(player2)
        self.window.show_view(next_player_ships_placement)
        if DummyView.iterations == 2 and not DummyView.has_ran:
            arcade.get_window().set_visible(False)
            player1 = DummyView.players[0]
            player2 = DummyView.players[1]
            GAME = aiGame_hard(player1, player2)
            arcade.set_window(GAME.player1_other_board)
            arcade.schedule(GAME.run, 0.25)
            DummyView.has_ran = True


class AI_place(arcade.View):

    def __init__(self, player: Player):
        """
            Application constructor.
            :param: width(int) - width of window
            :param: height(int) - height of window
            :param: title (string) - title of window
            :pre: The NumberShips class has been run and the users selected how many ships they want to play with
            """
        super().__init__()
        # initialized global variables
        self.player = player
        self.shape_list = None
        self.length_of_ship = player.num_of_ships
        self.selected = False
        self.row = 0
        self.column = 0
        self.direction = Direction.RIGHT
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell
        for i in range(50):
            self.place()
            self.recreate_grid()
            self.next()

    def on_show(self):
        """
            Sets background color to black
            :post: The View has a background color
            """
        # set background color to black
        arcade.set_background_color(arcade.color.BLACK)

    def recreate_grid(self):
        """
            Redraws grid after event.
            :post: The grid has now update after an event
            """
        self.shape_list = arcade.ShapeElementList()
        # draws each grid box and assigns color based on 2Darray value
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # if grid box is white 2Darray value will be 0
                if self.grid[row][column] == 0:
                    color = arcade.color.WHITE
                # if grid box is red 2Darray value will be 1
                else:
                    color = arcade.color.RED
                # calculates value of x and y coordinates from screen inputs
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                # updates current list values holding grid
                current_rect = arcade.create_rectangle_filled(x + OFFSET_AXIS_LABEL, y, WIDTH, HEIGHT, color)
                self.shape_list.append(current_rect)

    def on_draw(self):
        """
            Initial screen view.
            :post: The grid and text are now on the screen
            """
        arcade.start_render()
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        numbers.reverse()
        for i in range(8):
            arcade.draw_text(letters[i], (i * WIDTH) + 70, SCREEN_WIDTH - 20, arcade.color.WHITE)
            arcade.draw_text(numbers[i], OFFSET_AXIS_LABEL / 2, (i * HEIGHT) + 70, arcade.color.WHITE)
        self.shape_list.draw()
        arcade.draw_text("Press SPACE to rotate, ENTER to lock in the ship", SCREEN_WIDTH / 1.9, 730,
                         arcade.color.WHITE, 28, anchor_x="center")
        if self.length_of_ship == 0:
            dummy_view = DummyView()
            DummyView.players.append(self.player)
            self.window.show_view(dummy_view)
        arcade.draw_text("Ship", 750, 725, arcade.color.WHITE, 15, anchor_x="center")
        arcade.draw_text("Orientation:", 750, 700, arcade.color.WHITE, 15, anchor_x="center")
        if self.direction == Direction.RIGHT:
            arcade.draw_text("Horizontal", 750, 675, arcade.color.WHITE, 15, anchor_x="center")
        else:
            arcade.draw_text("Vertical", 750, 675, arcade.color.WHITE, 15, anchor_x="center")

    def place(self):
        """
            Called when the user presses a mouse button.
            :param: x (int) - x location of mouse press
            :param: y (int) - y location of mouse press
            :param: button (button) - button of mouse press
            :param: modifiers - life cycle method
            :post: Checks to see if a grid cell was pressed and places a ship accordingly
            """
        # Change the x/y screen coordinates to grid coordinates
        row = random.randint(1, 8)
        self.row = row
        column = random.randint(1, 8)
        self.column = column

        # Make sure initial mouse press is on grid
        if row < ROW_COUNT and column < COLUMN_COUNT:
            i = 0
            # allows selection of location of ship to be horizontal
            if self.direction == Direction.RIGHT:
                # if grid cell is white with no ship currently placed, change grid cells to selected based on
                # ship length, origin, and direction and then change setting to ship is successfully selected
                if self.grid[row][column] == 0 and not self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (
                                column + self.length_of_ship - 1) < COLUMN_COUNT:
                            self.grid[row][column + i] = 1
                            self.selected = True
                        else:
                            print(f"invalid placement")
                            self.selected = False
                            break
                # if grid cell is red and ship is selected make current selection ship cells white again and changed
                # selection back to not selection elif self.grid[row][column] == 1 and self.selected: for i in range(
                # self.length_of_ship): if row < ROW_COUNT and column < COLUMN_COUNT and (column +
                # self.length_of_ship - 1) < COLUMN_COUNT: self.grid[row][column + i] = 0 self.selected = False else:
                # print(f"offscreen redo") self.selected = False break if grid cell selected is white and a ship
                # location has already been selected then do not select another ship

                # if grid cell selected is red and a ship location has not been selected then a
                # ship already occupies that location and another grid cell must be selected

            # allows selection of location of ship to be vertical
            elif self.direction == Direction.DOWN:
                # if grid cell is white with no ship currently placed, change grid cells to selected based on
                # ship length, origin, and direction and then change setting to ship is successfully selected
                if self.grid[row][column] == 0 and not self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (row - self.length_of_ship + 1) > -1:
                            self.grid[row - i][column] = 1
                            self.selected = True
                        else:
                            self.selected = False

                # if grid cell is red and ship is selected make current selection ship cells white again and
                # changed selection back to not selection
                elif self.grid[row][column] == 1 and self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (row - self.length_of_ship + 1) > -1:
                            self.grid[row - i][column] = 0
                            self.selected = False
                        else:
                            self.selected = False
                # if grid cell selected is white and a ship location has already been selected
                # then do not select another ship

        # redraw grid

    def next(self):
        """
             Called whenever a key is pressed.
             :param: key (key) - key pressed
             :param: modifiers - life cycle method
             :post: The ship's location is now locked on the board or the ships orientation is changed
             """
        # sets the location of first ship in board class when enter key is pressed and then remaining
        # ships as they are looped through
        if self.selected:
            self.selected = False
            #print(self.row, self.column)
            self.player.board.place_ships(self.length_of_ship, (self.row, self.column), self.direction)
            # loops through the remaining ships in decreasing length
            if self.length_of_ship > 0:
                self.length_of_ship = self.length_of_ship - 1
                self.row = 0
                self.column = 0



        # allows the orientation of the ship placement to change between horizontal and vertical
        # when space bar is pushed and a ship is not currently selected
