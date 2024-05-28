"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from a_threads import SystemInfo

class SystemInfoWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Информация о системе")
        self.resize(350, 500)

        self.system_info = SystemInfo()
        self.system_info.systemInfoReceived.connect(self.updateSystemInfo)

        self.lineEditDelay = QtWidgets.QLineEdit()
        self.lineEditDelay.setPlaceholderText("Введите время задержки")
        self.textEditCPU = QtWidgets.QTextEdit()
        self.textEditRAM = QtWidgets.QTextEdit()

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.lineEditDelay)
        l.addWidget(self.textEditCPU)
        l.addWidget(self.textEditRAM)

        self.setLayout(l)

        self.system_info.start()

        self.lineEditDelay.textChanged.connect(self.changeDelay)

    def updateSystemInfo(self, info):
        cpu_value, ram_value = info
        self.textEditCPU.setText(f"Загрузка CPU: {cpu_value}%")
        self.textEditRAM.setText(f"Использование RAM: {ram_value}%")

    def changeDelay(self):
        delay = int(self.lineEditDelay.text()) if self.lineEditDelay.text() else 1
        self.system_info.delay = delay

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    widget = SystemInfoWidget()
    widget.show()
    app.exec()