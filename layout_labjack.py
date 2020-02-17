# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_labjack.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1939, 1006)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 520, 261, 461))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(170, 60, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 140, 71, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 40, 131, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(0, 20, 131, 41))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 120, 131, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(0, 20, 131, 41))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 200, 221, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.SampleRateSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.SampleRateSpinBox.setGeometry(QtCore.QRect(0, 20, 221, 41))
        self.SampleRateSpinBox.setDecimals(6)
        self.SampleRateSpinBox.setMaximum(100000.0)
        self.SampleRateSpinBox.setProperty("value", 0.0)
        self.SampleRateSpinBox.setObjectName("SampleRateSpinBox")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 270, 221, 61))
        self.groupBox_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.AnalogChannelDropDownList = QtWidgets.QComboBox(self.groupBox_6)
        self.AnalogChannelDropDownList.setGeometry(QtCore.QRect(0, 20, 221, 41))
        self.AnalogChannelDropDownList.setObjectName("AnalogChannelDropDownList")
        self.StartButton = QtWidgets.QPushButton(self.groupBox)
        self.StartButton.setGeometry(QtCore.QRect(20, 350, 221, 41))
        self.StartButton.setObjectName("StartButton")
        self.StopButton = QtWidgets.QPushButton(self.groupBox)
        self.StopButton.setGeometry(QtCore.QRect(20, 410, 221, 41))
        self.StopButton.setObjectName("StopButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 261, 501))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(8, 40, 201, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(8, 150, 201, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 241, 61))
        self.label_3.setObjectName("label_3")
        self.PlotWidget = PlotWidget(self.centralwidget)
        self.PlotWidget.setGeometry(QtCore.QRect(299, 29, 1611, 951))
        self.PlotWidget.setObjectName("PlotWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "                  SETUP"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_2.setText(_translate("MainWindow", "Send"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Sample Rate"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Analog Channel"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.groupBox_2.setTitle(_translate("MainWindow", "             READINGS"))
        self.label.setText(_translate("MainWindow", "READINGS 1"))
        self.label_2.setText(_translate("MainWindow", "READINGS 2"))
        self.label_3.setText(_translate("MainWindow", "Analog Channel: AOCH_1"))


from pyqtgraph import PlotWidget
