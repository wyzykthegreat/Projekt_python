from PyQt5.QtWidgets import QWidget, QSlider, QVBoxLayout
from PyQt5 import QtCore
from Backend.config import Singleton
import datetime

class DoubleSlider(QWidget):
    def __init__(self, start_date, end_date, min_width=150):
        super().__init__()
        self.__start_date = start_date
        self.__end_date = end_date
        self.__min_width = min_width

        self.__slider1 = self.__prepare_slider1()
        self.__slider2 = self.__prepare_slider2()

        self.__prepare_layout()

    def __prepare_slider(self, init_value):
        slider = QSlider(QtCore.Qt.Horizontal)
        slider.setMinimum(self.__start_date)
        slider.setMaximum(self.__end_date)
        slider.setMinimumWidth(self.__min_width)
        slider.setValue(init_value)

        return slider

    def __prepare_slider1(self):
        slider = self.__prepare_slider(self.__start_date)
        slider.valueChanged.connect(self.__on_change_slider1)
        return slider

    def __prepare_slider2(self):
        slider = self.__prepare_slider(self.__end_date)
        slider.valueChanged.connect(self.__on_change_slider2)
        return slider

    def __on_change_slider1(self):
        data = Singleton.get_instance()

        data.print_data()

        start_date = self.__slider1.value()
        end_date = self.__slider2.value()

        data.set_date_range(start_date, end_date)

        if start_date > end_date:
            self.__slider1.setValue(end_date)

    def __on_change_slider2(self):
        data = Singleton.get_instance()

        data.print_data()

        start_date = self.__slider1.value()
        end_date = self.__slider2.value()

        data.set_date_range(start_date, end_date)

        if end_date < start_date:
            self.__slider2.setValue(start_date)

    def __prepare_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.__slider1)
        layout.addWidget(self.__slider2)

        self.setLayout(layout)