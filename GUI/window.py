import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QGridLayout, QHBoxLayout
from checkboxes import ListWidget
from graph import GraphWidget
from buttons import PushButton, UpdateBtn, ReportBtn


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


class TabsWidget(QWidget):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        layout = QVBoxLayout()

        self.__tabs = QTabWidget()
        self.__tabs.setFixedSize(1550, 850)
        self.__tabs.resize(width, height)

        dane = 100

        self.__tab1 = QWidget()
        self.__tab2 = QWidget()

        self.__tabs.addTab(self.__tab1, "Zakazeni")
        self.__tabs.addTab(self.__tab2, "Ozdrowieni")

        layout_tab1 = QGridLayout()
        layout_tab1.rowCount = 10
        layout_tab1.columnCount = 10
        countries = list

        layout_tab1.addWidget(ListWidget(dane, countries), 4, 8, 1, 3)
        layout_tab1.addWidget(GraphWidget(self), 0, 0, 5, 8)
        layout_tab1.addWidget(ReportBtn(), 6, 0, 4, 2)
        layout_tab1.addWidget(UpdateBtn(), 6, 8, 4, 2)

        self.__tab1.setLayout(layout_tab1)
        self.__tab2.setLayout(QGridLayout(self))

        layout.addWidget(self.__tabs)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])

    empty_view = Window()

    sys.exit(app.exec_())
