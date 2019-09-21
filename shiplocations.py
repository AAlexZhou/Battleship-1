
"""""
Need a player passed to me with number of player
"""""
import arcade
from board import Board
from ship import Ship, Direction

# Set how many rows and columns we will have
ROW_COUNT = 8
COLUMN_COUNT = 8

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 80
HEIGHT = 80

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

#
OFFSET_AXIS_LABEL = 30
OFFSET_BUTTON = 100

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + OFFSET_AXIS_LABEL
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN + OFFSET_AXIS_LABEL + OFFSET_BUTTON
SCREEN_TITLE = "BATTLESHIP"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title)

        self.board = Board()

        self.shape_list = None
        self.length_of_ship = 5
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

        arcade.set_background_color(arcade.color.BLACK)
        self.recreate_grid()

    def recreate_grid(self):
        self.shape_list = arcade.ShapeElementList()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 0:
                    color = arcade.color.WHITE
                else:
                    color = arcade.color.RED

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                current_rect = arcade.create_rectangle_filled(x + OFFSET_AXIS_LABEL, y, WIDTH, HEIGHT, color)
                self.shape_list.append(current_rect)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing

        arcade.start_render()
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        numbers.reverse()
        for i in range(8):
                        arcade.draw_text(letters[i], (i * WIDTH) + 70, SCREEN_WIDTH - 20, arcade.color.WHITE)
                        arcade.draw_text(numbers[i], OFFSET_AXIS_LABEL / 2, (i * HEIGHT) + 70, arcade.color.WHITE)

        self.shape_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        self.column = (x - OFFSET_AXIS_LABEL) // (WIDTH + MARGIN)
        self.row = y // (HEIGHT + MARGIN)

        row = self.row
        column = self.column

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            i = 0
            # Flip the location between 1 and 0.
            if(self.direction == Direction.RIGHT):
                if self.grid[row][column] == 0:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT:
                            self.grid[row][column + i] = 1
                else:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT:
                            self.grid[row][column + i] = 0
                        if row < ROW_COUNT and column < COLUMN_COUNT:
                            self.grid[row][column - i] = 0
            elif(self.direction == Direction.DOWN):
                if self.grid[row][column] == 0:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT:
                            self.grid[row - i][column] = 1
                else:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT:
                            self.grid[row + i][column] = 0
                        if row < ROW_COUNT and column < COLUMN_COUNT:
                            self.grid[row - i][column] = 0
        self.recreate_grid()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.ENTER:
            print(self.row, self.column)
            self.board.place_ships(self.length_of_ship, (self.row, self.column), self.direction)
            if self.length_of_ship > 0:
                self.length_of_ship = self.length_of_ship - 1
                print(self.board.get_board_view()[1])
        if key == arcade.key.SPACE:
            print(f"space")
            if(self.direction == Direction.RIGHT):
                self.direction = Direction.DOWN
                print(self.direction)
            elif(self.direction == Direction.DOWN):
                self.direction = Direction.RIGHT
                print(self.direction)



def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
