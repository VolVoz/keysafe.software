# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/keyboard.ui'
#
# Created: Tue Nov 15 19:02:51 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_keyboard(object):
    def setupUi(self, keyboard):
        keyboard.setObjectName(_fromUtf8("keyboard"))
        keyboard.resize(800, 600)
        self.centralwidget = QtGui.QWidget(keyboard)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labe_text = QtGui.QLabel(self.frame_2)
        self.labe_text.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.labe_text.setAlignment(QtCore.Qt.AlignCenter)
        self.labe_text.setObjectName(_fromUtf8("labe_text"))
        self.verticalLayout_2.addWidget(self.labe_text)
        self.input_text = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_text.sizePolicy().hasHeightForWidth())
        self.input_text.setSizePolicy(sizePolicy)
        self.input_text.setObjectName(_fromUtf8("input_text"))
        self.input_text.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.verticalLayout_2.addWidget(self.input_text)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.eee = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eee.sizePolicy().hasHeightForWidth())
        self.eee.setSizePolicy(sizePolicy)
        self.eee.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.eee.setObjectName(_fromUtf8("eee"))
        self.gridLayout.addWidget(self.eee, 1, 2, 1, 1)
        self.ukr_ii = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ukr_ii.sizePolicy().hasHeightForWidth())
        self.ukr_ii.setSizePolicy(sizePolicy)
        self.ukr_ii.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ukr_ii.setObjectName(_fromUtf8("ukr_ii"))
        self.gridLayout.addWidget(self.ukr_ii, 1, 11, 1, 1)
        self.hhh = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hhh.sizePolicy().hasHeightForWidth())
        self.hhh.setSizePolicy(sizePolicy)
        self.hhh.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.hhh.setObjectName(_fromUtf8("hhh"))
        self.gridLayout.addWidget(self.hhh, 2, 5, 1, 1)
        self.qqq = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qqq.sizePolicy().hasHeightForWidth())
        self.qqq.setSizePolicy(sizePolicy)
        self.qqq.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.qqq.setObjectName(_fromUtf8("qqq"))
        self.gridLayout.addWidget(self.qqq, 1, 0, 1, 1)
        self.ppp = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ppp.sizePolicy().hasHeightForWidth())
        self.ppp.setSizePolicy(sizePolicy)
        self.ppp.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ppp.setObjectName(_fromUtf8("ppp"))
        self.gridLayout.addWidget(self.ppp, 1, 9, 1, 1)
        self.vvv = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vvv.sizePolicy().hasHeightForWidth())
        self.vvv.setSizePolicy(sizePolicy)
        self.vvv.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.vvv.setObjectName(_fromUtf8("vvv"))
        self.gridLayout.addWidget(self.vvv, 3, 4, 1, 1)
        self.lll = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lll.sizePolicy().hasHeightForWidth())
        self.lll.setSizePolicy(sizePolicy)
        self.lll.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.lll.setObjectName(_fromUtf8("lll"))
        self.gridLayout.addWidget(self.lll, 2, 8, 1, 1)
        self.ukr_x = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ukr_x.sizePolicy().hasHeightForWidth())
        self.ukr_x.setSizePolicy(sizePolicy)
        self.ukr_x.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ukr_x.setObjectName(_fromUtf8("ukr_x"))
        self.gridLayout.addWidget(self.ukr_x, 1, 10, 1, 1)
        self.yyy = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yyy.sizePolicy().hasHeightForWidth())
        self.yyy.setSizePolicy(sizePolicy)
        self.yyy.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.yyy.setObjectName(_fromUtf8("yyy"))
        self.gridLayout.addWidget(self.yyy, 1, 5, 1, 1)
        self.ukr_e = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ukr_e.sizePolicy().hasHeightForWidth())
        self.ukr_e.setSizePolicy(sizePolicy)
        self.ukr_e.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ukr_e.setObjectName(_fromUtf8("ukr_e"))
        self.gridLayout.addWidget(self.ukr_e, 2, 10, 1, 1)
        self.sss = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sss.sizePolicy().hasHeightForWidth())
        self.sss.setSizePolicy(sizePolicy)
        self.sss.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.sss.setObjectName(_fromUtf8("sss"))
        self.gridLayout.addWidget(self.sss, 2, 1, 1, 1)
        self.ooo = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ooo.sizePolicy().hasHeightForWidth())
        self.ooo.setSizePolicy(sizePolicy)
        self.ooo.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ooo.setObjectName(_fromUtf8("ooo"))
        self.gridLayout.addWidget(self.ooo, 1, 8, 1, 1)
        self.ukr_g = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ukr_g.sizePolicy().hasHeightForWidth())
        self.ukr_g.setSizePolicy(sizePolicy)
        self.ukr_g.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ukr_g.setObjectName(_fromUtf8("ukr_g"))
        self.gridLayout.addWidget(self.ukr_g, 2, 11, 1, 1)
        self.iii = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iii.sizePolicy().hasHeightForWidth())
        self.iii.setSizePolicy(sizePolicy)
        self.iii.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.iii.setObjectName(_fromUtf8("iii"))
        self.gridLayout.addWidget(self.iii, 1, 7, 1, 1)
        self.ttt = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ttt.sizePolicy().hasHeightForWidth())
        self.ttt.setSizePolicy(sizePolicy)
        self.ttt.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ttt.setObjectName(_fromUtf8("ttt"))
        self.gridLayout.addWidget(self.ttt, 1, 4, 1, 1)
        self.ukrt_j = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ukrt_j.sizePolicy().hasHeightForWidth())
        self.ukrt_j.setSizePolicy(sizePolicy)
        self.ukrt_j.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ukrt_j.setObjectName(_fromUtf8("ukrt_j"))
        self.gridLayout.addWidget(self.ukrt_j, 2, 9, 1, 1)
        self.ddd = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ddd.sizePolicy().hasHeightForWidth())
        self.ddd.setSizePolicy(sizePolicy)
        self.ddd.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ddd.setObjectName(_fromUtf8("ddd"))
        self.gridLayout.addWidget(self.ddd, 2, 2, 1, 1)
        self.dott = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dott.sizePolicy().hasHeightForWidth())
        self.dott.setSizePolicy(sizePolicy)
        self.dott.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.dott.setObjectName(_fromUtf8("dott"))
        self.gridLayout.addWidget(self.dott, 3, 10, 1, 1)
        self.ukr_b = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ukr_b.sizePolicy().hasHeightForWidth())
        self.ukr_b.setSizePolicy(sizePolicy)
        self.ukr_b.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ukr_b.setObjectName(_fromUtf8("ukr_b"))
        self.gridLayout.addWidget(self.ukr_b, 3, 8, 1, 1)
        self.mmm = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mmm.sizePolicy().hasHeightForWidth())
        self.mmm.setSizePolicy(sizePolicy)
        self.mmm.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.mmm.setObjectName(_fromUtf8("mmm"))
        self.gridLayout.addWidget(self.mmm, 3, 7, 1, 1)
        self.aaa = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aaa.sizePolicy().hasHeightForWidth())
        self.aaa.setSizePolicy(sizePolicy)
        self.aaa.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.aaa.setObjectName(_fromUtf8("aaa"))
        self.gridLayout.addWidget(self.aaa, 2, 0, 1, 1)
        self.nnn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nnn.sizePolicy().hasHeightForWidth())
        self.nnn.setSizePolicy(sizePolicy)
        self.nnn.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.nnn.setObjectName(_fromUtf8("nnn"))
        self.gridLayout.addWidget(self.nnn, 3, 6, 1, 1)
        self.zero = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero.sizePolicy().hasHeightForWidth())
        self.zero.setSizePolicy(sizePolicy)
        self.zero.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.zero.setObjectName(_fromUtf8("zero"))
        self.gridLayout.addWidget(self.zero, 0, 10, 1, 1)
        self.bbb = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bbb.sizePolicy().hasHeightForWidth())
        self.bbb.setSizePolicy(sizePolicy)
        self.bbb.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.bbb.setObjectName(_fromUtf8("bbb"))
        self.gridLayout.addWidget(self.bbb, 3, 5, 1, 1)
        self.zzz = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zzz.sizePolicy().hasHeightForWidth())
        self.zzz.setSizePolicy(sizePolicy)
        self.zzz.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.zzz.setObjectName(_fromUtf8("zzz"))
        self.gridLayout.addWidget(self.zzz, 3, 1, 1, 1)
        self.ggg = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ggg.sizePolicy().hasHeightForWidth())
        self.ggg.setSizePolicy(sizePolicy)
        self.ggg.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ggg.setObjectName(_fromUtf8("ggg"))
        self.gridLayout.addWidget(self.ggg, 2, 4, 1, 1)
        self.ccc = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ccc.sizePolicy().hasHeightForWidth())
        self.ccc.setSizePolicy(sizePolicy)
        self.ccc.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ccc.setObjectName(_fromUtf8("ccc"))
        self.gridLayout.addWidget(self.ccc, 3, 3, 1, 1)
        self.four = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.four.sizePolicy().hasHeightForWidth())
        self.four.setSizePolicy(sizePolicy)
        self.four.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.four.setObjectName(_fromUtf8("four"))
        self.gridLayout.addWidget(self.four, 0, 4, 1, 1)
        self.rrr = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rrr.sizePolicy().hasHeightForWidth())
        self.rrr.setSizePolicy(sizePolicy)
        self.rrr.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.rrr.setObjectName(_fromUtf8("rrr"))
        self.gridLayout.addWidget(self.rrr, 1, 3, 1, 1)
        self.two = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two.sizePolicy().hasHeightForWidth())
        self.two.setSizePolicy(sizePolicy)
        self.two.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.two.setObjectName(_fromUtf8("two"))
        self.gridLayout.addWidget(self.two, 0, 2, 1, 1)
        self.five = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.five.sizePolicy().hasHeightForWidth())
        self.five.setSizePolicy(sizePolicy)
        self.five.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.five.setObjectName(_fromUtf8("five"))
        self.gridLayout.addWidget(self.five, 0, 5, 1, 1)
        self.six = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.six.sizePolicy().hasHeightForWidth())
        self.six.setSizePolicy(sizePolicy)
        self.six.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.six.setObjectName(_fromUtf8("six"))
        self.gridLayout.addWidget(self.six, 0, 6, 1, 1)
        self.nine = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nine.sizePolicy().hasHeightForWidth())
        self.nine.setSizePolicy(sizePolicy)
        self.nine.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.nine.setObjectName(_fromUtf8("nine"))
        self.gridLayout.addWidget(self.nine, 0, 9, 1, 1)
        self.seven = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seven.sizePolicy().hasHeightForWidth())
        self.seven.setSizePolicy(sizePolicy)
        self.seven.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.seven.setObjectName(_fromUtf8("seven"))
        self.gridLayout.addWidget(self.seven, 0, 7, 1, 1)
        self.eight = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eight.sizePolicy().hasHeightForWidth())
        self.eight.setSizePolicy(sizePolicy)
        self.eight.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.eight.setObjectName(_fromUtf8("eight"))
        self.gridLayout.addWidget(self.eight, 0, 8, 1, 1)
        self.fff = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fff.sizePolicy().hasHeightForWidth())
        self.fff.setSizePolicy(sizePolicy)
        self.fff.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.fff.setObjectName(_fromUtf8("fff"))
        self.gridLayout.addWidget(self.fff, 2, 3, 1, 1)
        self.jjj = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jjj.sizePolicy().hasHeightForWidth())
        self.jjj.setSizePolicy(sizePolicy)
        self.jjj.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.jjj.setObjectName(_fromUtf8("jjj"))
        self.gridLayout.addWidget(self.jjj, 2, 6, 1, 1)
        self.xxx = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xxx.sizePolicy().hasHeightForWidth())
        self.xxx.setSizePolicy(sizePolicy)
        self.xxx.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.xxx.setObjectName(_fromUtf8("xxx"))
        self.gridLayout.addWidget(self.xxx, 3, 2, 1, 1)
        self.kkk = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kkk.sizePolicy().hasHeightForWidth())
        self.kkk.setSizePolicy(sizePolicy)
        self.kkk.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.kkk.setObjectName(_fromUtf8("kkk"))
        self.gridLayout.addWidget(self.kkk, 2, 7, 1, 1)
        self.www = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.www.sizePolicy().hasHeightForWidth())
        self.www.setSizePolicy(sizePolicy)
        self.www.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.www.setObjectName(_fromUtf8("www"))
        self.gridLayout.addWidget(self.www, 1, 1, 1, 1)
        self.ukr_uu = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ukr_uu.sizePolicy().hasHeightForWidth())
        self.ukr_uu.setSizePolicy(sizePolicy)
        self.ukr_uu.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.ukr_uu.setObjectName(_fromUtf8("ukr_uu"))
        self.gridLayout.addWidget(self.ukr_uu, 3, 9, 1, 1)
        self.uuu = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uuu.sizePolicy().hasHeightForWidth())
        self.uuu.setSizePolicy(sizePolicy)
        self.uuu.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.uuu.setObjectName(_fromUtf8("uuu"))
        self.gridLayout.addWidget(self.uuu, 1, 6, 1, 1)
        self.one = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy)
        self.one.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.one.setObjectName(_fromUtf8("one"))
        self.gridLayout.addWidget(self.one, 0, 1, 1, 1)
        self.three = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.three.sizePolicy().hasHeightForWidth())
        self.three.setSizePolicy(sizePolicy)
        self.three.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.three.setObjectName(_fromUtf8("three"))
        self.gridLayout.addWidget(self.three, 0, 3, 1, 1)
        self.exit_from_keyboard = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_from_keyboard.sizePolicy().hasHeightForWidth())
        self.exit_from_keyboard.setSizePolicy(sizePolicy)
        self.exit_from_keyboard.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.exit_from_keyboard.setObjectName(_fromUtf8("exit_from_keyboard"))
        self.gridLayout.addWidget(self.exit_from_keyboard, 4, 3, 1, 2)
        self.okay = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okay.sizePolicy().hasHeightForWidth())
        self.okay.setSizePolicy(sizePolicy)
        self.okay.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.okay.setObjectName(_fromUtf8("okay"))
        self.gridLayout.addWidget(self.okay, 4, 1, 1, 2)
        self.add_space = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_space.sizePolicy().hasHeightForWidth())
        self.add_space.setSizePolicy(sizePolicy)
        self.add_space.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.add_space.setObjectName(_fromUtf8("add_space"))
        self.gridLayout.addWidget(self.add_space, 4, 9, 1, 2)
        self.remove_symbol = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_symbol.sizePolicy().hasHeightForWidth())
        self.remove_symbol.setSizePolicy(sizePolicy)
        self.remove_symbol.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.remove_symbol.setObjectName(_fromUtf8("remove_symbol"))
        self.gridLayout.addWidget(self.remove_symbol, 4, 7, 1, 2)
        self.verticalLayout.addWidget(self.frame)
        keyboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(keyboard)
        QtCore.QMetaObject.connectSlotsByName(keyboard)

    def retranslateUi(self, keyboard):
        keyboard.setWindowTitle(_translate("keyboard", "MainWindow", None))
        self.labe_text.setText(_translate("keyboard", "TextLabel", None))
        self.eee.setText(_translate("keyboard", "У", None))
        self.ukr_ii.setText(_translate("keyboard", "Ї", None))
        self.hhh.setText(_translate("keyboard", "Р", None))
        self.qqq.setText(_translate("keyboard", "Й", None))
        self.ppp.setText(_translate("keyboard", "З", None))
        self.vvv.setText(_translate("keyboard", "М", None))
        self.lll.setText(_translate("keyboard", "Д", None))
        self.ukr_x.setText(_translate("keyboard", "Х", None))
        self.yyy.setText(_translate("keyboard", "Н", None))
        self.ukr_e.setText(_translate("keyboard", "Є", None))
        self.sss.setText(_translate("keyboard", "І", None))
        self.ooo.setText(_translate("keyboard", "Щ", None))
        self.ukr_g.setText(_translate("keyboard", "Ґ", None))
        self.iii.setText(_translate("keyboard", "Ш", None))
        self.ttt.setText(_translate("keyboard", "Е", None))
        self.ukrt_j.setText(_translate("keyboard", "Ж", None))
        self.ddd.setText(_translate("keyboard", "В", None))
        self.dott.setText(_translate("keyboard", ".", None))
        self.ukr_b.setText(_translate("keyboard", "Б", None))
        self.mmm.setText(_translate("keyboard", "Ь", None))
        self.aaa.setText(_translate("keyboard", "Ф", None))
        self.nnn.setText(_translate("keyboard", "Т", None))
        self.zero.setText(_translate("keyboard", "0", None))
        self.bbb.setText(_translate("keyboard", "И", None))
        self.zzz.setText(_translate("keyboard", "Я", None))
        self.ggg.setText(_translate("keyboard", "П", None))
        self.ccc.setText(_translate("keyboard", "С", None))
        self.four.setText(_translate("keyboard", "4", None))
        self.rrr.setText(_translate("keyboard", "К", None))
        self.two.setText(_translate("keyboard", "2", None))
        self.five.setText(_translate("keyboard", "5", None))
        self.six.setText(_translate("keyboard", "6", None))
        self.nine.setText(_translate("keyboard", "9", None))
        self.seven.setText(_translate("keyboard", "7", None))
        self.eight.setText(_translate("keyboard", "8", None))
        self.fff.setText(_translate("keyboard", "А", None))
        self.jjj.setText(_translate("keyboard", "О", None))
        self.xxx.setText(_translate("keyboard", "Ч", None))
        self.kkk.setText(_translate("keyboard", "Л", None))
        self.www.setText(_translate("keyboard", "Ц", None))
        self.ukr_uu.setText(_translate("keyboard", "Ю", None))
        self.uuu.setText(_translate("keyboard", "Г", None))
        self.one.setText(_translate("keyboard", "1", None))
        self.three.setText(_translate("keyboard", "3", None))
        self.exit_from_keyboard.setText(_translate("keyboard", "ВИХІД", None))
        self.okay.setText(_translate("keyboard", "OK", None))
        self.add_space.setText(_translate("keyboard", "\"        \"", None))
        self.remove_symbol.setText(_translate("keyboard", "<", None))

