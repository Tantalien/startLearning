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
x = 0
number = random.randint(1, 100)
print(number)


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('rainbow.png'))
        self.setWindowTitle('***amazing rainbow***')
        self.lineEdit.setPlaceholderText('Введите число')
        self.pushButton.clicked.connect(self.variable)

    def variable(self):
        global x
        z = self.lineEdit.text()  # создала переменную, вводимую через lineEdit
        x = z
        print(x)

    def enter(self):
        global a
        global b
        global c
        global i
        global x
        global number

        while True:
            if number == x:
                self.label_2.setText('Угадал! Ты умничка')
            if number - i < x < number + i:
                self.label_2.setText('Огонь!')
            elif number - a < x < number + a:
                self.label_2.setText('Очень горячо')
            elif number - b < x < number + b:
                self.label_2.setText('Горячо, но не сильно')
            elif number - c < x < number + c:
                self.label_2.setText('Холодно')
            elif number > 100 or x < 1:
                self.label_2.setText('Диапазон загаданного числа от 1 до 100')
            else:
                self.label_2.setText('Лёд!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()
