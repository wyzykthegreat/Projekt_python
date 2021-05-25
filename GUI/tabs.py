from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QGridLayout
from GUI.countries_list import ListWidget
from GUI.graph import GraphWidget
from GUI.buttons import UpdateBtn, ReportBtn

class TabsWidget(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.__tabs = QTabWidget()
        self.__tabs.resize(1500, 800)

        self.__tab1 = QWidget()
        self.__tab2 = QWidget()

        self.__tabs.addTab(self.__tab1, "Zakazeni")
        self.__tabs.addTab(self.__tab2, "Ozdrowieni")

        layout_tab1 = QGridLayout()
        layout_tab1.addWidget(ListWidget(), 0, 3)
        layout_tab1.addWidget(GraphWidget(self), 0, 0)
        layout_tab1.addWidget(ReportBtn(), 3, 0)

        self.__tab1.setLayout(layout_tab1)
        self.__tab2.setLayout(QVBoxLayout(self))

        layout.addWidget(self.__tabs)
        self.setLayout(layout)