from PyQt4 import QtGui

from design import admin_form_design
from new_user.new_user_model import AddNewUser


class AdminForm(QtGui.QMainWindow, admin_form_design.Ui_AdminFormMain):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.new_user_window = AddNewUser()
        self.new_user.clicked.connect(self.register_user)
        self.exit_to_main.clicked.connect(self.exit)

    def register_user(self):
        self.new_user_window.show()

    def exit(self):
        self.close()
