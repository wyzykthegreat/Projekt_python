from PyQt5.QtWidgets import QCheckBox, QLineEdit
from GUI.graph import get_countries, GraphWidget
from Backend.config import Singleton, FILENAME_NEW_CASES


class Cbx(QCheckBox):
    def __init__(self, parent, name):
        super().__init__(name)
        self.__parent = parent

        self.clicked.connect(self.__func_to(self.text()))

    def __func_to(self, name):
        return lambda _: self.__on_click(name)

    def __on_click(self, name):
        parameters = Singleton.get_instance()
        if name in parameters.countries:
            parameters.countries.remove(name)
            self.__update_graph()
        else:
            parameters.countries.append(name)
            self.__update_graph()

    def __update_graph(self):
        plot = GraphWidget(self.__parent, "Ozdrowieni")
        plot.update_graph()

    def show(self):
        self.setVisible(True)

    def hide(self):
        self.setVisible(False)
