import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from dist.window import Ui_MainWindow
from PIL import Image
import sqlite3


class Window(QMainWindow, Ui_MainWindow):
    def get_file(self):
        self.file_name = QFileDialog.getOpenFileName(self, "Open file", '', "Image (*.png *.jpg)")

    def update_all(self, activity):
        self.graphicsView.setPixmap(QPixmap())
        self.graphicsView.setPixmap(QPixmap(self.file_name[0]))
        if activity:
            self.cur.execute('''INSERT INTO actions (action) VALUES (?);''', (activity, ))
            res = self.cur.execute('''SELECT * FROM actions;''').fetchall()
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def change_a_picture(self):
        self.get_file()
        self.update_all(False)

    def browse_files(self):
        self.get_file()
        self.image = Picture(
            Image.open(
                self.file_name[0]
            ),
            self.file_name[0].split('/')[-1]
        )
        self.update_all(False)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_name = QFileDialog.getOpenFileName(self, "Open file", '', "Image (*.png *.jpg)")
        self.image = Picture(Image.open(self.file_name[0]), self.file_name[0].split('/')[-1], self.file_name[0])
        self.update_all(False)
        self.Open_PushButton.clicked.connect(lambda: self.change_a_picture())
        self.con = sqlite3.connect('history.db')
        self.cur = self.con.cursor()
        res = self.cur.execute('''SELECT * FROM actions;''').fetchall()
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

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
        self.Crop_PushButton.clicked.connect(lambda: self.update_all('Cropping'))

        self.BW_PushButton.clicked.connect(lambda: self.image.bw())
        self.BW_PushButton.clicked.connect(lambda: self.update_all('Black/White'))

        self.Invert_PushButton.clicked.connect(lambda: self.image.invert())
        self.Invert_PushButton.clicked.connect(lambda: self.update_all('Inverting'))

        self.Curve_PushButton.clicked.connect(lambda: self.image.curve(self.CurveRatio_Value.text()))
        self.Curve_PushButton.clicked.connect(lambda: self.update_all('Brightening'))

        self.Resize_PushButton.clicked.connect(
            lambda: self.image.resize_image(
                self.Resize_X_Value.text(

                ),
                self.Resize_Y_Value.text(

                )
            )
        )
        self.Resize_PushButton.clicked.connect(lambda: self.update_all('Resizing'))


class Picture:
    def __init__(self, file, title, path):
        self.file = file
        self.title = title
        self.path = path
        self.pixels = self.file.load()
        self.x, self.y = self.file.size

    def resize_image(self, x_axis, y_axis):
        self.file = self.file.resize((int(x_axis), int(y_axis)))
        self.file.save(self.path, 'jpeg')

    def crop_image(self, x_pos1, y_pos1, x_pos2, y_pos2):
        self.file = self.file.crop((int(x_pos1), int(y_pos1), int(x_pos2), int(y_pos2)))
        self.file.save(self.path, 'jpeg')

    def bw(self):
        for i in range(self.x):
            for j in range(self.y):
                if 'png' in self.path:
                    r, g, b, a = self.pixels[i, j]
                else:
                    r, g, b = self.pixels[i, j]
                a = (r + g + b) // 3
                self.pixels[i, j] = a, a, a
        self.file.save(self.path)

    def invert(self):
        for i in range(self.x):
            for j in range(self.y):
                if 'png' in self.path:
                    r, g, b, a = self.pixels[i, j]
                else:
                    r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 255 - r, 255 - g, 255 - b
        self.file.save(self.path)

    def curve(self, ratio):
        ratio = int(ratio)
        for i in range(self.x):
            for j in range(self.y):
                if 'png' in self.path:
                    r, g, b, a = self.pixels[i, j]
                    brightness = r + g + b if r + g + b > 0 else 1
                else:
                    r, g, b = self.pixels[i, j]
                    brightness = r + g + b if r + g + b > 0 else 1
                if brightness < ratio:
                    k = ratio / brightness
                    self.pixels[i, j] = min(255, int(r * k ** 2)), min(255, int(g * k ** 2)), min(255,
                                                                                                  int(b * k ** 2))
                else:
                    self.pixels[i, j] = r, g, b
        self.file.save(self.path)


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())
# ура
