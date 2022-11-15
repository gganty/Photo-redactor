import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from window import Ui_MainWindow
from PIL import Image


def mix(file_1, file_2, percentage_1st_photo):
    if 1 >= percentage_1st_photo >= 0:
        r, g, b = file_1
        r2, g2, b2 = file_2
        r = r * percentage_1st_photo + r2 * (1 - percentage_1st_photo)
        g = g * percentage_1st_photo + g2 * (1 - percentage_1st_photo)
        b = b * percentage_1st_photo + b2 * (1 - percentage_1st_photo)
        return round(r), round(g), round(b)
    else:
        print('Mix percentage value must be between 0 and 1, both sides included.')


class Window(QMainWindow, Ui_MainWindow):
    def get_file(self):
        self.file_name = QFileDialog.getOpenFileName(self, "Open file", '', "Image (*.png *.jpg)")

    def update_image(self):
        self.graphicsView.setPixmap(QPixmap())
        self.graphicsView.setPixmap(QPixmap(self.file_name[0]))

    def change_a_picture(self):
        self.get_file()
        self.update_image()

    def browse_files(self):
        self.get_file()
        self.image = Picture(
            Image.open(
                self.file_name[0]
            ),
            self.file_name[0].split('/')[-1]
        )
        self.update_image()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_name = QFileDialog.getOpenFileName(self, "Open file", '', "Image (*.png *.jpg)")
        self.image = Picture(Image.open(self.file_name[0]), self.file_name[0].split('/')[-1])
        self.update_image()
        self.Open_PushButton.clicked.connect(lambda: self.change_a_picture())

        self.Crop_PushButton.clicked.connect(
            lambda: self.image.crop_image(
                self.Crop_X_Value_1.text(

                ),
                self.Crop_Y_Value_1.text(

                ),
                self.Crop_X_Value_2.text(

                ),
                self.Crop_Y_Value_2.text(

                )
            )
        )
        self.Crop_PushButton.clicked.connect(lambda: self.update_image())

        self.BW_PushButton.clicked.connect(lambda: self.image.bw())
        self.BW_PushButton.clicked.connect(lambda: self.update_image())

        self.Invert_PushButton.clicked.connect(lambda: self.image.invert())
        self.Invert_PushButton.clicked.connect(lambda: self.update_image())

        self.Curve_PushButton.clicked.connect(lambda: self.image.curve(self.CurveRatio_Value.text()))
        self.Curve_PushButton.clicked.connect(lambda: self.update_image())

        self.Resize_PushButton.clicked.connect(
            lambda: self.image.resize_image(
                self.Resize_X_Value.text(

                ),
                self.Resize_Y_Value.text(

                )
            )
        )
        self.Resize_PushButton.clicked.connect(lambda: self.update_image())


class Picture:
    def __init__(self, file, title):
        self.file = file
        self.title = title
        self.pixels = self.file.load()
        self.x, self.y = self.file.size

    def resize_image(self, x_axis, y_axis):
        self.file = self.file.resize((int(x_axis), int(y_axis)))
        self.file.save(self.title)

    def crop_image(self, x_pos1, y_pos1, x_pos2, y_pos2):
        self.file = self.file.crop((int(x_pos1), int(y_pos1), int(x_pos2), int(y_pos2)))
        self.file.save(self.title)

    def bw(self):
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                a = (r + g + b) // 3
                self.pixels[i, j] = a, a, a
        self.file.save(self.title)

    def invert(self):
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 255 - r, 255 - g, 255 - b
        self.file.save(self.title)

    def curve(self, ratio):
        ratio = int(ratio)
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                brightness = r + g + b if r + g + b > 0 else 1
                if brightness < ratio:
                    k = ratio / brightness
                    self.pixels[i, j] = min(255, int(r * k ** 2)), min(255, int(g * k ** 2)), min(255,
                                                                                                  int(b * k ** 2))
                else:
                    self.pixels[i, j] = r, g, b
        self.file.save(self.title)


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())
