# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(337, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.video_field = QtWidgets.QLineEdit(self.centralwidget)
        self.video_field.setGeometry(QtCore.QRect(20, 20, 201, 29))
        self.video_field.setObjectName("video_field")
        self.ground_data_field = QtWidgets.QLineEdit(self.centralwidget)
        self.ground_data_field.setGeometry(QtCore.QRect(20, 60, 201, 29))
        self.ground_data_field.setObjectName("ground_data_field")
        self.video_buton = QtWidgets.QPushButton(self.centralwidget)
        self.video_buton.setGeometry(QtCore.QRect(230, 20, 91, 29))
        self.video_buton.setObjectName("video_buton")
        self.ground_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.ground_data_button.setGeometry(QtCore.QRect(230, 60, 91, 29))
        self.ground_data_button.setObjectName("ground_data_button")
        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setGeometry(QtCore.QRect(250, 120, 51, 29))
        self.confirm_button.setObjectName("confirm_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выберите входные данные"))
        self.video_buton.setText(_translate("MainWindow", "Выбрать файл"))
        self.ground_data_button.setText(_translate("MainWindow", "Выбрать файл"))
        self.confirm_button.setText(_translate("MainWindow", "OK"))


