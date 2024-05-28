from PySide6 import QtWidgets

from b_systeminfo_widget import SystemInfoWidget as SystemInfoWidget
from c_weatherapi_widget import WindowWeather as WindowWeather


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.SystemInfoWidget = SystemInfoWidget()
        self.WindowWeather = WindowWeather()


        l_main = QtWidgets.QHBoxLayout()
        l_main.addWidget(self.SystemInfoWidget)
        l_main.addWidget(self.WindowWeather)

        self.setLayout(l_main)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
