from PySide6 import QtWidgets
from ui.login import Ui_Form


DEBAG = False

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEditLogin.setPlaceholderText("Введите логин")
        self.ui.lineEditPassword.setPlaceholderText("Введите пароль")

        if DEBAG:
            self.ui.lineEditLogin.setText("Логин")
            self.ui.lineEditPassword.setText("Пароль")



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
