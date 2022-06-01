from PyQt6.QtWidgets import *  # star is used for importing all functions of a library to use them without PyQt6. ...
from PyQt6.QtCore import *
import functions
import sys  # only for cmd allowance


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setMinimumSize(QSize(100, 80))

        self.setWindowTitle("Test title")

        self.button = QPushButton("Test button")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.tbwc)

        self.setCentralWidget(self.button)  # Central Window Widget

    def tbwc(self):
        self.button.setText("Unclickable test button")
        self.button.setEnabled(False)
        print('Debug: Clicked the button')


ps = QApplication(sys.argv)  # sys.argv is used to allow usage of cmd args for our app

window = MainWindow()  # creating window
window.show()  # window is hidden by default

ps.exec()  # cycle start point

# OUT OF THE APP ZONE
