from PySide6 import QtWidgets

DEBUG = True


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUI()

        if DEBUG:
            self.lineEditLogin.setText("ФИО")
            self.lineEditPassword.setText("Password")

    def __initUI(self):
        self.setFixedSize(350, 100)
        self.setWindowTitle("Авторизация")

        labelLogin = QtWidgets.QLabel("Логин")
        labelLogin.setMinimumWidth(70)

        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setPlaceholderText("Введите логин")

        labelPassword = QtWidgets.QLabel("Пароль")
        labelPassword.setMinimumWidth(70)

        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setPlaceholderText("Введите пароль")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.pushButtonLogin = QtWidgets.QPushButton("Войти")

        l_login = QtWidgets.QHBoxLayout()
        l_login.addWidget(labelLogin)
        l_login.addWidget(self.lineEditLogin)

        l_password = QtWidgets.QHBoxLayout()
        l_password.addWidget(labelPassword)
        l_password.addWidget(self.lineEditPassword)

        l_main = QtWidgets.QVBoxLayout()
        l_main.addLayout(l_login)
        l_main.addLayout(l_password)
        l_main.addWidget(self.pushButtonLogin)
        l_main.addSpacerItem(QtWidgets.QSpacerItem(0, 10,
                                                   QtWidgets.QSizePolicy.Policy.Expanding,
                                                   QtWidgets.QSizePolicy.Policy.Expanding
                                                   ))

        self.setLayout(l_main)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
