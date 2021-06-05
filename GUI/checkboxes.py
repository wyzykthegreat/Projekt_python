from PyQt5.QtWidgets import QCheckBox, QMessageBox
from GUI.graph import GraphWidget
from Backend.config import Singleton
from Backend.exceptions import UnableToAddMoreCountriesToGraph


class Cbx(QCheckBox):
    def __init__(self, parent, name):
        super().__init__(name)
        self.__parent = parent

        self.clicked.connect(self.__func_to())

    def __func_to(self):
        return lambda _: self.__on_click()

    def __on_click(self):
        data = Singleton.get_instance()
        name = self.text()
        try:
            if name in data.get_countries_list():
                data.remove_country(name)
                self.__update_graph()
            else:
                if len(data.get_countries_list()) > 5:
                    self.setChecked(False)
                    raise UnableToAddMoreCountriesToGraph()
                else:
                    data.add_country(name)
                self.__update_graph()

        except UnableToAddMoreCountriesToGraph as err:
            msg = QMessageBox()
            msg.setWindowTitle("Caught error")
            msg.setText(f"{err}")
            msg.exec_()

    def __update_graph(self):
        plot = GraphWidget(self.__parent, "Ozdrowieni")
        plot.update_graph()

    def show(self):
        self.setVisible(True)

    def hide(self):
        self.setVisible(False)
