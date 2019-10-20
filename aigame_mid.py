"""
AI Game module containing the Game class for AI and
the SetUp class which gets the information needed for
AI to initialize the mid-level game
"""

import sys
import arcade
from popup_modal import PopupModal
from player import Player
from board_window_mid import AI_window
from board_window_mid import BoardWindow
count = 0
count2 = 0
WINDOW_HEIGHT = 715
WINDOW_WIDTH = 715


class aiGame_mid:
    def __init__(self, player1: Player, player2: Player):
        """
        Constructs a new Game object. Creates an instance of the main menu window.
        :param: player1 (Player) - player 1 in the game
        :param: mdeium-level AI in the game

        :return: returns none.

        :pre: Both Players (Player 2 is AI in this case) have been initialized already with ships placed
        :post AI windows setup
        """

        print("Making game")

        self.player1 = player1
        self.player2 = player2
        self.turn_over = True
        self.game_over = False
        self.is_game_over = False
        self.own_board = arcade.Window(715, 715, "Your Board")
        self.other_board = arcade.Window(715, 715, "Their Board")
        self.player1_own_board = AI_window(
            WINDOW_WIDTH, WINDOW_HEIGHT, "Your Board", self.player1, self.on_turn_end, True)

        self.player1_other_board = BoardWindow(
            WINDOW_WIDTH, WINDOW_HEIGHT, "Their Board", self.player2, self.on_turn_end, False)

        self.own_board.show_view(self.player1_own_board)
        self.other_board.show_view(self.player1_other_board)

        self.current_player = self.player1

    def end_game(self):
        """
        Shows the endgame screen and announces the winner
        :return: returns none.

        :pre the function _init_ compiles successfully
        :post: Application exists (either AI wins or player1 wins)
        """

        self.game_over = True

        self.own_board.set_visible(False)
        self.other_board.set_visible(False)
        if not self.player1.has_lost():
            PopupModal("Player 1 wins!")
            print("Player 1 has won!")
        elif not self.player2.has_lost():
            print("Player 2 has won!")
            PopupModal("Player 2 wins!")

        arcade.schedule(sys.exit, 5)

    def on_turn_end(self):
        """
        Handles switching player states at the end of a turn

        :return: None
        :pre scoreboard function runs successfully
        :post: Switches current player and toggles self.turn_over.
               Also announce the score for each player on scoreboard.
        """
        AI_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Your Board", self.player1, self.on_turn_end, True)
        arcade.pause(1.5)
        y = self.player1.x
        z = self.player2.x
        print(f"                         ScoreBoard                                  ")
        print(f"Player 1's Score: ")
        print(z)
        print(f"")
        print(f"")
        print(f"")
        print(f"AI's Score: ")
        print(y)
        self.turn_over = True

    def run(self, _):
        """
        Handles the flow of the game and deciding when to switch turns
        :return: returns none

        :post: If between turns swaps what board is viewed, If game is over, ends game
        """
        if ((not self.player1.has_lost()) or (not self.player2.has_lost())) and self.turn_over:
            if self.current_player == self.player1:
                self.player1_own_board.recreate_grid()
                self.own_board.show_view(self.player1_own_board)
                self.other_board.show_view(self.player1_other_board)
            self.turn_over = False
        elif (self.player1.has_lost() or self.player2.has_lost()) and not self.is_game_over:
            self.is_game_over = True
            self.end_game()
