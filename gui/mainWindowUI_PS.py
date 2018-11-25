# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUI.ui'
#
# Created: Mon Nov 19 14:56:10 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SecretButtonLayOut = QtGui.QHBoxLayout()
        self.SecretButtonLayOut.setObjectName("SecretButtonLayOut")
        self.SecretButton = QtGui.QPushButton(self.centralwidget)
        self.SecretButton.setMaximumSize(QtCore.QSize(15, 15))
        self.SecretButton.setCheckable(True)
        self.SecretButton.setObjectName("SecretButton")
        self.SecretButtonLayOut.addWidget(self.SecretButton)
        self.SecretButtonLine = QtGui.QFrame(self.centralwidget)
        self.SecretButtonLine.setFrameShape(QtGui.QFrame.HLine)
        self.SecretButtonLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.SecretButtonLine.setObjectName("SecretButtonLine")
        self.SecretButtonLayOut.addWidget(self.SecretButtonLine)
        self.verticalLayout.addLayout(self.SecretButtonLayOut)
        self.MaxFileName = QtGui.QLineEdit(self.centralwidget)
        self.MaxFileName.setObjectName("MaxFileName")
        self.verticalLayout.addWidget(self.MaxFileName)
        self.RenderPassLine = QtGui.QFrame(self.centralwidget)
        self.RenderPassLine.setFrameShape(QtGui.QFrame.HLine)
        self.RenderPassLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.RenderPassLine.setObjectName("RenderPassLine")
        self.verticalLayout.addWidget(self.RenderPassLine)
        self.RenderPassLabel = QtGui.QLabel(self.centralwidget)
        self.RenderPassLabel.setMaximumSize(QtCore.QSize(100, 30))
        self.RenderPassLabel.setObjectName("RenderPassLabel")
        self.verticalLayout.addWidget(self.RenderPassLabel)
        self.RenderPassLayOut = QtGui.QVBoxLayout()
        self.RenderPassLayOut.setObjectName("RenderPassLayOut")
        self.verticalLayout.addLayout(self.RenderPassLayOut)
        self.AxfFileLine = QtGui.QFrame(self.centralwidget)
        self.AxfFileLine.setFrameShape(QtGui.QFrame.HLine)
        self.AxfFileLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.AxfFileLine.setObjectName("AxfFileLine")
        self.verticalLayout.addWidget(self.AxfFileLine)
        self.AxfFileLabel = QtGui.QLabel(self.centralwidget)
        self.AxfFileLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.AxfFileLabel.setObjectName("AxfFileLabel")
        self.verticalLayout.addWidget(self.AxfFileLabel)
        self.AxfFileList = QtGui.QListWidget(self.centralwidget)
        self.AxfFileList.setObjectName("AxfFileList")
        self.verticalLayout.addWidget(self.AxfFileList)
        self.StartRenderButton = QtGui.QPushButton(self.centralwidget)
        self.StartRenderButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.StartRenderButton.setObjectName("StartRenderButton")
        self.verticalLayout.addWidget(self.StartRenderButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "BruDigital_AXFrender", None, QtGui.QApplication.UnicodeUTF8))
        self.SecretButton.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.RenderPassLabel.setText(QtGui.QApplication.translate("MainWindow", "Render Passes", None, QtGui.QApplication.UnicodeUTF8))
        self.AxfFileLabel.setText(QtGui.QApplication.translate("MainWindow", "AXF Files", None, QtGui.QApplication.UnicodeUTF8))
        self.StartRenderButton.setText(QtGui.QApplication.translate("MainWindow", "Start render", None, QtGui.QApplication.UnicodeUTF8))

