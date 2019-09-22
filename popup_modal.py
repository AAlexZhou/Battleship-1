import arcade

class PopupModal(arcade.Window):
    def __init__(self, text):
        super().__init__(400, 200, "")
        self.text = text

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Render to the screen.
        """

        arcade.start_render()
        arcade.draw_text(self.text, 100, 100, arcade.color.BLACK, 32)
