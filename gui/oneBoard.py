import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class clickMe(QObject):

    clickclick = pyqtSignal()

    def __init__(self):
        QObject.__init___(self)

    def click1(self):
        self.clickclick.emit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 739)
        MainWindow.setMouseTracking(True)
        # MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 110, 471, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.player_board = QtWidgets.QWidget(self.gridLayoutWidget)
        self.player_board.setEnabled(True)
        self.player_board.setMinimumSize(QtCore.QSize(400, 47))
        self.player_board.setMaximumSize(QtCore.QSize(400, 400))
        self.player_board.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.player_board.setStyleSheet(open("mystylesheet.css").read())
        self.player_board.setObjectName("player_board")

        self.boardLayout_3 = QtWidgets.QGridLayout(self.player_board)
        self.boardLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.boardLayout_3.setSpacing(0)
        self.boardLayout_3.setObjectName("boardLayout_3")

        self.make_col_label()
        self.make_row_label()
        self.make_grid_buttons()

        self.label_yourBoard = QtWidgets.QLabel(self.centralwidget)
        self.label_yourBoard.setGeometry(QtCore.QRect(80, 30, 201, 67))
        self.label_yourBoard.setTextFormat(QtCore.Qt.RichText)
        self.label_yourBoard.setAlignment(QtCore.Qt.AlignCenter)
        self.label_yourBoard.setObjectName("label_yourBoard")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(770, 230, 120, 80))
        self.widget.setObjectName("widget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1160, 21))
        self.menubar.setObjectName("menubar")
        self.menuPlayBoard = QtWidgets.QMenu(self.menubar)
        self.menuPlayBoard.setObjectName("menuPlayBoard")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPlayBoard.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def make_col_label(self):
        self.label_wholeColumn = QtWidgets.QHBoxLayout()
        self.label_wholeColumn.setObjectName("label_wholeColumn")

        self.label_col = {}

        for i in range(8):
            self.label_col[i] = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_wholeColumn.addWidget(self.label_col[i])

        self.gridLayout.addLayout(self.label_wholeColumn, 0, 1, 1, 1)

    def make_row_label(self):
        self.label_wholeRow = QtWidgets.QVBoxLayout()
        self.label_wholeRow.setObjectName("label_wholeRow")

        self.label_row = {}

        for i in range (8):
            self.label_row[i] = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_wholeRow.addWidget(self.label_row[i])

        self.gridLayout.addLayout(self.label_wholeRow, 2, 0, 1, 1)

    def make_grid_buttons(self):
        self.grid = {}
        # self.click_rowIndex = 0
        # self.click_colIndex = 0
        for row in range(8):
            for col in range(8):
                self.grid[(row, col)] = QtWidgets.QPushButton(self.player_board)
                self.grid[(row, col)].setMinimumSize(QtCore.QSize(47, 47))
                self.grid[(row,col)].setObjectName(f"Button Row {row}, Col {col}")
                self.boardLayout_3.addWidget(self.grid[(row, col)], row, col, 1, 1)
                if self.grid[(row, col)].clicked:
                    # temp = clickMe()
                    self.click_colIndex = col
                    self.click_rowIndex = row
                    self.grid[(row, col)].clicked.connect(self.clickclick)

        self.gridLayout.addWidget(self.player_board, 2, 1, 1, 1)

    def clickclick(self):
        # temp_btn = self.sender().text()
        print(f"{temp_btn} clicked")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        for i in range(8):
            self.label_row[i].setText(_translate("MainWindow", str(i) ))

        uppercase_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]

        for i in range(8):
            self.label_col[i].setText(_translate("MainWindow", uppercase_alphabet[i]))
        self.label_yourBoard.setText(_translate("MainWindow", "YOUR BOARD"))
        self.menuPlayBoard.setTitle(_translate("MainWindow", "PlayBoard"))


app = QApplication(sys.argv)
font = QtGui.QFont()
font.setFamily("Segoe UI Black")
font.setPointSize(20)
font.setBold(True)
font.setWeight(75)
app.setFont(font)
window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())


