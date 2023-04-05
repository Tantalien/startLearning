import random
import sys
from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

Form, _ = uic.loadUiType('Play.ui')

# глобальные переменные
a = 5  # variable very hot
b = 10  # variable hot
c = 20  # variable cold
i = 2  # fire
number = random.randint(1, 100)


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('rainbow.png'))
        self.setWindowTitle('***amazing rainbow***')
        self.lineEdit.setPlaceholderText('Введите число')
        #self.pushButton.clicked.connect(self.enter)
        self.pushButton.clicked.connect(self.variable)

    def variable (self):                              # создала переменную, вводимую через lineEdit
        z = self.lineEdit.text()
        #self.label_2.setText(self.lineEdit.text())
        print(z)
        #попробовать эту функцию объединить с enter, чтобы она видела z. Или создать наследуемый класс


'''
    def enter(self):
        global a
        global b
        global c
        global i
        global number
        z =  
        #q = self.label_2.setText(self.lineEdit.text()) не верно

        while True:
            #q = int(input('Угадай число (от 1 до 100):'))    #пока не понимаю, как сделать, чтобы q была связана с lineEdit
            if number == q:
                self.label_2.setText('Угадал! Ты умничка')
            if number - i < q < number + i:
                self.label_2.setText('Огонь!')
            elif number - a < q < number + a:
                self.label_2.setText('Очень горячо')
            elif number - b < q < number + b:
                self.label_2.setText('Горячо, но не сильно')
            elif number - c < q < number + c:
                self.label_2.setText('Холодно')
            elif guess > 100 or q < 1:
                self.label_2.setText('Диапазон загаданного числа от 1 до 100')
            else:
                self.label_2.setText('Лёд!')
       '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()

