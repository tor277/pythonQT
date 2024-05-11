from PySide6 import QtWidgets
from ui.book_shop import Ui_Form

from login_write import Window as LoginWidget
from c_ship_form import Window as ShipWidget
from d_engine_settings import Window as EngineWidget
from e_progile_card import Window as ProfileWidget


DEBAG = False


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.LoginWidget = LoginWidget()
        self.ShipWidget = ShipWidget()
        self.EnginWidget = EngineWidget()
        self.ProfileWidget = ProfileWidget()

        l_left = QtWidgets.QVBoxLayout()
        l_left.addWidget(self.LoginWidget)
        l_left.addWidget(self.ProfileWidget)
        l_left.addWidget(self.ShipWidget)
        l_left.addSpacerItem(QtWidgets.QSpacerItem(0, 10,
                                                   QtWidgets.QSizePolicy.Policy.Expanding,
                                                   QtWidgets.QSizePolicy.Policy.Expanding
                                                   ))

        l_main = QtWidgets.QHBoxLayout()
        l_main.addLayout(l_left)
        l_main.addWidget(self.EnginWidget)

        self.setLayout(l_main)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
