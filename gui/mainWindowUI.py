# -*- coding: utf-8 -*-
# Created: Sun Nov 18 19:39:08 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(868, 504)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SecretButtonLayOut = QtWidgets.QHBoxLayout()
        self.SecretButtonLayOut.setObjectName("SecretButtonLayOut")
        self.SecretButton = QtWidgets.QPushButton(Form)
        self.SecretButton.setMaximumSize(QtCore.QSize(15, 15))
        self.SecretButton.setCheckable(True)
        self.SecretButton.setObjectName("SecretButton")
        self.SecretButtonLayOut.addWidget(self.SecretButton)
        self.SecretButtonLine = QtWidgets.QFrame(Form)
        self.SecretButtonLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.SecretButtonLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SecretButtonLine.setObjectName("SecretButtonLine")
        self.SecretButtonLayOut.addWidget(self.SecretButtonLine)
        self.verticalLayout.addLayout(self.SecretButtonLayOut)
        self.MaxFileName = QtWidgets.QLineEdit(Form)
        self.MaxFileName.setObjectName("MaxFileName")
        self.verticalLayout.addWidget(self.MaxFileName)
        self.RenderPassLabel = QtWidgets.QLabel(Form)
        self.RenderPassLabel.setMaximumSize(QtCore.QSize(100, 30))
        self.RenderPassLabel.setObjectName("RenderPassLabel")
        self.verticalLayout.addWidget(self.RenderPassLabel)
        self.RenderPassLayOut = QtWidgets.QVBoxLayout()
        self.RenderPassLayOut.setObjectName("RenderPassLayOut")
        self.verticalLayout.addLayout(self.RenderPassLayOut)
        self.RenderPassLine = QtWidgets.QFrame(Form)
        self.RenderPassLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.RenderPassLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.RenderPassLine.setObjectName("RenderPassLine")
        self.verticalLayout.addWidget(self.RenderPassLine)
        self.AxfFileLabel = QtWidgets.QLabel(Form)
        self.AxfFileLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.AxfFileLabel.setObjectName("AxfFileLabel")
        self.verticalLayout.addWidget(self.AxfFileLabel)
        self.AxfFileLine = QtWidgets.QFrame(Form)
        self.AxfFileLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.AxfFileLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AxfFileLine.setObjectName("AxfFileLine")
        self.verticalLayout.addWidget(self.AxfFileLine)
        self.AxfFileList = QtWidgets.QListWidget(Form)
        self.AxfFileList.setObjectName("AxfFileList")
        self.verticalLayout.addWidget(self.AxfFileList)
        self.StartRenderButton = QtWidgets.QPushButton(Form)
        self.StartRenderButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.StartRenderButton.setObjectName("StartRenderButton")
        self.verticalLayout.addWidget(self.StartRenderButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.SecretButton, QtCore.SIGNAL("toggled(bool)"), self.MaxFileName.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.SecretButton.setText(QtWidgets.QApplication.translate("Form", "+", None, -1))
        self.RenderPassLabel.setText(QtWidgets.QApplication.translate("Form", "Render Passes", None, -1))
        self.AxfFileLabel.setText(QtWidgets.QApplication.translate("Form", "AXF Files", None, -1))
        self.StartRenderButton.setText(QtWidgets.QApplication.translate("Form", "Start render", None, -1))

