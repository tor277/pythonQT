"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets
from PySide6.QtCore import QSettings, QEvent, Qt
from PySide6.QtGui import QKeyEvent

from ui.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.settings = QSettings("MyComp", "MyApp")

        self.ui.dial.valueChanged.connect(self.sync_all)
        self.ui.horizontalSlider.valueChanged.connect(self.sync_all)

        self.ui.comboBox.currentIndexChanged.connect(self.change_display_mode)

        self.init_keybord_handling()

        self.ui.comboBox.addItems(["dec", "bin", "oct", "hex"])

        self.saving_settings()

    def init_keybord_handling(self):
        self.ui.dial.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.ui.dial and event.type() == QEvent.KeyPress:
            if event.text() == "+":
                self.ui.dial.setValue(self.ui.dial.value() + 1)
                print(f"Значение = {self.ui.dial.value()}")
                return True
            elif event.text() == "-":
                self.ui.dial.setValue(self.ui.dial.value() - 1)
                print(f"Значение ={self.ui.dial.value()}")
                return True
        return super(Window, self).eventFilter(obj, event)


    def sync_all(self, value):
        sender = self.sender()
        if sender == self.ui.dial or sender == self.ui.horizontalSlider:
            self.ui.horizontalSlider.setValue(value)
            self.ui.dial.setValue(value)
            self.update_lcd_number(value)

    def update_lcd_number(self, value):
        mode = self.ui.comboBox.currentText().lower()
        if mode == 'dec':
            self.ui.lcdNumber.display(value)
        elif mode == 'bin':
            self.ui.lcdNumber.display(bin(value)[2:])
        elif mode == 'oct':
            self.ui.lcdNumber.display(oct(value)[2:])
        elif mode == 'hex':
            self.ui.lcdNumber.display(hex(value)[2:])

    def change_display_mode(self):
        self.update_lcd_number(self.ui.dial.value())

    def saving_settings(self):
        if self.settings.contains("display_mode"):
            mode = self.settings.value("display_mode")
            index = self.ui.comboBox.findText(mode)
            if index != -1:
                self.ui.comboBox.setCurrentIndex(index)
        if self.settings.contains("lcd_value"):
            value = int(self.settings.value("lcd_value"))
            self.ui.dial.setValue(value)
            self.ui.horizontalSlider.setValue(value)
            self.update_lcd_number(value)

    def closeEvent(self, event):
        self.settings.setValue("display_mode", self.ui.comboBox.currentText())
        self.settings.setValue("lcd_value", self.ui.dial.value())
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
