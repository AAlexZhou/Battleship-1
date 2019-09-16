import sys
from PyQt5.QtWidgets import QDialog, QApplication
# from gui.board import Ui_MainWindow
from gui.startMenu import Ui_MainWindow

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
