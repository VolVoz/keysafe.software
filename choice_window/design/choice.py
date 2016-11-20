# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../QtUserInterfaces/chooise_window.ui'
#
# Created: Mon Sep 26 10:28:33 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_ChoiceWindow(object):
    def setupUi(self, ChoiceWindow):
        ChoiceWindow.setObjectName(_fromUtf8("ChoiceWindow"))
        ChoiceWindow.resize(640, 480)
        self.ChoiceFormWidget = QtGui.QWidget(ChoiceWindow)
        self.ChoiceFormWidget.setObjectName(_fromUtf8("ChoiceFormWidget"))
        self.gridLayout = QtGui.QGridLayout(self.ChoiceFormWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalGroupBox = QtGui.QGroupBox(self.ChoiceFormWidget)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.horizontalGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.horizontalGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.yes = QtGui.QPushButton(self.horizontalGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yes.sizePolicy().hasHeightForWidth())
        self.yes.setSizePolicy(sizePolicy)
        self.yes.setObjectName(_fromUtf8("yes"))
        self.gridLayout_2.addWidget(self.yes, 1, 0, 1, 1)
        self.no = QtGui.QPushButton(self.horizontalGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no.sizePolicy().hasHeightForWidth())
        self.no.setSizePolicy(sizePolicy)
        self.no.setObjectName(_fromUtf8("no"))
        self.gridLayout_2.addWidget(self.no, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.horizontalGroupBox, 0, 0, 1, 1)
        ChoiceWindow.setCentralWidget(self.ChoiceFormWidget)

        self.retranslateUi(ChoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ChoiceWindow)

    def retranslateUi(self, ChoiceWindow):
        ChoiceWindow.setWindowTitle(_translate("ChoiceWindow", "MainWindow", None))
        self.yes.setText(_translate("ChoiceWindow", "ТАК", None))
        self.no.setText(_translate("ChoiceWindow", "НІ", None))
        self.yes.setStyleSheet('QPushButton {background-color: #ffffff; color: #000000;'
                               'font: 75 50pt DejaVu Sans Mono for Powerline;}')
        self.no.setStyleSheet('QPushButton {background-color: #ffffff; color: #000000;'
                               'font: 75 50pt DejaVu Sans Mono for Powerline;}')