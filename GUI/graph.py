import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import datetime
from Backend.config import Singleton, FILENAME_RECOVERED, FILENAME_NEW_CASES


class GraphWidget(FigureCanvas):
    def __init__(self, parent, type: str):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        super().__init__(self.fig)
        self.type = type
        self.parent = parent
        self.plot_graph()

    def plot_graph(self):
        parameters = Singleton.get_instance()  # przywołanie naszego Singletona
        filepath = FILENAME_NEW_CASES if self.type == "Zakazeni" else FILENAME_RECOVERED
        countries_list = parameters.countries
        self.display_data(read_countries_data(filepath, countries_list), self.type)

    def display_data(self, n_of_patients_in_countries,
                     type: str):  # tutaj bedzie trzeba zrobic zakres dat forze # fixme
        parameters = Singleton.get_instance()
        for country, data in n_of_patients_in_countries.items():
            self.ax.semilogy(data, label=country)
        drawing(type, parameters.date_range[0])

    def update_graph(self):
        plot = GraphWidget(self.parent, self.type)
        if self.type == "Zakazeni":
            self.parent.layout_tab1.addWidget(plot, 0, 0)
            self.parent.setLayout(self.parent.layout_tab1)
        else:
            self.parent.layout_tab2.addWidget(plot, 0, 0)
            self.parent.setLayout(self.parent.layout_tab2)
        self.parent.show()


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
