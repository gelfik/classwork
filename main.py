# from PyQt5 import QtWidgets, uic
# import sys
#
# app = QtWidgets.QApplication([])
# win = uic.loadUi("untitled.ui")  # расположение вашего файла .ui
#
# win.show()
# sys.exit(app.exec())
import random

from PyQt5 import QtWidgets
from design import Ui_MainWindow  # импорт нашего сгенерированного файла
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
import sys


def error(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(text)
    msg.setWindowTitle("Error")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


class mywindow_savefile(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cохранение')
        self.setGeometry(10, 10, 640, 480)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Cохранение", "",
                                                  "Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            if '.txt' in fileName:
                self.filename = fileName
            else:
                self.filename = fileName + '.txt'
        else:
            print(None)
            self.filename = None


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_GenPass.clicked.connect(self.btnGenPass)
        self.ui.pushButton_SaveFile_Pass.clicked.connect(self.btnSaveFile_Pass)
        self.ui.pushButton_Shifr.clicked.connect(self.btnShifr)
        self.ui.pushButton_DeShifr.clicked.connect(self.btnDeShifr)
        self.ui.pushButton_SaveFile_Shifr.clicked.connect(self.btnSaveFile_Shifr)
        self.ui.comboBox_shifrLang.addItems(['rus', 'en'])
        self.ui.comboBox_PassType.addItems(['Да', 'Нет'])

    def btnChange(self):
        self.ui.pushButton_GenPass.clicked.connect(self.btnGenPass)
        self.ui.pushButton_SaveFile_Pass.clicked.connect(self.btnSaveFile_Pass)
        self.ui.pushButton_Shifr.clicked.connect(self.btnShifr)
        self.ui.pushButton_DeShifr.clicked.connect(self.btnDeShifr)
        self.ui.pushButton_SaveFile_Shifr.clicked.connect(self.btnSaveFile_Shifr)

    def btnGenPass(self):
        # print(self.ui.spinBox.value())
        PassType = False
        if self.ui.comboBox_PassType.currentText() == 'Да':
            PassType = True
        passlist = genpassword(self.ui.spinBox.value(), PassType)
        self.ui.textEdit_PassList.setText(passlist)
        self.ui.pushButton_SaveFile_Pass.setEnabled(True)

    def btnSaveFile_Pass(self):
        if self.ui.textEdit_PassList.toPlainText() == '':
            error('Пароли не сгенерированны!')
        else:
            self.savefile_window = mywindow_savefile()
            if self.savefile_window.filename:
                with open(self.savefile_window.filename, 'w') as file:
                    file.write('{}'.format(self.ui.textEdit_PassList.toPlainText()))

    def btnShifr(self):
        if self.ui.lineEdit_Key.text() == '' or self.ui.textEdit_Text.toPlainText() == '':
            error('Данные не заполнены!')
        else:
            print(self.ui.comboBox_shifrLang.currentText())
            print(self.ui.lineEdit_Key.text()[:1])
            text = self.ui.textEdit_Text.toPlainText().lower()
            key = self.ui.lineEdit_Key.text().lower()
            if self.ui.comboBox_shifrLang.currentText() == 'en':
                if cheaktext(text, tabula_recta_en) and cheaktext(key, tabula_recta_en):
                    code = encrypt(key, text, tabula_recta_en)
                    self.ui.textEdit_Shifr.setText(code)
                    self.ui.pushButton_SaveFile_Shifr.setEnabled(True)
                else:
                    error('Неверно выбран язык!')
            elif self.ui.comboBox_shifrLang.currentText() == 'rus':
                if cheaktext(text, tabula_recta_rus) and cheaktext(key, tabula_recta_rus):
                    code = encrypt(key, text, tabula_recta_rus)
                    self.ui.textEdit_Shifr.setText(code)
                    self.ui.pushButton_SaveFile_Shifr.setEnabled(True)
                else:
                    error('Неверно выбран язык!')


    def btnDeShifr(self):
        if self.ui.lineEdit_Key.text() == '' or self.ui.textEdit_Text.toPlainText() == '':
            error('Данные не заполнены!')
        else:
            print(self.ui.lineEdit_Key.text()[:1])
            text = self.ui.textEdit_Text.toPlainText().lower()
            key = self.ui.lineEdit_Key.text().lower()
            if self.ui.comboBox_shifrLang.currentText() == 'en':
                if cheaktext(text, tabula_recta_en) and cheaktext(key, tabula_recta_en):
                    code = decrypt(key, text, tabula_recta_en)
                    self.ui.textEdit_Shifr.setText(code)
                    self.ui.pushButton_SaveFile_Shifr.setEnabled(True)
                else:
                    error('Неверно выбран язык!')
            elif self.ui.comboBox_shifrLang.currentText() == 'rus':
                if cheaktext(text, tabula_recta_rus) and cheaktext(key, tabula_recta_rus):
                    code = decrypt(key, text, tabula_recta_rus)
                    self.ui.textEdit_Shifr.setText(code)
                    self.ui.pushButton_SaveFile_Shifr.setEnabled(True)
                else:
                    error('Неверно выбран язык!')

    def btnSaveFile_Shifr(self):
        if self.ui.textEdit_PassList.toPlainText() == '':
            error('Шифр не сгенерирован!')
        else:
            self.savefile_window = mywindow_savefile()
            if self.savefile_window.filename:
                with open(self.savefile_window.filename, 'w') as file:
                    file.write('{}'.format(self.ui.textEdit_Shifr.toPlainText()))


tabula_recta_en = 'abcdefghijklmnopqrstuvwxyz'
tabula_recta_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def cheaktext(text, tabula):
    for index, char in enumerate(text):
        if char != ' ':
            if not char in tabula:
                return False
    return True


def encrypt(key, text, tabula_recta):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            mj = tabula_recta.index(ch)
            kj = tabula_recta.index(key[(index - space) % len(key)])
            cj = (mj + kj) % len(tabula_recta)
            result.append(tabula_recta[cj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)


def decrypt(key, text, tabula_recta):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            cj = tabula_recta.index(ch)
            kj = tabula_recta.index(key[(index - space) % len(key)])
            mj = (cj - kj) % len(tabula_recta)
            result.append(tabula_recta[mj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)


def genpassword(symbol_count, type):
    def gen_one_password():
        Pass_Symbol = []
        spec_cymbol = "!\"#$%&'()*+,-.:;<=>?"
        symbol = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        if type:
            Pass_Symbol.extend(list(spec_cymbol + symbol))
        else:
            Pass_Symbol.extend(list(symbol))
        psw = ''.join([random.choice(Pass_Symbol) for x in range(int(symbol_count))])
        return str(psw)

    alltext = ''
    for i in range(10):
        text = gen_one_password()
        print(text)
        alltext += text + '\n'

    return alltext



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
