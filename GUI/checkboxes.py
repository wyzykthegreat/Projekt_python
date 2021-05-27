import sys

from PyQt5.QtWidgets import QCheckBox, QFormLayout, QGroupBox

import Backend.config as config
from GUI.graph import get_countries, GraphWidget
from Backend.config import Singleton, FILENAME_NEW_CASES



class Cbx(QCheckBox):
    def __init__(self, name):
        super().__init__(name)
        self.__cbx_list = list()

    def _make_list(self, data):
        size = get_countries(FILENAME_NEW_CASES)
        cbx_layout = QFormLayout()
        self.__cbx_group = QGroupBox("Countries")

        for i in range(len(size[1:])):
            name = "{}".format(size[i + 1])
            cbx = Cbx(name)
            self.__cbx_list.append(cbx)
            cbx_layout.addRow(cbx)
            cbx.clicked.connect(self.func_to(cbx.text(), data))

        self.__cbx_group.setLayout(cbx_layout)
        return self.__cbx_group

    def func_to(self, name, data):

        return lambda _: self.raz(name, data)

    def raz(self, name, data: Singleton):
        if name in data.countries:
            data.countries.remove(name)
        else:
            data.countries.append(name)


        print(data.countries)
