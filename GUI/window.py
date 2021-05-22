import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from tabs import TabsWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        width, height = 1600, 900
        self.setFixedSize(width, height)
        self.setWindowTitle("Python-19")
        self.__tabs_widget = TabsWidget(self, width, height)
        layout = QHBoxLayout()
        self.__tabs_widget.setLayout(layout)
        self.show()


if __name__ == "__main__":
    app = QApplication([])

    empty_view = Window()

    sys.exit(app.exec_())
