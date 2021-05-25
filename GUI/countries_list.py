from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import Qt
from checkboxes import Cbx
import config

config.FILENAME = None
config.COUNTRIES = []
config.START_DAY = None
config.END_DAY = None

class ListWidget(QScrollArea):
    def __init__(self):
        super().__init__()
        self.__init_view()

    def __init_view(self):
        cbx = Cbx("Countries")
        self.setWidget(cbx._make_list())
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)