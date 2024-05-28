"""
Разработать приложение для мониторинга нагрузки системы и системных процессов (аналог диспетчера задач).

Обязательные функции в приложении:

Показ общих сведений о системе (в текстовом виде!):
Название процессора, количество ядер, текущая загрузка
Общий объём оперативной памяти, текущая загрузка оперативаной памяти
Количество, жестких дисков + информация по каждому (общий/занятый объём)
Обеспечить динамический выбор обновления информации (1, 5, 10, 30 сек.)
Показ работающих процессов
Показ работающих служб
Показ задач, которые запускаются с помощью планировщика задач
"""

from PySide6 import QtWidgets, QtCore
import psutil, platform


class TaskManagerApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Системный информер")
        self.resize(250, 700)

        self.processor_label = QtWidgets.QLabel()
        self.memory_label = QtWidgets.QLabel()
        self.disk_label = QtWidgets.QLabel()
        self.disks_info_list = QtWidgets.QListWidget()
        self.processes_list = QtWidgets.QListWidget()
        self.services_list = QtWidgets.QListWidget()
        self.disks_info_list.setMaximumHeight(70)
        self.scheduler_tasks_list = QtWidgets.QListWidget()

        self.interval_map = {
            1: 1000,  # 1 секунда
            5: 5000,  # 5 секунд
            10: 10000,  # 10 секунд
            30: 30000  # 30 секунд
        }

        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update_info)
        self.update_timer.start(1000)  # Обновление информации каждую секунду

        self.interval_combobox = QtWidgets.QComboBox()
        self.interval_combobox.addItems(['1 сек', '5 сек', '10 сек', '30 сек'])
        self.interval_combobox.currentIndexChanged.connect(self.update_interval)

        self.l = QtWidgets.QVBoxLayout()
        self.l.addWidget(self.interval_combobox)
        self.l.addWidget(self.processor_label)
        self.l.addWidget(self.memory_label)
        self.l.addWidget(self.disk_label)
        self.l.addWidget(self.disks_info_list)
        self.l.addWidget(QtWidgets.QLabel("Работающие процессы:"))
        self.l.addWidget(self.processes_list)
        self.l.addWidget(QtWidgets.QLabel("Запущенные сервисы:"))
        self.l.addWidget(self.services_list)
        self.l.addWidget(QtWidgets.QLabel("Запланированные задачи:"))
        self.l.addWidget(self.scheduler_tasks_list)

        self.setLayout(self.l)

        self.update_info()

    def update_info(self):
        cpu_percent = psutil.cpu_percent()
        cpu_info = platform.processor()
        cpu_cores = psutil.cpu_count(logical=False)
        ram_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        processes = psutil.process_iter()

        self.processor_label.setText(f"Процессор: {cpu_info}\n Количество Ядер: {cpu_cores}\n Загрузка CPU: {cpu_percent}%")
        self.memory_label.setText(f"Используется ОЗУ: {ram_info.percent}%\n Объем ОЗУ: {round(ram_info.total / 1024 ** 3, 2)} GB")
        self.disk_label.setText(f"Занято на диске: {disk_info.percent}%")
        self.processes_list.clear()
        self.services_list.clear()
        self.scheduler_tasks_list.clear()
        self.disks_info_list.clear()

        for process in processes:
            self.processes_list.addItem(process.name())

        for service in psutil.win_service_iter():
            self.services_list.addItem(service.display_name())

        for service in psutil.win_service_iter():
            if service.display_name() == 'Tasks':
                tasks = service.tasks()
                for task in tasks:
                    self.scheduler_tasks_list.addItem(task)
        if not any(service.display_name() == 'Tasks' for service in psutil.win_service_iter()):
            self.scheduler_tasks_list.addItem("Планы отсуствуют")

        for partition in psutil.disk_partitions():
            disk_info = psutil.disk_usage(partition.mountpoint)
            self.disks_info_list.addItem(f"Диски: {partition.device}\n "
                                         f"({partition.mountpoint}): \n Общий объем - {round(disk_info.total / 1024**3, 2)}\n"
                                         f" Занято - {round(disk_info.used / 1024**3, 2)} GB")

    def update_interval(self, index):
        interval_text = self.interval_combobox.currentText()
        interval_seconds = int(interval_text.split()[0])
        self.update_timer.setInterval(self.interval_map[interval_seconds])

if __name__ == '__main__':

    app = QtWidgets.QApplication()

    task_manager_app = TaskManagerApp()
    task_manager_app.show()
    app.exec()