from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import Qt
from GUI.checkboxes import Cbx
from Backend.config import Singleton


class ListWidget(QScrollArea):
    def __init__(self, data: Singleton):
        super().__init__()
        self.__init_view(data)

    def __init_view(self, data):
        cbx = Cbx("Countries")
        self.setWidget(cbx._make_list(data))
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)