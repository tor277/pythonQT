from PySide6 import QtWidgets

from a_login_form import Window as LoginWidget
from b_ship_parameters import Window as ShipParametersWidget
from c_engine_settings import Window as EngineSettingsWidget
from d_profile_card import Window as ProfileCardWidget

DEBUG = True


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.loginWidget = LoginWidget()
        self.shipParametersWidget = ShipParametersWidget()
        self.engineSettingsWidget = EngineSettingsWidget()
        self.profileCardWidget = ProfileCardWidget()

        l_left = QtWidgets.QVBoxLayout()
        l_left.addWidget(self.loginWidget)
        l_left.addWidget(self.profileCardWidget)
        l_left.addWidget(self.shipParametersWidget)
        l_left.addSpacerItem(QtWidgets.QSpacerItem(
            0, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        ))

        l_main = QtWidgets.QHBoxLayout()
        l_main.addLayout(l_left)
        l_main.addWidget(self.engineSettingsWidget)

        self.setLayout(l_main)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
