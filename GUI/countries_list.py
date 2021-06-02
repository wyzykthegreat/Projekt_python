from PyQt5.QtWidgets import QScrollArea, QFormLayout, QGroupBox, QLineEdit, QVBoxLayout, QWidget, QSpacerItem, \
    QSizePolicy
from PyQt5.QtCore import Qt
from GUI.checkboxes import Cbx
from GUI.graph import GraphWidget
from GUI.graph import get_countries
from Backend.config import FILENAME_NEW_CASES


class ListWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.__parent = parent
        self.__controls = QWidget()
        self.__controls_layout = QVBoxLayout()
        self.__cbx_group = self.__make_list()
        self.__searchbar = QLineEdit()
        self.__scroll = QScrollArea()


        self.__init_view()
        self.__searchbar.textChanged.connect(self.__update_display)

    def __update_display(self, text):
        for country in self.__cbx_group:
            if text.lower() in country.text().lower():
                country.setVisible(True)
            else:
                country.setVisible(False)


    def __init_view(self):
        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.__controls_layout.addItem(spacer)
        self.__controls.setLayout(self.__controls_layout)


        layout = QVBoxLayout()
        layout.addWidget(self.__searchbar)
        self.__scroll.setWidget(self.__controls)
        self.__scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.__scroll.setWidgetResizable(True)
        layout.addWidget(self.__scroll)
        self.setLayout(layout)


    def __make_list(self):
        size = get_countries(FILENAME_NEW_CASES)
        self.__cbx_group = list()

        for i in range(len(size[1:])):
            name = "{}".format(size[i + 1])
            cbx = Cbx(self.__parent, name)
            self.__controls_layout.addWidget(cbx)
            self.__cbx_group.append(cbx)


        return self.__cbx_group