import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QGridLayout, QCheckBox, QLabel, QScrollArea, \
    QFormLayout, QGroupBox
from PyQt5.QtCore import Qt


class ListWidget(QScrollArea):
    def __init__(self, size, countries):
        super().__init__()
        self.__init_view(size, countries)

    def __init_view(self, size, countries):  # size to bedzie lista krajow
        cbx_layout = QFormLayout()
        cbx_group = QGroupBox()

        for i in range(size):  # tu bedzie for i in lista krajow
            name = "Country {}".format(i)
            cbx = Cbx(name)
            cbx_layout.addRow(cbx)
            cbx.stateChanged.connect(cbx.clicked(countries))
            # tutaj trzeba dodac co sie dzieje jak kliknie sie checkbox

        cbx_group.setLayout(cbx_layout)
        self.setWidget(cbx_group)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)


class Cbx(QCheckBox):
    def __init__(self, name):
        super().__init__(name)

    def clicked(self, cntries):
        if self.isChecked():
            cntries.append(self)
        else:
            pass
