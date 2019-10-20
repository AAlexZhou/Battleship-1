"""
main_menu_gui module contains the MainMenuGUI class for, shockingly, making the main menu gui.
The basic architecture for the code was taken from an example in the Arcade documentation: http://arcade.academy/examples/gui_text_html
"""

import arcade
from button import TextButton
from button import check_mouse_press_for_buttons
from button import check_mouse_release_for_buttons
import sys
from gui_number_ships import NumberShips
from gui_number_ships_mid import NumberShips_mid
from gui_number_ships_a import aNumberShips
from gui_number_ships_hard import NumberShips_hard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class MainMenu(arcade.View):
    '''
    Manages View for Main Menu Screen. Either quits the program or hands control off to NumberShips.
    '''

    def __init__(self):
        '''
        Constructs a MainMenu Object

        :pre: an Arcade window object exists so a View can be displayed on it
        '''
        super().__init__()
        self.button_list = []
        play_button = TextButton(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + 100, self.play_game, "Start")
        easy_button = TextButton(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 3 + 50), self.easy_mode, "Easy AI Mode")
        mid_button = TextButton(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 3), self.mid_mode, " Medium AI Mode")
        hard_button = TextButton(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 3 - 50), self.hard_mode, "Hard AI Mode")
        quit_button = TextButton(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 3) - 100, self.quit_game, "Quit")
        self.button_list.append(play_button)
        self.button_list.append(easy_button)
        self.button_list.append(mid_button)
        self.button_list.append(hard_button)
        self.button_list.append(quit_button)

    def on_show(self):
        '''
        Ran when view is intially rendered

        :post: The View has a background color
        '''
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        '''
        :pre: button class compiles successfully
        :post: The text and buttons are now on the screen
        :return: none
        '''
        arcade.start_render()
        arcade.draw_text("Welcome to KRAAG Battleship!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        for element in self.button_list:
            element.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user clicks the mouse and checks if they clicked a button
        :param: x (int): the x position of the mouse
        :param: y (int): the y position of the mouse
        :return: returns none.

        :post: Checks to see if a button was pressed by doing check_mouse_press_for_buttons
        """
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse click and executes a function if they clicked a button
        :param: x (int): the x position of the mouse
        :param: y (int): the y position of the mouse
        :return: returns none.

        :post: Checks to see if a button was release by doing check_mouse_release_for_buttons
        """
        check_mouse_release_for_buttons(x, y, self.button_list)

    def play_game(self):
        """
        Advances the game state.
        :return: returns none.

        :post: The game state advances to selecting how many ships the users want by changing the view to NumberShips
        """
        ship_num_view = aNumberShips()
        self.window.show_view(ship_num_view)

    @staticmethod
    def quit_game():
        """
        Closes the game.
        :return: returns none.

        :post: The window closes and the program ends
        """
        arcade.close_window()
        sys.exit()  # forcibly exits the python program so no futher windows open

    def easy_mode(self):
        # AI mode
        # return: none
        # post: The game state advances to selecting how many ships the users want by changing the view to NumberShips
        ship_num_view = NumberShips()
        self.window.show_view(ship_num_view)

    def mid_mode(self):
        # AI mode
        # return: none
        # post: The game state advances to selecting how many ships the users want by changing the view to NumberShips
        ship_num_view = NumberShips_mid()
        self.window.show_view(ship_num_view)

    def hard_mode(self):
        # AI mode
        # return: none
        # post: The game state advances to selecting how many ships the users want by changing the view to NumberShips
        ship_num_view = NumberShips_hard()
        self.window.show_view(ship_num_view)
