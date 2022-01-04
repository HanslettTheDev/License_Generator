# access command line arguments
import sys
sys.setrecursionlimit(2000)
import random

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from PyQt5.QtCore import (Qt, QPoint, QSize)

from PyQt5 import QtCore, QtGui, QtWidgets


class GenWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 343)
        self.license_box = QtWidgets.QLineEdit(Form)
        self.license_box.setGeometry(QtCore.QRect(20, 120, 351, 41))
        self.license_box.setObjectName("license_box")
        self.license_box.setStyleSheet(
            "font-size: 20px;\n"
        )
        self.generate_btn = QtWidgets.QPushButton(Form)
        self.generate_btn.setGeometry(QtCore.QRect(140, 190, 101, 41))
        self.generate_btn.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgb(5, 13, 25); \n"
"border-bottom: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #F8485E;\n"
"}")
        self.generate_btn.setObjectName("generate_btn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 321, 51))
        self.label.setStyleSheet("font-weight: bold;\n"
"font-size: 20px;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 260, 101, 51))
        self.label_2.setStyleSheet("font-weight: bold;\n"
"font-size: 20px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.license_strength = QtWidgets.QLabel(Form)
        self.license_strength.setGeometry(QtCore.QRect(140, 270, 81, 31))
        self.license_strength.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.license_strength.setText("")
        self.license_strength.setObjectName("license_strength")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ECU license Generator"))
        self.generate_btn.setText(_translate("Form", "Generate"))
        self.label.setText(_translate("Form", "ECU ProTech License Generator"))
        self.label_2.setText(_translate("Form", "Strength:"))


class GeneratorWindow(QMainWindow, GenWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = GenWindow()
        self.ui.setupUi(self)
        self.show()

        # add generate function
        self.ui.generate_btn.clicked.connect(self.generate)

    def verify(self, key):
        global score 
        score = 0

        check_digit = key[2] # check digit key
        check_digit_2 = key[8]
        count_1 = 0 # check digit count
        count_2 = 0

        # get the chunks by using the split method and use a for loop to check the digit
        chunks = key.split("-")
        print(chunks)
        for chunk in chunks:
            if len(chunk) != 5:
                return False
            
            for char in chunk:
                if char == check_digit:
                    count_1 += 1
                if char == check_digit_2:
                    count_2 += 1
                score += ord(char) # convert each char to a score 
        
        # rules
        if score > 2200 and score < 2300 and count_1 == 4 and count_2 == 2:
            return True
        else:
            return False   
                  
    def generate(self):
        # clear the text edit
        self.ui.license_box.setText("")
        # default credentials
        key = ""
        section = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"

        # Key = aaaaa-bbbbb-ccccc-ddddd-12345 or 25 char
        while len(key) < 30:
            # Randomly pick from the alphabet variable
            char = random.choice(alphabet) # add the random choice to the key
            key += char # add the random choice to the section
            section += char # Add in the dashes and hyphens
            if len(section) == 5:
                key += '-' # add a hyphen
                section = "" # reset the section variable
        # get the key but remove the last digit
        key = key[:-1]  
        

        # verify the key
        if self.verify(key):
            # key is verified and output to the screen
            self.ui.license_box.setText(key)
            self.ui.license_strength.setText("{score}".format(score=score))
        else: 
            self.generate()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GeneratorWindow()
    sys.exit(app.exec_())