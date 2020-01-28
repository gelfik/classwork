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
    msg.setWindowTitle("Info")
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
        self.ui.label_UserInf_Status.setText(get_YesNo(admin.pravchange))

        self.ui.pushButton_GenPass.clicked.connect(self.btnGenPass)
        self.ui.pushButton_SaveFile_Pass.clicked.connect(self.btnSaveFile_Pass)
        self.ui.pushButton_Shifr.clicked.connect(self.btnShifr)
        self.ui.pushButton_DeShifr.clicked.connect(self.btnDeShifr)
        self.ui.pushButton_SaveFile_Shifr.clicked.connect(self.btnSaveFile_Shifr)

        self.ui.checkBox_FilePravEdit_Ban.clicked.connect(self.btnCheckBox_StatusChange)
        self.ui.checkBox_FilePravEdit_Write.clicked.connect(self.btnCheckBox_StatusChange)
        self.ui.checkBox_FilePravEdit_Read.clicked.connect(self.btnCheckBox_StatusChange)
        self.ui.checkBox_FilePravEdit_Full.clicked.connect(self.btnCheckBox_StatusChange)
        self.ui.checkBox_FilePravEdit_SendPrav.clicked.connect(self.btnCheckBox_StatusChange)

        self.ui.comboBox_UserInf_User.view().pressed.connect(self.updateSelectUser)
        self.ui.comboBox_ChangePrav_User.view().pressed.connect(self.updatePravSelectUser)
        self.ui.comboBox_ChangePrav_Type.view().pressed.connect(self.updatePravUser)
        self.ui.comboBox_FileLook_File.view().pressed.connect(self.updateListPrav)
        self.ui.comboBox_FilePravEdit_File.view().pressed.connect(self.updateSelectPravChangeFile)
        self.ui.comboBox_FilePravEdit_User.view().pressed.connect(self.updateSelectPravChangeUser)

        self.user = admin
        self.ui.label_FileLook_Ban.setText(get_YesNo(self.user.file1.ban))
        self.ui.label_FileLook_Write.setText(get_YesNo(self.user.file1.write))
        self.ui.label_FileLook_Read.setText(get_YesNo(self.user.file1.read))
        self.ui.label_FileLook_Full.setText(get_YesNo(self.user.file1.full))
        self.ui.label_FileLook_SendPrav.setText(get_YesNo(self.user.file1.sendprav))

        self.ui.comboBox_FilePravEdit_File.clear()
        if self.user.file1.sendprav:
            self.ui.comboBox_FilePravEdit_File.addItem('File1')
        if self.user.file2.sendprav:
            self.ui.comboBox_FilePravEdit_File.addItem('File2')
        if self.user.file3.sendprav:
            self.ui.comboBox_FilePravEdit_File.addItem('File3')
        if self.user.file4.sendprav:
            self.ui.comboBox_FilePravEdit_File.addItem('File4')

        self.ui.comboBox_FilePravEdit_User.setCurrentIndex(0)
        self.ui.comboBox_FilePravEdit_File.setCurrentIndex(0)
        filename = self.ui.comboBox_FilePravEdit_File.currentText()
        user = self.ui.comboBox_FilePravEdit_User.currentText()
        self.change_LookPravFile(self.get_FileName(user, filename))

    def updateSelectPravChangeFile(self, index):
        item = self.ui.comboBox_FilePravEdit_File.model().itemFromIndex(index).row()
        self.ui.comboBox_FilePravEdit_File.setCurrentIndex(item)
        filename = self.ui.comboBox_FilePravEdit_File.currentText()
        user = self.ui.comboBox_FilePravEdit_User.currentText()
        self.change_LookPravFile(self.get_FileName(user, filename))

    def updateSelectPravChangeUser(self, index):
        self.ui.comboBox_FilePravEdit_File.clear()
        if self.user.file1.sendprav or self.user.file1.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File1')
        if self.user.file2.sendprav or self.user.file2.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File2')
        if self.user.file3.sendprav or self.user.file3.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File3')
        if self.user.file4.sendprav or self.user.file4.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File4')
        item = self.ui.comboBox_FilePravEdit_User.model().itemFromIndex(index).row()
        self.ui.comboBox_FilePravEdit_User.setCurrentIndex(item)
        filename = self.ui.comboBox_FilePravEdit_File.currentText()
        user = self.ui.comboBox_FilePravEdit_User.currentText()
        self.change_LookPravFile(self.get_FileName(user, filename))

    def updateSelectUser(self, index):
        item = self.ui.comboBox_UserInf_User.model().itemFromIndex(index).row()
        if item == 0:
            self.user = admin
        elif item == 1:
            self.user = user1
        elif item == 2:
            self.user = user2
        elif item == 3:
            self.user = user3
        elif item == 4:
            self.user = user4

        self.ui.comboBox_FileLook_File.setCurrentIndex(0)
        self.ui.label_FileLook_Ban.setText(get_YesNo(self.user.file1.ban))
        self.ui.label_FileLook_Write.setText(get_YesNo(self.user.file1.write))
        self.ui.label_FileLook_Read.setText(get_YesNo(self.user.file1.read))
        self.ui.label_FileLook_Full.setText(get_YesNo(self.user.file1.full))
        self.ui.label_FileLook_SendPrav.setText(get_YesNo(self.user.file1.sendprav))

        self.ui.comboBox_FilePravEdit_User.setCurrentIndex(0)
        self.ui.comboBox_FilePravEdit_File.setCurrentIndex(0)

        if self.user.pravchange == True:
            self.ui.groupBox_ChangePrav.setVisible(True)
            self.ui.comboBox_ChangePrav_User.setCurrentIndex(0)
            self.ui.label_UserInf_Status.setText(get_YesNo(self.user.pravchange))
            self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(user1))
        else:
            self.ui.groupBox_ChangePrav.setVisible(False)
            self.ui.label_UserInf_Status.setText(get_YesNo(self.user.pravchange))

        self.ui.comboBox_FilePravEdit_File.setEnabled(True)
        self.ui.comboBox_FilePravEdit_User.setEnabled(True)

        self.ui.checkBox_FilePravEdit_Ban.setEnabled(True)
        self.ui.checkBox_FilePravEdit_Write.setEnabled(True)
        self.ui.checkBox_FilePravEdit_Read.setEnabled(True)
        self.ui.checkBox_FilePravEdit_Full.setEnabled(True)
        self.ui.checkBox_FilePravEdit_SendPrav.setEnabled(True)
        self.ui.comboBox_FilePravEdit_File.clear()
        if self.user.file1.sendprav or self.user.file1.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File1')
        if self.user.file2.sendprav or self.user.file2.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File2')
        if self.user.file3.sendprav or self.user.file3.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File3')
        if self.user.file4.sendprav or self.user.file4.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File4')

        if self.ui.comboBox_FilePravEdit_File.currentText() and self.ui.comboBox_FilePravEdit_User.currentText():
            filename = self.ui.comboBox_FilePravEdit_File.currentText()
            user = self.ui.comboBox_FilePravEdit_User.currentText()
            self.change_LookPravFile(self.get_FileName(user, filename))
        else:
            self.ui.comboBox_FilePravEdit_File.setEnabled(False)
            self.ui.comboBox_FilePravEdit_User.setEnabled(False)
            self.ui.checkBox_FilePravEdit_Ban.setEnabled(False)
            self.ui.checkBox_FilePravEdit_Write.setEnabled(False)
            self.ui.checkBox_FilePravEdit_Read.setEnabled(False)
            self.ui.checkBox_FilePravEdit_Full.setEnabled(False)
            self.ui.checkBox_FilePravEdit_SendPrav.setEnabled(False)

    def updatePravSelectUser(self, index):
        item = self.ui.comboBox_ChangePrav_User.model().itemFromIndex(index).row()
        if item == 0:
            self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(user1))
        elif item == 1:
            self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(user2))
        elif item == 2:
            self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(user3))
        elif item == 3:
            self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(user4))

    def updatePravUser(self, index):
        user = self.ui.comboBox_ChangePrav_User.currentText()
        item = self.ui.comboBox_ChangePrav_Type.model().itemFromIndex(index).row()
        if self.user.pravchange == True:
            update_UserPrav(self.get_UserName(user), item)
            self.ui.comboBox_ChangePrav_Type.setCurrentIndex(item)
            if self.user.user == user:
                self.ui.label_UserInf_Status.setText(get_YesNo(self.user.pravchange))
                self.ui.groupBox_ChangePrav.setVisible(False)
            error(f'Права пользователя {user} на редактирование прав других пользователей изменены!')
        else:
            error(f'Вы не можете изменять права!')

    def updateListPrav(self, index):
        item = self.ui.comboBox_FileLook_File.model().itemFromIndex(index).row()
        self.ui.comboBox_FileLook_File.setCurrentIndex(item)
        file = self.get_FileName(self.user, self.ui.comboBox_FileLook_File.currentText())
        self.ui.label_FileLook_Ban.setText(get_YesNo(file.ban))
        self.ui.label_FileLook_Write.setText(get_YesNo(file.write))
        self.ui.label_FileLook_Read.setText(get_YesNo(file.read))
        self.ui.label_FileLook_Full.setText(get_YesNo(file.full))
        self.ui.label_FileLook_SendPrav.setText(get_YesNo(file.sendprav))

    def btnCheckBox_StatusChange(self):
        ban = self.ui.checkBox_FilePravEdit_Ban.isChecked()
        write = self.ui.checkBox_FilePravEdit_Write.isChecked()
        read = self.ui.checkBox_FilePravEdit_Read.isChecked()
        full = self.ui.checkBox_FilePravEdit_Full.isChecked()
        sendprav = self.ui.checkBox_FilePravEdit_SendPrav.isChecked()
        filename = self.ui.comboBox_FilePravEdit_File.currentText()
        user = self.ui.comboBox_FilePravEdit_User.currentText()
        file = self.get_FileName(user, filename)

        ban_status = self.get_PravStatusUser(file, 'ban')
        write_status = self.get_PravStatusUser(file, 'write')
        read_status = self.get_PravStatusUser(file, 'read')
        full_status = self.get_PravStatusUser(file, 'full')
        sendprav_status = self.get_PravStatusUser(file, 'sendprav')
        user_dostup_filename = self.get_FileName(self.user, filename)

        if not full_status and ban:
            self.change_PravFile(file, False, True, True, True, True)
            self.change_LookPicFile(self.user, self.ui.comboBox_FileLook_File.currentText())
        elif not ban_status and full:
            self.change_PravFile(file, True, False, False, False, False)
            self.change_LookPicFile(self.user, self.ui.comboBox_FileLook_File.currentText())


        # if ban:
        #     self.ui.checkBox_FilePravEdit_Write.setChecked(False)
        #     self.ui.checkBox_FilePravEdit_Read.setChecked(False)
        #     self.ui.checkBox_FilePravEdit_Full.setChecked(False)
        #     self.ui.checkBox_FilePravEdit_SendPrav.setChecked(False)
        #     self.change_PravFile(file, True, False, False, False, False)
        #     self.change_LookPicFile(self.user, self.ui.comboBox_FileLook_File.currentText())
        #     if ban_status == ban:
        #         self.change_lookCheakBoxStatus(ban_status, write_status, read_status, full_status, sendprav_status)
        #         error(f'Не удалось изменить права на файл {filename} для пользователя {user}!')
        #     else:
        #         error(f'Полный запрет на файл {filename} для пользователя {user} УСТАНОВЛЕН!')
        # elif ban_status:
        #     self.change_PravFile(file, False, False, False, False, False)
        #     self.change_lookCheakBoxStatus(False, write_status, read_status, full_status, sendprav_status)
        #     self.change_LookPicFile(self.user, self.ui.comboBox_FileLook_File.currentText())
        #     error(f'Полный запрет на файл {filename} для пользователя {user} СНЯТ!')
        #
        # if full or read or write:
        #     self.change_PravFile(file, ban, write, read, full, sendprav)
        #     self.change_LookPicFile(self.user, self.ui.comboBox_FileLook_File.currentText())
        #     error(f'Права на файл {filename} для пользователя {user} УСТАНОВЛЕНЫ!')
        # elif full_status or read_status or write_status:
        #     self.change_PravFile(file, ban, write, read, full, sendprav)
        #     self.change_LookPicFile(self.user, self.ui.comboBox_FileLook_File.currentText())
        #     error(f'Права на файл {filename} для пользователя {user} СНЯТЫ!')
        #
        # elif sendprav:
        #     self.change_PravFile(file, ban, write, read, full, sendprav)
        #     self.change_LookPicFile(self.user, self.ui.comboBox_FileLook_File.currentText())
        #     error(f'Права на передачу прав файла {filename} для пользователя {user} УСТАНОВЛЕНЫ!')
        # elif sendprav_status:
        #     self.change_PravFile(file, ban, write, read, full, sendprav)
        #     self.change_LookPicFile(self.user, self.ui.comboBox_FileLook_File.currentText())
        #     error(f'Права на передачу прав файла {filename} для пользователя {user} СНЯТЫ!')

    def change_lookCheakBoxStatus(self, ban_status, write_status, read_status, full_status, sendprav_status):
        self.ui.checkBox_FilePravEdit_Ban.setChecked(ban_status)
        self.ui.checkBox_FilePravEdit_Write.setChecked(write_status)
        self.ui.checkBox_FilePravEdit_Read.setChecked(read_status)
        self.ui.checkBox_FilePravEdit_Full.setChecked(full_status)
        self.ui.checkBox_FilePravEdit_SendPrav.setChecked(sendprav_status)


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

    def btnSelectUser(self):
        self.ui.groupBox_ChangePrav.setVisible(False)
        self.ui.groupBox_FilePravEdit.setVisible(False)
        self.ui.groupBox_FileLook.setVisible(False)

        user = self.ui.comboBox_UserInf_User.currentText()
        print(user)
        self.user = self.get_UserName(user)

        if self.user.pravchange == True:
            self.ui.groupBox_ChangePrav.setVisible(True)
            self.ui.label_UserInf_Status.setText(get_YesNo(self.user.pravchange))
        else:
            self.ui.groupBox_ChangePrav.setVisible(False)
            self.ui.label_UserInf_Status.setText(get_YesNo(self.user.pravchange))

        self.ui.groupBox_FilePravEdit.setVisible(True)
        self.ui.groupBox_FileLook.setVisible(True)

    def get_UserName(self, user):
        if user == 'Admin':
            return admin
        elif user == 'User1':
            return user1
        elif user == 'User2':
            return user2
        elif user == 'User3':
            return user3
        elif user == 'User4':
            return user4
        else:
            return self.user

    def get_FileName(self, username, filename):
        if filename == 'File1':
            return self.get_UserName(username).file1
        elif filename == 'File2':
            return self.get_UserName(username).file2
        elif filename == 'File3':
            return self.get_UserName(username).file3
        elif filename == 'File4':
            return self.get_UserName(username).file4

    def get_PravStatusUser(self, file, param):
        if param == 'ban':
            return file.ban
        elif param == 'write':
            return file.write
        elif param == 'read':
            return file.read
        elif param == 'full':
            return file.full
        elif param == 'sendprav':
            return file.sendprav

    def change_LookPravFile(self, user):
        self.ui.checkBox_FilePravEdit_Ban.setChecked(user.ban)
        self.ui.checkBox_FilePravEdit_Write.setChecked(user.write)
        self.ui.checkBox_FilePravEdit_Read.setChecked(user.read)
        self.ui.checkBox_FilePravEdit_Full.setChecked(user.full)
        self.ui.checkBox_FilePravEdit_SendPrav.setChecked(user.sendprav)

    def change_LookPicFile(self, user, filename):
        file = self.get_FileName(user, filename)
        self.ui.label_FileLook_Ban.setText(get_YesNo(file.ban))
        self.ui.label_FileLook_Write.setText(get_YesNo(file.write))
        self.ui.label_FileLook_Read.setText(get_YesNo(file.read))
        self.ui.label_FileLook_Full.setText(get_YesNo(file.full))
        self.ui.label_FileLook_SendPrav.setText(get_YesNo(file.sendprav))

    def change_PravFile(self, user, ban, write, read, full, sendprav):
        user.ban = ban
        user.write = write
        user.read = read
        user.full = full
        user.sendprav = sendprav
        self.ui.checkBox_FilePravEdit_Ban.setChecked(ban)
        self.ui.checkBox_FilePravEdit_Write.setChecked(write)
        self.ui.checkBox_FilePravEdit_Read.setChecked(read)
        self.ui.checkBox_FilePravEdit_Full.setChecked(full)
        self.ui.checkBox_FilePravEdit_SendPrav.setChecked(sendprav)

tabula_recta_en = 'abcdefghijklmnopqrstuvwxyz'
tabula_recta_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def get_UserPrav(user):
    if user.pravchange == True:
        return 0
    else:
        return 1


def get_YesNo(param):
    if param == True:
        return 'Да'
    else:
        return 'Нет'


def update_UserPrav(user, type):
    if type == 0:
        user.pravchange = True
    else:
        user.pravchange = False


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


# class Users():
#     def __init__(self, user1):
#         self.user1 = user1
#         # , user2, user3, user4
#         # self.user2 = user2
#         # self.user3 = user3
#         # self.user4 = user4


class User():
    def __init__(self, user, pravchange, file1, file2, file3, file4):
        self.user = user
        self.pravchange = pravchange
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3
        self.file4 = file4


class File():
    def __init__(self, filename, ban, write, read, full, sendprav):
        self.filename = filename
        self.ban = ban
        self.write = write
        self.read = read
        self.full = full
        self.sendprav = sendprav


admin = User('Admin', True, File('File1', False, True, True, True, True), File('File2', False, True, True, True, True),
             File('File3', False, True, True, True, True), File('File4', False, True, True, True, True))

user1 = User('User1', True, File('File1', True, True, True, True, True), File('File2', False, False, True, True, True),
             File('File3', False, True, True, True, True), File('File4', False, True, True, True, True))
user2 = User('User2', False, File('File1', False, True, True, True, True), File('File2', False, True, True, True, True),
             File('File3', False, True, True, True, True), File('File4', False, True, True, True, True))
user3 = User('User3', False, File('File1', False, True, True, True, False), File('File2', False, True, True, True, True),
             File('File3', False, True, True, True, False), File('File4', False, True, True, True, True))
user4 = User('User4', False, File('File1', False, True, True, True, True), File('File2', False, True, True, False, False),
             File('File3', False, True, True, False, False), File('File4', False, True, True, True, True))

print(admin.file1.filename)
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
