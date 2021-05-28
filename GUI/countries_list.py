from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import Qt
from GUI.checkboxes import Cbx
from GUI.graph import GraphWidget


class ListWidget(QScrollArea):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.__init_view()

    def __init_view(self):
        cbx = Cbx(self.parent, "Countries")
        self.setWidget(cbx._make_list())
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
