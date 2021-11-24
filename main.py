from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 200)  
        # Смещение от левого верхнего угла на 300 вправо, 250 вниз и характеристики: ширина 350, высота 200

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)  # Смещение от левого верхнего угла программы на 100 вправо и 100 вниз
        self.main_text.adjustSize()  # Авторасстягивание объекта, если тот не влезает в свои параметры

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100,50)
        self.new_text.adjustSize()




def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show() # Показываем окно
    sys.exit(app.exec()) # Закрываем окно

if __name__ == "__main__":
    application()