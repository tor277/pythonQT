"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)


3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets
from PySide6.QtCore import QDateTime
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit

from ui.c_signals_events import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()



    def initSignals(self) -> None:

        self.ui.pushButtonLT.clicked.connect(self.move_left_up)
        self.ui.pushButtonRT.clicked.connect(self.move_right_up)
        self.ui.pushButtonLB.clicked.connect(self.move_left_down)
        self.ui.pushButtonRB.clicked.connect(self.move_right_down)
        self.ui.pushButtonCenter.clicked.connect(self.move_center)
        self.ui.pushButtonMoveCoords.clicked.connect(self.move_to_coords)
        self.ui.pushButtonGetData.clicked.connect(self.get_data)


    def move_left_up(self):
        self.move_window(-10, -10)

    def move_right_up(self):
        self.move_window(10, -10)

    def move_left_down(self):
        self.move_window(-10, 10)

    def move_right_down(self):
        self.move_window(10, 10)

    def move_center(self):
        screen_size = QApplication.primaryScreen().geometry()
        screen_center = screen_size.center()
        window_size = self.frameGeometry()
        window_size.moveCenter(screen_center)
        self.move(window_size.topLeft())

    def move_to_coords(self):
        x = self.ui.spinBoxX.value()
        y = self.ui.spinBoxY.value()
        self.move(x, y)

    def move_window(self, dx, dy):
        current_x = self.x()
        current_y = self.y()

        new_x = current_x + dx
        new_y = current_y +dy

        self.move(new_x, new_y)

    def get_data(self):

        screen = QGuiApplication.primaryScreen()
        screen_num = QGuiApplication.screens()
        screen_size = screen.size()
        current_screen = QGuiApplication.screenAt(self.mapToGlobal(self.pos()))
        if current_screen:
            current_screen_name = current_screen.name()
        else:
            current_screen_name = "Не удалось определить экран"

        window_size = self.size()
        min_window_size = self.minimumSize()
        window_position = self.pos()
        center = QGuiApplication.primaryScreen().geometry().center()
        window_state = self.windowState()
        state_info = ""
        if self.isMaximized():
            state_info = "Окно развернуто на весь экран"
        elif self.isMinimized():
            state_info = "Окно свернуто"
        else:
            state_info = "Окно в нормальном состоянии"


        info = (f'Кол-во экранов: {len(screen_num)}\n '
                                           f'Текущий основной экран: {screen}\n'
                                           f'Разрешение экрана: {screen_size.width()} x {screen_size.height()}\n'
                                           f'На каком экране окно находится: {current_screen_name}\n'
                                           f'Размеры окна: {window_size.width()} x {window_size.height()}\n'
                                           f'Минимальные размеры окна: {min_window_size.width()} x {min_window_size.height()}\n'
                                           f'Текущее положение (координаты) окна: {window_position.y()} x {window_position.x()}\n'
                                           f'Координаты центра приложения: {center.toTuple()}\n'
                                           f'Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено): {state_info}\n')
        self.ui.plainTextEdit.setPlainText(info)

    def moveEvent(self, event):
        old_pos = event.oldPos()
        new_pos = event.pos()
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")

        print(
            f"{current_time} - Перемещение окна: Старая позиция - ({old_pos.x()}, {old_pos.y()}), Новая позиция - ({new_pos.x()}, {new_pos.y()})")

    def resizeEvent(self, event):
        new_size = event.size()
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")

        print(f"{current_time} - Изменение размера окна: Новый размер - ({new_size.width()}, {new_size.height()})")

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
