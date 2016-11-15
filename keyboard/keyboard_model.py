# -*- coding: utf-8 -*-
from PyQt4 import QtGui

from design import keyboard_design


class KeyboardWindow(QtGui.QMainWindow, keyboard_design.Ui_keyboard):
    def __init__(self, parent, edit_text):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.edit_text = edit_text
        self.parent_text = self.parent.text()
        self.input_text.setText(self.parent_text)
        self.labe_text.setText(u'<html><head/><body><p align="center"><span style="font-size:26pt;font-weight:600;">Введіть {}</span></p> </body></html>'.format(edit_text))
        self.exit_from_keyboard.clicked.connect(self.back)
        self.okay.clicked.connect(self.input_accept)
        self.qqq.clicked.connect(self.qqq_main)
        self.www.clicked.connect(self.www_main)
        self.eee.clicked.connect(self.eee_main)
        self.rrr.clicked.connect(self.rrr_main)
        self.ttt.clicked.connect(self.ttt_main)
        self.yyy.clicked.connect(self.yyy_main)
        self.uuu.clicked.connect(self.uuu_main)
        self.iii.clicked.connect(self.iii_main)
        self.ooo.clicked.connect(self.ooo_main)
        self.ppp.clicked.connect(self.ppp_main)
        self.aaa.clicked.connect(self.aaa_main)
        self.sss.clicked.connect(self.sss_main)
        self.ddd.clicked.connect(self.ddd_main)
        self.fff.clicked.connect(self.fff_main)
        self.ggg.clicked.connect(self.ggg_main)
        self.hhh.clicked.connect(self.hhh_main)
        self.jjj.clicked.connect(self.jjj_main)
        self.kkk.clicked.connect(self.kkk_main)
        self.lll.clicked.connect(self.lll_main)
        self.zzz.clicked.connect(self.zzz_main)
        self.xxx.clicked.connect(self.xxx_main)
        self.ccc.clicked.connect(self.ccc_main)
        self.vvv.clicked.connect(self.vvv_main)
        self.bbb.clicked.connect(self.bbb_main)
        self.nnn.clicked.connect(self.nnn_main)
        self.mmm.clicked.connect(self.mmm_main)
        self.one.clicked.connect(self.one_main)
        self.two.clicked.connect(self.two_main)
        self.three.clicked.connect(self.three_main)
        self.four.clicked.connect(self.four_main)
        self.five.clicked.connect(self.five_main)
        self.six.clicked.connect(self.six_main)
        self.seven.clicked.connect(self.seven_main)
        self.eight.clicked.connect(self.eith_main)
        self.nine.clicked.connect(self.nine_main)
        self.zero.clicked.connect(self.zero_main)
        self.add_space.clicked.connect(self.add_space_main)
        self.remove_symbol.clicked.connect(self.remove)
        self.ukr_x.clicked.connect(self.ukr_x_main)
        self.ukr_ii.clicked.connect(self.ukr_ii_main)
        self.ukr_g.clicked.connect(self.ukr_g_main)
        self.ukr_e.clicked.connect(self.ukr_e_main)
        self.ukr_b.clicked.connect(self.ukr_b_main)
        self.ukr_uu.clicked.connect(self.ukr_uu_main)
        self.dott.clicked.connect(self.dot_main)

    def back(self):
        self.close()

    def input_accept(self):
        text = self.input_text.text()
        self.parent.setText(text)
        self.close()

    def remove(self):
        self.input_text.backspace()

    def add_space_main(self):
        self.input_text.insert(u" ")

    def qqq_main(self):
        self.input_text.insert(u"Й")

    def www_main(self):
        self.input_text.insert(u"Ц")

    def eee_main(self):
        self.input_text.insert(u"У")

    def rrr_main(self):
        self.input_text.insert(u"К")

    def ttt_main(self):
        self.input_text.insert(u"Е")

    def yyy_main(self):
        self.input_text.insert(u"Н")

    def uuu_main(self):
        self.input_text.insert(u"Г")

    def iii_main(self):
        self.input_text.insert(u"Ш")

    def ooo_main(self):
        self.input_text.insert(u"Щ")

    def ppp_main(self):
        self.input_text.insert(u"З")

    def ukr_x_main(self):
        self.input_text.insert(u"Х")

    def ukr_ii_main(self):
        self.input_text.insert(u"Ї")

    def aaa_main(self):
        self.input_text.insert(u"Ф")

    def sss_main(self):
        self.input_text.insert(u"І")

    def ddd_main(self):
        self.input_text.insert(u"В")

    def fff_main(self):
        self.input_text.insert(u"А")

    def ggg_main(self):
        self.input_text.insert(u"П")

    def hhh_main(self):
        self.input_text.insert(u"Р")

    def jjj_main(self):
        self.input_text.insert(u"О")

    def kkk_main(self):
        self.input_text.insert(u"Л")

    def lll_main(self):
        self.input_text.insert(u"Д")

    def ukr_g_main(self):
        self.input_text.insert(u"Ґ")

    def ukr_e_main(self):
        self.input_text.insert(u"Є")

    def zzz_main(self):
        self.input_text.insert(u"Я")

    def xxx_main(self):
        self.input_text.insert(u"Ч")

    def ccc_main(self):
        self.input_text.insert(u"С")

    def vvv_main(self):
        self.input_text.insert(u"М")

    def bbb_main(self):
        self.input_text.insert(u"И")

    def nnn_main(self):
        self.input_text.insert(u"Т")

    def mmm_main(self):
        self.input_text.insert(u"Ь")

    def ukr_b_main(self):
        self.input_text.insert(u"Б")

    def ukr_uu_main(self):
        self.input_text.insert(u"Ю")

    def dot_main(self):
        self.input_text.insert(u".")

    def one_main(self):
        self.input_text.insert(u"1")

    def two_main(self):
        self.input_text.insert(u"2")

    def three_main(self):
        self.input_text.insert(u"3")

    def four_main(self):
        self.input_text.insert(u"4")

    def five_main(self):
        self.input_text.insert(u"5")

    def six_main(self):
        self.input_text.insert(u"6")

    def seven_main(self):
        self.input_text.insert(u"7")

    def eith_main(self):
        self.input_text.insert(u"8")

    def nine_main(self):
        self.input_text.insert(u"9")

    def zero_main(self):
        self.input_text.insert(u"0")
