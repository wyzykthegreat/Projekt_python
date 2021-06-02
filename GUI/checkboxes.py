from PyQt5.QtWidgets import QCheckBox
from GUI.graph import GraphWidget
from Backend.config import Singleton


class Cbx(QCheckBox):
    def __init__(self, parent, name):
        super().__init__(name)
        self.__parent = parent

        self.clicked.connect(self.__func_to(self.text()))

    def __func_to(self, name):
        return lambda _: self.__on_click(name)

    def __on_click(self, name):
        data = Singleton.get_instance()
        if name in data.get_countries_list():
            data.remove_country(name)
            self.__update_graph()
        else:
            data.add_country(name)
            self.__update_graph()

    def __update_graph(self):
        plot = GraphWidget(self.__parent, "Ozdrowieni")
        plot.update_graph()

    def show(self):
        self.setVisible(True)

    def hide(self):
        self.setVisible(False)
