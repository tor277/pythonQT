from PySide6 import QtWidgets
from ui.c_ship import Ui_Form


DEBAG = False

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Параметры корабля")



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
