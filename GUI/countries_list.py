from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import Qt
from GUI.checkboxes import Cbx
from GUI.graph import GraphWidget


class ListWidget(QScrollArea):
    def __init__(self, graph: GraphWidget):
        super().__init__()
        self.__init_view(graph)

    def __init_view(self, graph: GraphWidget):
        cbx = Cbx("Countries")
        self.setWidget(cbx._make_list(graph))
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)