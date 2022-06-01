from PyQt6.QtWidgets import *  # star is used for importing all functions of a library to use them without PyQt6. ...
# from PIL import Image
# import functions
import sys  # only for cmd allowance

ps = QApplication(sys.argv)  # sys.argv is used to allow usage of cmd args for our app
window = QWidget()  # creating window
window.show()  # window is hidden by default

ps.exec()  # cycle start point

# OUT OF THE APP ZONE
