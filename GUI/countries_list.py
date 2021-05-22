from PyQt5.QtWidgets import QScrollArea, QFormLayout, QGroupBox
from PyQt5.QtCore import Qt
from checkboxes import Cbx

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