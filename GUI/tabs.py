from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QGridLayout
from GUI.countries_list import ListWidget
from GUI.graph import GraphWidget
from GUI.buttons import UpdateBtn, ReportBtn
from Backend.config import Singleton

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

        data = Singleton()
        print(data)
        graph1 = GraphWidget(self, "Zakazeni")
        graph2 = GraphWidget(self, "Ozdrowieni")


        layout_tab1 = QGridLayout()
        layout_tab1.addWidget(ListWidget(graph1), 0, 3)
        layout_tab1.addWidget(graph1, 0, 0)
        layout_tab1.addWidget(ReportBtn(), 3, 0)
        #layout_tab1.addWidget(update_btn, 3, 3)

        layout_tab2 = QGridLayout()
        #layout_tab2.addWidget(ListWidget(), 0, 3)
        #layout_tab2.addWidget(graph2, 0, 0)
        #layout_tab2.addWidget(ReportBtn(), 3, 0)
        #layout_tab2.addWidget(update_btn, 3, 3)

        self.__tab1.setLayout(layout_tab1)
        self.__tab2.setLayout(layout_tab2)

        layout.addWidget(self.__tabs)
        self.setLayout(layout)


    def get_selected_tab(self):
        return self.__tabs.currentIndex()
