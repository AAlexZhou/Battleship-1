"""
button module contains the TextButton class for creating buttons with text in them. It also contains
the functions check_mouse_press_for_buttons and check_mouse_release_for_buttons which check if a button was pressed.
It also contains several classes of specific buttons used throughout the program.
The code for the TextButton class and the functions check_mouse_press_for_buttons and check_mouse_release_for_buttons
was taken from an example in the Arcade documentation: http://arcade.academy/examples/gui_text_button.html
"""
import arcade


class Button:
    """
    Button class to make the creation of buttons easier - text based button  
    """
    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        """
        Constructs a button with position, text, font size, color, button width and height
        :param: center_x (int) - center location of x coordinate
        :param: center_y (int) - center location of y coordinate
        :param: width (int) - width of button
        :param: length (int) - length of button
        :param: text - text that goes on button
        :param: font_face - font of text
        :param: face_color - sets button color to light gray
        :param: highlight_color - sets highlight color to white
        :param: shadow_color - sets shadow color to gray
        :param: button_height (int) - sets height to gray

        :pre: A window or view exists for the button to be created on
        """
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """
        initiates the button as a rectable with position and
        tracks whether or not the given button is pressed and displays corresponding color
        :return: returns none.

        :post: The button is drawn on the window
        """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        """
        bool controlling whether the button is pressed or not

        :post: self.pressed is true, allowing draw to know that it needs to do the clicked animation
        """
        self.pressed = True

    def on_release(self):
        """
        bool checking whether button is released

        :post: self.pressed is False, allowing draw to know that it needs to do the release animation
        """
        self.pressed = False


def check_mouse_press_for_buttons(x, y, button_list):
    """
    Given an x, y, see if we need to register any button clicks. 
    :param: x (int) - x position of mousepress
    :param: y (int) - y position of mousepress
    :param: button_list - contains list of buttons to search through

    :post: the button now knows whether it was pressed or not
    """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(x, y, button_list):
    """ 
    If a mouse button has been released, see if we need to process
    any release events. 
    :param: x (int) - x position of mousepress
    :param: y (int) - y position of mousepress
    :param: button_list - contains list of buttons to search through

    :post: Any relevent functions associated with the pressed button are executed
    """
    for button in button_list:
        if button.pressed:
            button.on_release()


class TextButton(Button):
    """
    Button class that deals with Text based buttons
    """
    def __init__(self, center_x, center_y, action_function, text):
        """
        Constructs a new NumberButton.
        :param: center_x (int): x position of where the center of the button is so the textbutton class can draw it.
        :param: center_y (int): y position of where the center of the button is so the textbutton class can draw it.
        :param: action_function: The function that is executed when the button is pressed.
        :return: returns none.

        :pre: A window or view exists for the button to be created on
        """
        super().__init__(center_x, center_y, 120, 45, text, 17, "Arial")
        self.action_function = action_function

    def on_release(self):
        """
        implements methods necessary when button is released
        :return: none

        :post: The action_function is executed
        """
        super().on_release()
        self.action_function()




