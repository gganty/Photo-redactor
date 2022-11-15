import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from window import Ui_MainWindow
from PIL import Image
import sqlite3


class Window(QMainWindow, Ui_MainWindow):
    def get_file(self):
        """
        Gets picture file from a dialog window.
        :return: None
        """
        self.file_name = QFileDialog.getOpenFileName(self, "Open file", '', "Image (*.png *.jpg)")

    def update_all(self, activity):
        """
        Updates history database and changes picture in QPixman.
        :param activity: Receives last activity to add it to database. Write 'None' if not needed.
        :return: None
        """
        self.graphicsView.setPixmap(QPixmap())
        self.graphicsView.setPixmap(QPixmap(self.file_name[0]))
        if activity:
            self.cur.execute('''INSERT INTO actions (action) VALUES (?);''', (activity,))
            res = self.cur.execute('''SELECT * FROM actions;''').fetchall()
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def change_a_picture(self):
        """
        Changes picture.
        :return: None
        """
        self.get_file()
        self.update_all(False)

    def browse_files(self):
        """
        Changes picture and creates a new object of class Picture.
        :return: None
        """
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
        self.image = Picture(Image.open(self.file_name[0]), self.file_name[0].split('/')[-1])
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
    def __init__(self, file, title):
        """
        Creates a Picture object.
        Requires parameters file and title.
        :param file: Path to file, separated with '/'.
        :param title: Name of the file.
        """
        self.file = file
        self.title = title
        self.pixels = self.file.load()
        self.x, self.y = self.file.size

    def resize_image(self, x_axis, y_axis):
        """
        def resize_image(self, x_axis, y_axis)
        Resizes image with given lengths.
        Function saves the file.
        :param x_axis: int, length.
        :param y_axis: int, height.
        :return: None
        """
        self.file = self.file.resize((int(x_axis), int(y_axis)))
        self.file.save(self.title)

    def crop_image(self, x_pos1, y_pos1, x_pos2, y_pos2):
        """
        def crop_image(self, x_pos1, y_pos1, x_pos2, y_pos2)
        Crops the image with a recktange, positioned with 2 dots, both need x and y arguements.
        Function saves the file.
        :param x_pos1: int, x value of upper-left corner position.
        :param y_pos1: int, y value of upper-left corner position.
        :param x_pos2: int, x value of lower-right corner position.
        :param y_pos2: int, y value of lower-right corner position.
        :return: None
        """
        self.file = self.file.crop((int(x_pos1), int(y_pos1), int(x_pos2), int(y_pos2)))
        self.file.save(self.title)

    def bw(self):
        """
        def bw(self)
        Makes an image to contain only black, gray and white colours.
        Function saves the file.
        :return: None
        """
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                a = (r + g + b) // 3
                self.pixels[i, j] = a, a, a
        self.file.save(self.title)

    def invert(self):
        """
        def invert(self)
        Inverts the colors of an image.
        Function saves the file.
        :return: None
        """
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 255 - r, 255 - g, 255 - b
        self.file.save(self.title)

    def curve(self, ratio):
        """
        def curve(self, ratio):
        Whitens an image with a certain strength, received in ratio
        :param ratio: int, strength of the whitening
        :return: None
        """
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
# ура
