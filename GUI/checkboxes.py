import sys

from PyQt5.QtWidgets import QCheckBox, QFormLayout, QGroupBox

import Backend.config as config
from GUI.graph import get_countries, GraphWidget
from Backend.config import Singleton, FILENAME_NEW_CASES



class Cbx(QCheckBox):
    def __init__(self, name):
        super().__init__(name)
        self.__cbx_list = list()

    def _make_list(self, graph: GraphWidget):
        size = get_countries(FILENAME_NEW_CASES)
        cbx_layout = QFormLayout()
        self.__cbx_group = QGroupBox("Countries")

        for i in range(len(size[1:])):
            name = "{}".format(size[i + 1])
            cbx = Cbx(name)
            self.__cbx_list.append(cbx)
            cbx_layout.addRow(cbx)
            cbx.clicked.connect(self.func_to(cbx.text(), graph))

        self.__cbx_group.setLayout(cbx_layout)
        return self.__cbx_group

    def func_to(self, name, graph: GraphWidget):

        return lambda _: self.raz(name, graph)

    def raz(self, name, graph: GraphWidget):
        data1 = Singleton.get_instance()
        if name in data1.countries:
            data1.countries.remove(name)
        else:
            data1.countries.append(name)

        graph.update_graph()
        print(data1.countries)
        print (data1)
