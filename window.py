# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Resize_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Resize_PushButton.setGeometry(QtCore.QRect(10, 240, 201, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Resize_PushButton.sizePolicy().hasHeightForWidth())
        self.Resize_PushButton.setSizePolicy(sizePolicy)
        self.Resize_PushButton.setObjectName("Resize_PushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 210, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.Crop_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Crop_PushButton.setGeometry(QtCore.QRect(10, 60, 201, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Crop_PushButton.sizePolicy().hasHeightForWidth())
        self.Crop_PushButton.setSizePolicy(sizePolicy)
        self.Crop_PushButton.setObjectName("Crop_PushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 10, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 30, 21, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.BW_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.BW_PushButton.setGeometry(QtCore.QRect(10, 120, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BW_PushButton.sizePolicy().hasHeightForWidth())
        self.BW_PushButton.setSizePolicy(sizePolicy)
        self.BW_PushButton.setObjectName("BW_PushButton")
        self.Invert_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Invert_PushButton.setGeometry(QtCore.QRect(10, 160, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Invert_PushButton.sizePolicy().hasHeightForWidth())
        self.Invert_PushButton.setSizePolicy(sizePolicy)
        self.Invert_PushButton.setObjectName("Invert_PushButton")
        self.Curve_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Curve_PushButton.setGeometry(QtCore.QRect(120, 160, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Curve_PushButton.sizePolicy().hasHeightForWidth())
        self.Curve_PushButton.setSizePolicy(sizePolicy)
        self.Curve_PushButton.setObjectName("Curve_PushButton")
        self.Open_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Open_PushButton.setGeometry(QtCore.QRect(430, 270, 171, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Open_PushButton.sizePolicy().hasHeightForWidth())
        self.Open_PushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Open_PushButton.setFont(font)
        self.Open_PushButton.setObjectName("Open_PushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 110, 81, 16))
        self.label.setObjectName("label")
        self.Crop_X_Value_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Crop_X_Value_1.setGeometry(QtCore.QRect(30, 10, 71, 21))
        self.Crop_X_Value_1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Crop_X_Value_1.setObjectName("Crop_X_Value_1")
        self.Crop_X_Value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Crop_X_Value_2.setGeometry(QtCore.QRect(30, 30, 71, 21))
        self.Crop_X_Value_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Crop_X_Value_2.setObjectName("Crop_X_Value_2")
        self.Crop_Y_Value_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Crop_Y_Value_1.setGeometry(QtCore.QRect(140, 10, 71, 21))
        self.Crop_Y_Value_1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Crop_Y_Value_1.setObjectName("Crop_Y_Value_1")
        self.Crop_Y_Value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Crop_Y_Value_2.setGeometry(QtCore.QRect(140, 30, 71, 21))
        self.Crop_Y_Value_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Crop_Y_Value_2.setObjectName("Crop_Y_Value_2")
        self.CurveRatio_Value = QtWidgets.QLineEdit(self.centralwidget)
        self.CurveRatio_Value.setGeometry(QtCore.QRect(120, 130, 91, 21))
        self.CurveRatio_Value.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.CurveRatio_Value.setObjectName("CurveRatio_Value")
        self.Resize_X_Value = QtWidgets.QLineEdit(self.centralwidget)
        self.Resize_X_Value.setGeometry(QtCore.QRect(30, 210, 71, 21))
        self.Resize_X_Value.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Resize_X_Value.setObjectName("Resize_X_Value")
        self.Resize_Y_Value = QtWidgets.QLineEdit(self.centralwidget)
        self.Resize_Y_Value.setGeometry(QtCore.QRect(140, 210, 71, 21))
        self.Resize_Y_Value.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Resize_Y_Value.setObjectName("Resize_Y_Value")
        self.graphicsView = QtWidgets.QLabel(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(230, 20, 381, 241))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setText("")
        self.graphicsView.setScaledContents(True)
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 0, 47, 13))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 270, 221, 61))
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScrollMargin(1)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(89)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuadditional_functions = QtWidgets.QMenu(self.menubar)
        self.menuadditional_functions.setObjectName("menuadditional_functions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuadditional_functions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Resize_PushButton.setText(_translate("MainWindow", "Resize"))
        self.label_3.setText(_translate("MainWindow", "X:"))
        self.label_4.setText(_translate("MainWindow", "Y:"))
        self.Crop_PushButton.setText(_translate("MainWindow", "Crop"))
        self.label_5.setText(_translate("MainWindow", "X1:"))
        self.label_6.setText(_translate("MainWindow", "Y1:"))
        self.label_7.setText(_translate("MainWindow", "X2:"))
        self.label_8.setText(_translate("MainWindow", "Y2:"))
        self.BW_PushButton.setText(_translate("MainWindow", "B/W"))
        self.Invert_PushButton.setText(_translate("MainWindow", "Invert"))
        self.Curve_PushButton.setText(_translate("MainWindow", "Curve"))
        self.Open_PushButton.setText(_translate("MainWindow", "Open"))
        self.label.setText(_translate("MainWindow", "Curve Ratio:"))
        self.Crop_X_Value_1.setText(_translate("MainWindow", "0"))
        self.Crop_X_Value_2.setText(_translate("MainWindow", "1"))
        self.Crop_Y_Value_1.setText(_translate("MainWindow", "0"))
        self.Crop_Y_Value_2.setText(_translate("MainWindow", "1"))
        self.CurveRatio_Value.setText(_translate("MainWindow", "0"))
        self.Resize_X_Value.setText(_translate("MainWindow", "0"))
        self.Resize_Y_Value.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Preview:"))
        self.menuadditional_functions.setTitle(_translate("MainWindow", "additional functions"))
