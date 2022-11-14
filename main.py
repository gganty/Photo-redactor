import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow
import functions


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = functions.open_image(input())
        self.Open_PushButton.clicked.connect(self.open_picture())
        self.Crop_PushButton.clicked.connect(self.image.crop_image(self.Crop_X_Value_1.text(),
                                                                   self.Crop_Y_Value_1.text(),
                                                                   self.Crop_X_Value_2.text(),
                                                                   self.Crop_Y_Value_2.text()))
        self.BW_PushButton.clicked.connect(self.image.bw())
        self.Invert_PushButton.clicked.connect(self.image.invert())
        self.Curve_PushButton.clicked.connect(self.image.curve(self.CurveRatio_Value.text()))
        self.Resize_PushButton.clicked.connect(self.image.resize_image(self.Resize_X_Value.text(),
                                                                       self.Resize_Y_Value.text()))
        self.Save_PushButton.clicked.connect(self.image.save(self.FileName.text()))

    def open_picture(self):
        self.image = functions.open_image(file=self.FileName.text())


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
