from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget
from GUI.tabs import TabsWidget
from GUI.countries_list import ListWidget
from GUI.slider import DoubleSlider
from GUI.buttons import ReportBtn, UncheckBtn


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyton-19")
        self.setFixedSize(790, 570)
        layout = QGridLayout()

        central_widget = QWidget()

        tabs_widget = TabsWidget()

        double_slider = DoubleSlider(tabs_widget)
        list_widget = ListWidget(tabs_widget)
        report_btn = ReportBtn(tabs_widget, "PDF")
        uncheck_btn = UncheckBtn(tabs_widget, list_widget, "Clear graph")

        layout.addWidget(tabs_widget, 0, 0, 2, 2)
        layout.addWidget(list_widget, 0, 3, 3, 1)
        layout.addWidget(double_slider, 3, 3, -1, -1)
        layout.addWidget(report_btn, 3, 0, -1, 1)
        layout.addWidget(uncheck_btn, 3, 1, -1, 1)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
        self.show()
