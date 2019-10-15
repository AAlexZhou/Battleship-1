'''
Handles Selection of Ships
'''
import arcade
import player
from button import TextButton
from button import check_mouse_press_for_buttons
from button import check_mouse_release_for_buttons
from gui_shiplocations_a import aShipPlacementView

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
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + OFFSET_AXIS_LABEL #1315
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN + OFFSET_AXIS_LABEL + OFFSET_BUTTON #1415


class aNumberShips(arcade.View):
    '''
    Handles selection for number of ships and passes control off the ShipPlacementView class
    '''
    def __init__(self):
        """
        Constructs a new MainMenuGUI object and sets the background color of the window.
        :return: returns none.

        :pre: The MainMenu class has been run and the user pressed the play_button
        """
        super().__init__()
        self.button_list = []
        self.button_1 = TextButton(110, 320, self.number_1, "1")
        self.button_2 = TextButton(250, 320, self.number_2, "2")
        self.button_3 = TextButton(390, 320, self.number_3, "3")
        self.button_4 = TextButton(530, 320, self.number_4, "4")
        self.button_5 = TextButton(670, 320, self.number_5, "5")

        self.button_list.append(self.button_1)
        self.button_list.append(self.button_2)
        self.button_list.append(self.button_3)
        self.button_list.append(self.button_4)
        self.button_list.append(self.button_5)

    def on_show(self):
        '''
        Ran when view is intially drawn to screen
        :post: The View has a background color
        '''
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        '''
        Ran when view is rendered
        :post: The text and buttons are now on the screen
        '''
        arcade.start_render()
        arcade.draw_text("How many Ships do you want?", SCREEN_WIDTH/1.80, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=45, anchor_x="center")
        for element in self.button_list:
            element.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called whenever the mouse moves
        :param: x (int): the x position of the mouse
        :param: y (int): the y position of the mouse

        :post: Checks to see if a button was pressed by doing check_mouse_press_for_buttons
        """
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called whenever the released the mouse
        :param: x (int): the x position of the mouse
        :param: y (int): the y position of the mouse

        :post: Checks to see if a button was release by doing check_mouse_release_for_buttons
        """
        check_mouse_release_for_buttons(x, y, self.button_list)

    def number_1(self):
        """
        Advances the game state by setting the view to ShipPlacementView and creates two instances of Player with 1 ship
        :return: none

        :post: The game state advances by creating two instances of Player with the correct number of ships and by passing these players into an instance of ShipPlacementView
        """
        num_of_ships = 1
        player1 = player.Player(num_of_ships)
        player2 = player.Player(num_of_ships)
        place_ships_view = aShipPlacementView(player1)
        self.window.show_view(place_ships_view)

    def number_2(self):
        """
        Advances the game state by setting the view to ShipPlacementView and creates two instances of Player with 2 ships
        :return: none

        :post: The game state advances by creating two instances of Player with the correct number of ships and by passing these players into an instance of ShipPlacementView
        """
        num_of_ships = 2
        player1 = player.Player(num_of_ships)
        player2 = player.Player(num_of_ships)
        place_ships_view = aShipPlacementView(player1)
        self.window.show_view(place_ships_view)

    def number_3(self):
        """
        Advances the game state by setting the view to ShipPlacementView and creates two instances of Player with 3 ships
        :return: none

        :post: The game state advances by creating two instances of Player with the correct number of ships and by passing these players into an instance of ShipPlacementView
        """
        num_of_ships = 3
        player1 = player.Player(num_of_ships)
        player2 = player.Player(num_of_ships)
        place_ships_view = aShipPlacementView(player1)
        self.window.show_view(place_ships_view)

    def number_4(self):
        """
        Advances the game state by setting the view to ShipPlacementView and creates two instances of Player with 4 ships
        :return: none

        :post: The game state advances by creating two instances of Player with the correct number of ships and by passing these players into an instance of ShipPlacementView
        """
        num_of_ships = 4
        player1 = player.Player(num_of_ships)
        player2 = player.Player(num_of_ships)
        place_ships_view = aShipPlacementView(player1)
        self.window.show_view(place_ships_view)

    def number_5(self):
        """
        Advances the game state by setting the view to ShipPlacementView and creates two instances of Player with 5 ships
        :return: none

        :post: The game state advances by creating two instances of Player with the correct number of ships and by passing these players into an instance of ShipPlacementView
        """
        num_of_ships = 5
        player1 = player.Player(num_of_ships)
        player2 = player.Player(num_of_ships)
        place_ships_view = aShipPlacementView(player1)
        self.window.show_view(place_ships_view)