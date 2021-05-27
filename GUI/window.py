from PyQt5.QtWidgets import QMainWindow
from GUI.tabs import TabsWidget

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyton-19")

        self.__tabs_widget = TabsWidget()
        self.setCentralWidget(self.__tabs_widget)
        self.show()

