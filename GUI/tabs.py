from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QGridLayout
from GUI.countries_list import ListWidget
from GUI.graph import GraphWidget
from GUI.buttons import UpdateBtn, ReportBtn
from Backend.config import Singleton
from GUI.slider import DoubleSlider


class TabsWidget(QWidget):

    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        self.tabs = QTabWidget()
        self.tabs.setFixedSize(520, 430)

        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1, "Zakazeni")
        self.tabs.addTab(self.tab2, "Ozdrowieni")

        data = Singleton()
        print(data)
        graph1 = GraphWidget(self, "Zakazeni")
        graph2 = GraphWidget(self, "Ozdrowieni")
        double_slider1 = DoubleSlider(self)

        self.layout_tab1 = QGridLayout()
        self.layout_tab1.addWidget(graph1, 0, 0, 3, 3)

        self.layout_tab2 = QGridLayout()
        self.layout_tab2.addWidget(graph2, 0, 0)

        self.tab1.setLayout(self.layout_tab1)
        self.tab2.setLayout(self.layout_tab2)

        layout.addWidget(self.tabs)
        layout.addWidget(ListWidget(self), 0, 3, 3, 1)
        layout.addWidget(double_slider1, 3, 3, -1, -1)
        layout.addWidget(ReportBtn(), 3, 0, -1, 1)

        self.setLayout(layout)
        self.show()

    def get_selected_tab(self):
        return self.tabs.currentIndex()
