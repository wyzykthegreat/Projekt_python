from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QGridLayout
from GUI.graph import GraphWidget


class TabsWidget(QTabWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(520, 430)

        self.__tab1 = QWidget()
        self.__tab2 = QWidget()

        self.addTab(self.__tab1, "Zakazeni")
        self.addTab(self.__tab2, "Ozdrowieni")

        graph1 = GraphWidget(self, "Zakazeni")
        graph2 = GraphWidget(self, "Ozdrowieni")

        self.__layout_tab1 = QGridLayout()
        self.__layout_tab1.addWidget(graph1)

        self.__layout_tab2 = QGridLayout()
        self.__layout_tab2.addWidget(graph2)

        self.__tab1.setLayout(self.__layout_tab1)
        self.__tab2.setLayout(self.__layout_tab2)

    def update_graphs(self, plot1, plot2):
        self.__layout_tab1.addWidget(plot1, 0, 0, 3, 3)
        self.__layout_tab2.addWidget(plot2, 0, 0, 3, 3)

        self.__tab1.setLayout(self.__layout_tab1)
        self.__tab2.setLayout(self.__layout_tab2)

        self.show()
