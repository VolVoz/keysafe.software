# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

from design import delete_keys_design
from choice_window.choice_model import ChoiceWindow
from info_window.info_model import InfoWindow
from database.models import Key

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


class DeleteKeysWindow(QtGui.QMainWindow, delete_keys_design.Ui_DeleteKeys):
    def __init__(self, keys):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.exit_to_main.clicked.connect(self.exit)
        if keys:
            buttons = {}
            row_count = 0
            for key in keys:
                buttons[key.id] = QtGui.QPushButton(self.scrollAreaWidgetContents)
                buttons[key.id].setFixedSize(150, 100)
                if key.status is True:
                    buttons[key.id].setStyleSheet('QPushButton {background-color: #669900;'
                                                  'color: #ffffff;'
                                                  'font: 75 40pt DejaVu Sans Mono for Powerline;}')
                else:
                    buttons[key.id].setStyleSheet('QPushButton {background-color: #cc3300;'
                                                  'color: #ffffff;'
                                                  'font: 75 40pt DejaVu Sans Mono for Powerline;}')
                buttons[key.id].setText(_translate("GetKeyWindow", str(key.room.encode('utf-8')), None))
                buttons[key.id].setObjectName(key.rfid_chip)
                buttons[key.id].clicked.connect(self.button_clicked)
                self.gridLayout_2.addWidget(buttons[key.id], int(row_count % 3), int(row_count / 3))
                row_count += 1

    def button_clicked(self):
        sender = self.sender()
        key = Key.get_by_rfid(str(sender.objectName()))
        if key['data']:
            self.choice = ChoiceWindow(
                operation='delete_key',
                label_text=u'Видалити ключ від кімнати {} ?'.format(key['data'].room),
                key=key['data'].rfid_chip,
                parent=self)
            self.choice.showFullScreen()
            QtCore.QTimer.singleShot(10000, self.choice.close)
        elif key['warnings']:
            self.info = InfoWindow(label_text=u'У системі незнадено такого ключа')
            self.info.showFullScreen()
            QtCore.QTimer.singleShot(5000, self.info.close)
        else:
            self.info = InfoWindow(label_text=u'Вибачте, сталася помилка,зверніться будь ласка до адміністратора')
            self.info.showFullScreen()
            QtCore.QTimer.singleShot(5000, self.info.close)

    def exit(self):
        self.close()

