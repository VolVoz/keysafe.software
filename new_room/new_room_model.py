# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import zmq
from design import new_room_design
from info_window.info_model import InfoWindow

from database.models import User, Key
from info_window.info_model import InfoWindow
from new_room.design import new_room_design


class AddNewRoom(QtGui.QMainWindow, new_room_design.Ui_addRoomWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.add_rfid_chip.clicked.connect(self.connect_rfid_chip)
        self.add_new_key.clicked.connect(self.create_key)
        self.exit_to_main.clicked.connect(self.exit)
        self.user = User
        self.key = Key
        self.room.clear()
        self.rfid_chip.clear()
        self.info_error = InfoWindow(label_text=u'Вибачте, сталася помилка, зверніться будь ласка до адміністратора')

    def connect_rfid_chip(self):
        self.startReading()
        self.read_card = InfoWindow(label_text=u"Піднесіть ключ", parent=self, hide_ok=True, read='key')
        self.read_card.showFullScreen()
        QtCore.QTimer.singleShot(5000, self.read_card.return_rfid)

    def startReading(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("readTeacherId")

    def create_key(self):
        room = unicode(self.room.text().toUtf8(), encoding="UTF-8")
        rfid_chip = unicode(self.rfid_chip.text().toUtf8(), encoding="UTF-8")
        try:
            if self.user.get_by_rfid(rfid_chip)['warnings'] and self.key.get_by_rfid(rfid_chip)['warnings']:
                new_key = self.key.create(room, rfid_chip)
                if new_key['errors'] or new_key['warnings']:
                    if 'place' in new_key['warnings'].message:
                        self.info = InfoWindow(label_text=u'Немає вільних місць для ключів',
                                               parent=self)
                        self.info.showFullScreen()
                        QtCore.QTimer.singleShot(5000, self.info.close)
                        QtCore.QTimer.singleShot(5000, self.close)
                    else:
                        self.info_error.showFullScreen()
                        QtCore.QTimer.singleShot(5000, self.info_error.close)
                else:
                    self.info = InfoWindow(label_text=u'Будь ласка, поставте ключ у приймач протягом 10 секунд', parent=self)
                    self.info.showFullScreen()
                    QtCore.QTimer.singleShot(5000, self.info.close)
                    QtCore.QTimer.singleShot(5000, self.close)
            else:
                self.info = InfoWindow(label_text=u'Такий RFID ключ вже зареєстрований у системі')
                self.info.showFullScreen()
                QtCore.QTimer.singleShot(5000, self.info.close)
        except:
            self.info_error.showFullScreen()
            QtCore.QTimer.singleShot(5000, self.info_error.close)

    def exit(self):
        self.room.clear()
        self.rfid_chip.clear()
        self.close()
