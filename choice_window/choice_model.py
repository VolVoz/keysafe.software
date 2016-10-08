# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from design import choice


class ChoiceWindow(QtGui.QMainWindow, choice.Ui_ChoiceWindow):
    def __init__(self, label_text=None, user=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.user = user
        self.label.setText(u'<html><head/><body><p align="center"><span style="font-size:26pt;font-weight:600;">{}</span></p> </body></html>'.format(label_text))
        self.yes.clicked.connect(self.press_yes)
        self.no.clicked.connect(self.press_no)

    def press_no(self):
        self.close()

    def press_yes(self):
        print self.user, "take this key"
        self.close()


