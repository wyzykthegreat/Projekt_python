from PyQt5.QtWidgets import QWidget, QSlider, QVBoxLayout
from PyQt5 import QtCore
from Backend.config import Singleton
import datetime


class DoubleSlider(QWidget):
    def __init__(self, min_width=150):
        super().__init__()
        data = Singleton.get_instance()
        start_value = 0
        end_value = data.n_of_days
        self.__start_value = start_value
        self.__end_value = end_value
        self.__min_width = min_width

        self.__slider1 = self.__prepare_slider1()
        self.__slider2 = self.__prepare_slider2()

        self.__prepare_layout()

    def __prepare_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.__slider1)
        layout.addWidget(self.__slider2)

        self.setLayout(layout)

    def __prepare_slider(self, init_value):
        slider = QSlider(QtCore.Qt.Horizontal)
        slider.setMinimum(self.__start_value)
        slider.setMaximum(self.__end_value)
        slider.setMinimumWidth(self.__min_width)
        slider.setValue(init_value)

        return slider

    def __prepare_slider1(self):
        slider = self.__prepare_slider(self.__start_value)
        slider.valueChanged.connect(self.__on_change_slider1)
        return slider

    def __prepare_slider2(self):
        slider = self.__prepare_slider(self.__end_value)
        slider.valueChanged.connect(self.__on_change_slider2)
        return slider

    def __on_change_slider1(self):
        data = Singleton.get_instance()

        data.print_data()

        start_value = self.__slider1.value()
        end_value = self.__slider2.value()

        self.__update_singleton_date_range()

        if start_value > end_value:
            self.__slider1.setValue(end_value)

    def __on_change_slider2(self):
        data = Singleton.get_instance()

        data.print_data()

        start_value = self.__slider1.value()
        end_value = self.__slider2.value()

        self.__update_singleton_date_range()

        if end_value < start_value:
            self.__slider2.setValue(start_value)

    def __update_singleton_date_range(self):
        singleton = Singleton.get_instance()

        start_value = self.__slider1.value()
        end_value = self.__slider2.value()

        start_date = singleton.start_day
        end_date = singleton.end_day

        start_date_new = start_date + datetime.timedelta(days = start_value)
        end_date_new = end_date - datetime.timedelta(days = singleton.n_of_days - end_value)

        print(start_date_new)
        print(end_date_new)
        print(singleton.n_of_days)


        singleton.set_date_range(start_date_new, end_date_new)
