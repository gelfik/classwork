# from PyQt5 import QtWidgets, uic
# import sys
#
# app = QtWidgets.QApplication([])
# win = uic.loadUi("untitled.ui")  # расположение вашего файла .ui
#
# win.show()
# sys.exit(app.exec())
import random

import PyQt5
from PyQt5 import QtWidgets
from design import Ui_MainWindow  # импорт нашего сгенерированного файла
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QTableWidgetItem
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
        self.user = admin

        self.ui.pushButton_GenPass.clicked.connect(self.btnGenPass)
        self.ui.pushButton_SaveFile_Pass.clicked.connect(self.btnSaveFile_Pass)
        self.ui.pushButton_Shifr.clicked.connect(self.btnShifr)
        self.ui.pushButton_DeShifr.clicked.connect(self.btnDeShifr)
        self.ui.pushButton_SaveFile_Shifr.clicked.connect(self.btnSaveFile_Shifr)

        self.ui.lineEdit_Fraza.textChanged.connect(self.updateAllTwoChange)
        self.ui.lineEdit_Poradak_Stolb.textChanged.connect(self.updatePoradak_Stolb)
        self.ui.lineEdit_Poradak_Strok.textChanged.connect(self.updatePoradak_Strok)

        self.ui.checkBox_FilePravEdit_Ban.clicked.connect(lambda: self.btnCheckBox_StatusChange('ban'))
        self.ui.checkBox_FilePravEdit_Write.clicked.connect(lambda: self.btnCheckBox_StatusChange('write'))
        self.ui.checkBox_FilePravEdit_Read.clicked.connect(lambda: self.btnCheckBox_StatusChange('read'))
        self.ui.checkBox_FilePravEdit_Full.clicked.connect(lambda: self.btnCheckBox_StatusChange('full'))
        self.ui.checkBox_FilePravEdit_SendPrav.clicked.connect(lambda: self.btnCheckBox_StatusChange('sendprav'))

        self.ui.comboBox_UserInf_User.view().pressed.connect(self.updateSelectUser)
        self.ui.comboBox_ChangePrav_User.view().pressed.connect(self.updatePravSelectUser)
        self.ui.comboBox_ChangePrav_Type.view().pressed.connect(self.updatePravUser)
        self.ui.comboBox_FileLook_File.view().pressed.connect(self.updateListPrav)
        self.ui.comboBox_FilePravEdit_File.view().pressed.connect(self.updateSelectPravChangeFile)
        self.ui.comboBox_FilePravEdit_User.view().pressed.connect(self.updateSelectPravChangeUser)

        self.ui.label_FileLook_Ban.setText(get_YesNo(self.user.file1.ban))
        self.ui.label_FileLook_Write.setText(get_YesNo(self.user.file1.write))
        self.ui.label_FileLook_Read.setText(get_YesNo(self.user.file1.read))
        self.ui.label_FileLook_Full.setText(get_YesNo(self.user.file1.full))
        self.ui.label_FileLook_SendPrav.setText(get_YesNo(self.user.file1.sendprav))

        self.ui.comboBox_FilePravEdit_File.clear()
        if self.user.file1.sendprav or self.user.file1.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File1')
        if self.user.file2.sendprav or self.user.file1.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File2')
        if self.user.file3.sendprav or self.user.file1.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File3')
        if self.user.file4.sendprav or self.user.file1.full:
            self.ui.comboBox_FilePravEdit_File.addItem('File4')

        self.ui.comboBox_FilePravEdit_User.setCurrentIndex(0)
        self.ui.comboBox_FilePravEdit_File.setCurrentIndex(0)
        filename = self.ui.comboBox_FilePravEdit_File.currentText()
        user = self.ui.comboBox_FilePravEdit_User.currentText()
        self.change_LookPravFile(self.get_FileName(user, filename))

        # self.ui.lineEdit_Fraza.setInputMask('XXXXXXXXXXXXXXXXXXXXXXXXX')
        self.ui.lineEdit_Poradak_Stolb.setInputMask('99999')
        self.ui.lineEdit_Poradak_Strok.setInputMask('99999')

        self.updateTableUserPrav()

        self.ui.tableWidget_Osn.setColumnWidth(0,20)
        self.ui.tableWidget_Osn.setColumnWidth(1, 20)
        self.ui.tableWidget_Osn.setColumnWidth(2, 20)
        self.ui.tableWidget_Osn.setColumnWidth(3, 20)
        self.ui.tableWidget_Osn.setColumnWidth(4, 20)

        self.ui.tableWidget_Stolb.setColumnWidth(0, 20)
        self.ui.tableWidget_Stolb.setColumnWidth(1, 20)
        self.ui.tableWidget_Stolb.setColumnWidth(2, 20)
        self.ui.tableWidget_Stolb.setColumnWidth(3, 20)
        self.ui.tableWidget_Stolb.setColumnWidth(4, 20)

        self.ui.tableWidget_Strok.setColumnWidth(0, 20)
        self.ui.tableWidget_Strok.setColumnWidth(1, 20)
        self.ui.tableWidget_Strok.setColumnWidth(2, 20)
        self.ui.tableWidget_Strok.setColumnWidth(3, 20)
        self.ui.tableWidget_Strok.setColumnWidth(4, 20)

    def updatePoradak_Stolb(self):
        poradok_text_stolb = self.ui.lineEdit_Poradak_Stolb.text()
        if len(poradok_text_stolb) == 5:
            symbol_list = ['6', '7', '8', '9', '0']
            status = True
            for i, text in enumerate(symbol_list):
                if not poradok_text_stolb.find(text) == -1:
                    status = False
            if status:
                self.updateAllTwoChange()
            else:
                self.ui.lineEdit_Poradak_Stolb.setText('12345')
                error('Введите числа для задания порадка в диапазоне от 1 до 5!')
        else:
            self.ui.lineEdit_Poradak_Stolb.setText('12345')
            error('Заполните порядок столбцов!')

    def updatePoradak_Strok(self):
        poradok_text_stolb = self.ui.lineEdit_Poradak_Stolb.text()
        poradok_text_line = self.ui.lineEdit_Poradak_Strok.text()
        if len(poradok_text_line) == 5:
            symbol_list = ['6', '7', '8', '9', '0']
            status = True
            for i, text in enumerate(symbol_list):
                if not poradok_text_line.find(text) == -1:
                    status = False
            if status:
                self.updateAllTwoChange()
            else:
                self.ui.lineEdit_Poradak_Strok.setText('12345')
                error('Введите числа для задания порадка в диапазоне от 1 до 5!')
        else:
            self.ui.lineEdit_Poradak_Strok.setText('12345')
            error('Заполните порядок строк!')

    def updateAllTwoChange(self):
        poradok_text_stolb = self.ui.lineEdit_Poradak_Stolb.text()
        poradok_text_line = self.ui.lineEdit_Poradak_Strok.text()
        old_text = self.ui.lineEdit_Fraza.text().ljust(25, " ")
        twochange.list_text = []
        for i in range(5):
            twochange.list_text.append(old_text[i * 5:i * 5 + 5])

        for i, text in enumerate(twochange.list_text):
            j = 0
            for j in range(5):
                self.ui.tableWidget_Osn.setItem(i, j, QTableWidgetItem(text[j:j+1]))
                j += 1

        twochange.list_stolb = []
        for i, text in enumerate(twochange.list_text):
            new_text = ''
            for j in range(5):
                count = int(poradok_text_stolb[j:j+1])
                new_text += text[count - 1:count]
            twochange.list_stolb.append(new_text)
        for i, text in enumerate(twochange.list_stolb):
            for j in range(5):
                self.ui.tableWidget_Stolb.setItem(i, j, QTableWidgetItem(text[j:j+1]))
                j += 1

        twochange.list_line = ['', '', '', '', '']
        for i in range(5):
            stroka_text = ''
            count = int(poradok_text_line[i:i+1])
            for j, text in enumerate(twochange.list_stolb):
                stroka_text += text[count - 1:count]
            twochange.list_line[i] = stroka_text

        for i, text in enumerate(twochange.list_line):
            for j in range(5):
                self.ui.tableWidget_Strok.setItem(i, j, QTableWidgetItem(text[j:j+1]))
                j += 1

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
        self.ui.comboBox_UserInf_User.setCurrentIndex(item)
        self.user = self.get_UserName(self.ui.comboBox_UserInf_User.currentText())

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
        # item = self.ui.comboBox_ChangePrav_User.model().itemFromIndex(index).row()
        # if item == 0:
        #     self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(user1))
        # elif item == 1:
        #     self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(user2))
        # elif item == 2:
        #     self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(user3))
        # elif item == 3:
        #     self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(user4))

        item = self.ui.comboBox_ChangePrav_User.model().itemFromIndex(index).row()
        self.ui.comboBox_ChangePrav_User.setCurrentIndex(item)
        self.ui.comboBox_ChangePrav_Type.setCurrentIndex(get_UserPrav(self.get_UserName(self.ui.comboBox_ChangePrav_User.currentText())))

    def updatePravUser(self, index):
        def update_UserPrav(user, type):
            if type == 0:
                user.pravchange = True
            else:
                user.pravchange = False

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

    def btnCheckBox_StatusChange(self, param):
        def cheakPravForFile(file):
            if not file.ban and not file.full and not file.read and not file.write and not file.sendprav:
                file.ban = True
                self.ui.checkBox_FilePravEdit_Ban.setChecked(True)
                file.write = False
                self.ui.checkBox_FilePravEdit_Write.setChecked(False)
                file.read = False
                self.ui.checkBox_FilePravEdit_Read.setChecked(False)
                file.sendprav = False
                self.ui.checkBox_FilePravEdit_SendPrav.setChecked(False)
                file.full = False
                self.ui.checkBox_FilePravEdit_Full.setChecked(False)

        def get_PravStatusUser(file, param):
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

        file = self.get_FileName(self.ui.comboBox_FilePravEdit_User.currentText(),
                                 self.ui.comboBox_FilePravEdit_File.currentText())

        status = get_PravStatusUser(file, param)

        if param == 'ban':
            if status:
                self.change_PravFile(file, False, True, True, True, True)
            else:
                self.change_PravFile(file, True, False, False, False, False)
        elif param == 'full':
            if status:
                self.change_PravFile(file, False, None, None, None, False)
            else:
                self.change_PravFile(file, False, True, True, True, True)
        elif param == 'write':
            if status:
                self.change_PravFile(file, False, False, None, None, None)
            else:
                self.change_PravFile(file, False, True, None, None, None)
        elif param == 'read':
            if status:
                self.change_PravFile(file, False, None, False, None, None)
            else:
                self.change_PravFile(file, False, None, True, None, None)
        elif param == 'sendprav':
            if status:
                self.change_PravFile(file, False, None, None, False, None)
            else:
                self.change_PravFile(file, False, None, None, True, None)
        cheakPravForFile(file)
        self.change_LookPicFile(self.user, self.ui.comboBox_FileLook_File.currentText())
        self.updateTableUserPrav()

    # def cheakPravForFile(self, file):
    #     if not file.ban and not file.full and not file.read and not file.write and not file.sendprav:
    #         file.ban = True
    #         self.ui.checkBox_FilePravEdit_Ban.setChecked(True)
    #         file.write = False
    #         self.ui.checkBox_FilePravEdit_Write.setChecked(False)
    #         file.read = False
    #         self.ui.checkBox_FilePravEdit_Read.setChecked(False)
    #         file.sendprav = False
    #         self.ui.checkBox_FilePravEdit_SendPrav.setChecked(False)
    #         file.full = False
    #         self.ui.checkBox_FilePravEdit_Full.setChecked(False)

    def get_UserPravText(self, file):
        text = ''
        if file.ban:
            text = 'Полный запрет'
        elif file.full:
            text = 'Полный доступ'
        else:
            if file.read:
                text += 'Чтение'
            if file.write:
                if text != '':
                    text += ', '
                text += 'Запись'
            if file.sendprav:
                if text != '':
                    text += ', '
                text += 'Передача прав'

        if text == '':
            return 'Нет прав!'
        return text

    def updateTableUserPrav(self):
        i = 0
        userlist = [admin, user1, user2, user3, user4]
        for user in userlist:
            j = 0
            filelist = [user.file1, user.file2, user.file3, user.file4]
            for file in filelist:
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(self.get_UserPravText(file)))
                j += 1
            i += 1

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

    def change_PravFile(self, user, ban, write, read, sendprav, full):
        if ban is not None:
            user.ban = ban
            self.ui.checkBox_FilePravEdit_Ban.setChecked(ban)
        if write is not None:
            user.write = write
            self.ui.checkBox_FilePravEdit_Write.setChecked(write)
        if read is not None:
            user.read = read
            self.ui.checkBox_FilePravEdit_Read.setChecked(read)
        if sendprav is not None:
            user.sendprav = sendprav
            self.ui.checkBox_FilePravEdit_SendPrav.setChecked(sendprav)
        if full is not None:
            user.full = full
            self.ui.checkBox_FilePravEdit_Full.setChecked(full)


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

class TwoChange():
    def __init__(self):
        list_stolb = []
        list_line = []

class User():
    def __init__(self, user, pravchange, file1, file2, file3, file4):
        self.user = user
        self.pravchange = pravchange
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3
        self.file4 = file4


class File():
    def __init__(self, filename, ban, write, read, sendprav, full):
        self.filename = filename
        self.ban = ban
        self.write = write
        self.read = read
        self.sendprav = sendprav
        self.full = full

twochange = TwoChange()

admin = User('Admin', True, File('File1', False, True, True, True, True), File('File2', False, True, True, True, True),
             File('File3', False, True, True, True, True), File('File4', False, True, True, True, True))

user1 = User('User1', True, File('File1', False, True, True, True, True), File('File2', False, False, True, False, False),
             File('File3', False, True, True, True, False), File('File4', False, True, True, False, False))
user2 = User('User2', False, File('File1', False, True, False, False, False), File('File2', False, True, True, True, True),
             File('File3', False, False, True, False, False), File('File4', False, False, False, True, False))
user3 = User('User3', False, File('File1', False, True, False, False, False),
             File('File2', False, True, True, True, False),
             File('File3', False, True, True, True, True), File('File4', False, True, True, False, False))
user4 = User('User4', False, File('File1', False, True, True, True, False),
             File('File2', False, True, True, False, False),
             File('File3', False, True, True, False, False), File('File4', False, True, True, True, True))

print(admin.file1.filename)
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
