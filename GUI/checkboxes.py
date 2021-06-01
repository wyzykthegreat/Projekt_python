from PyQt5.QtWidgets import QCheckBox, QFormLayout, QGroupBox
from GUI.graph import get_countries, GraphWidget
from Backend.config import Singleton, FILENAME_NEW_CASES


class Cbx(QCheckBox):
    def __init__(self, parent, name):
        super().__init__(name)
        self.__cbx_list = list()
        self.parent = parent

    def _make_list(self): # dodac guzik co odznacza wszystko # %fixme
        size = get_countries(FILENAME_NEW_CASES)
        cbx_layout = QFormLayout()
        self.__cbx_group = QGroupBox("Countries")

        for i in range(len(size[1:])):
            name = "{}".format(size[i + 1])
            cbx = Cbx(self.parent, name)
            self.__cbx_list.append(cbx)
            cbx_layout.addRow(cbx)
            cbx.clicked.connect(self.func_to(cbx.text()))

        self.__cbx_group.setLayout(cbx_layout)
        return self.__cbx_group

    def func_to(self, name):

        return lambda _: self.raz(name)

    def raz(self, name):
        parameters = Singleton.get_instance()
        if name in parameters.countries:
            parameters.countries.remove(name)
            self.__update_graph()
        else:
            parameters.countries.append(name)
            self.__update_graph()
        print(parameters.countries)
        print(parameters)

    def __update_graph(self):
        plot = GraphWidget(self.parent, "Ozdrowieni")
        plot.update_graph()
