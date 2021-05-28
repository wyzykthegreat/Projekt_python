from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QGridLayout, QCheckBox, QLabel, QScrollArea, \
    QFormLayout, QGroupBox, QPushButton
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import datetime
from Backend.config import Singleton, FILENAME_RECOVERED, FILENAME_NEW_CASES


class GraphWidget(FigureCanvas):
    def __init__(self, parent, type: str):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        super().__init__(self.fig)
        self.setParent(parent)
        self.type = type
        self.update_graph()


    def update_graph(self):
        parameters = Singleton.get_instance() #przywołanie naszego Singletona
        filepath = FILENAME_NEW_CASES if self.type == "Zakazeni" else FILENAME_RECOVERED
        countries_list = parameters.countries
        display_data(read_countries_data(filepath, countries_list), self.type)


def read_countries_data(filepath, countries):
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

def drawing(type: str, start_date: datetime):
    plt.xlabel(f"Dni od {start_date}")
    if type == "Zakazeni":
        plt.ylabel("Liczba zakażeń")
        plt.title("Całkowita liczba zakażeń COVID-19")
    elif type == "Ozdrowieni":
        plt.ylabel("Liczba ozdrowień")
        plt.title("Całkowita liczba ozdrowień COVID-19")
    plt.grid()
    plt.legend()
    plt.show()
    return 0

def display_data(n_of_patients_in_countries, type: str):
    parameters = Singleton.get_instance()
    for country, data in n_of_patients_in_countries.items():
        plt.semilogy(data, label=country)

    drawing(type, parameters.date_range[0])
