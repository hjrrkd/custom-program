import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5.QtCore import QDate
import os
import sqlite3
import cvcake

##주문자정보를받고그림그리는함수호출
path = os.path.dirname(os.path.realpath(__file__))  ##현재디렉토리경로
form_class = uic.loadUiType(path + "/info.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClick)
        
    def btnClick(self):
        self.name = str(self.name_input.toPlainText())
        self.phone = str(self.phone_input.toPlainText())
        self.require = str(self.require_input.toPlainText()) 
        
        if(self.rb1.isChecked()):
            self.hosu = "1"
        elif(self.rb2.isChecked()):
            self.hosu = "2"
        elif(self.rb3.isChecked()):
            self.hosu = "3"
        
        self.date = self.date_input.date()
        self.pick = str(self.date.year()) + "-" + str(self.date.month()) + "-" + str(self.date.day())
        ##self.date += self.date_input.month()
        ##self.date += self.date_input.day()
        
        
        if(self.name == "" or self.phone == ""):
            QMessageBox.about(self,'경고','정보를 다 입력하지 않았습니다.')
        else:
            conn = sqlite3.connect(path + "/cakeDB.db", isolation_level=None)
            c = conn.cursor()
            c.execute("INSERT INTO userTable(name, phone, size, require, pick) \
                VALUES(?,?,?,?,?)", \
                (self.name, self.phone, self.hosu, self.require, self.pick))
            ##c.execute("CREATE TABLE IF NOT EXISTS userTable \
                ##(name text, phone text)")
            ##c.execute("INSERT INTO userTable VALUES('바보', '1234')")
            print(c.fetchall())
            conn.close()
            ##케이크그리는 창 뜨기
            self.close()
            cvcake.drawcake()   ##케이크그리기
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())

    