from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QGridLayout, QCheckBox, QLabel, QScrollArea, \
    QFormLayout, QGroupBox, QPushButton
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from Backend.config import Singleton, FILENAME_RECOVERED, FILENAME_NEW_CASES


class GraphWidget(FigureCanvas):
    def __init__(self, parent, type: str):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        super().__init__(fig)
        self.setParent(parent)
        self.type = type
        self.update_graph()


    def update_graph(self):
        data2 = Singleton.get_instance()
        filepath = FILENAME_NEW_CASES if self.type == "Zakazeni" else FILENAME_RECOVERED
        countries_list = data2.countries
        display_data(read_countries_data(filepath, countries_list))


def read_countries_data(filepath, countries):
    countries_list = []
    countries_data = {}

    with open(filepath, "r") as f:
        for line in f:
            maybe_country = line.split(",")[1]

            if maybe_country in countries:
                line = line.strip()
                n_of_patients_in_time = get_patients_as_vector(line)

                countries_data[maybe_country] = n_of_patients_in_time

    return countries_data

def get_countries(filepath):
    countries_list = []

    with open(filepath, "r") as f:
        for line in f:
            if line.split(",")[1] not in countries_list:
                countries_list.append(line.split(",")[1])

    return countries_list

def get_patients_as_vector(country_data_line):
    n_of_unimportant_column = 4
    n_of_patients_in_time = country_data_line.split(",")[n_of_unimportant_column:]
    n_of_patients_in_time = [int(val) for val in n_of_patients_in_time]

    return n_of_patients_in_time

def drawing():
    plt.xlabel("Days (subsequent data)")
    plt.ylabel("Total number of patients")
    plt.title("Covid-19 number of patients since 01.01.2020")
    plt.grid()
    plt.legend()
    plt.show()
    return 0

def display_data(n_of_patients_in_countries):
    for country, data in n_of_patients_in_countries.items():
        plt.semilogy(data, label=country)

    drawing()
