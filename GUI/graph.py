import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import datetime
from Backend.config import Singleton, FILENAME_RECOVERED, FILENAME_NEW_CASES
from io import BytesIO


class GraphWidget(FigureCanvas):
    __IMG_FORMAT = "png"

    def __init__(self, parent, type: str):
        self.__fig, self.__ax = plt.subplots(figsize=(5, 4), dpi=100)
        super().__init__(self.__fig)
        self.__type = type
        self.__parent = parent
        self.__plot_graph()

    def __plot_graph(self):
        data = Singleton.get_instance()  # przywołanie naszego Singletona
        filepath = FILENAME_NEW_CASES if self.__type == "Zakazeni" else FILENAME_RECOVERED
        countries_list = data.get_countries_list()
        self.display_data(read_countries_data(filepath, countries_list), self.__type)

    def display_data(self, n_of_patients_in_countries, type: str):
        singleton = Singleton.get_instance()
        for country, data in n_of_patients_in_countries.items():
            self.__ax.semilogy(data, label=country)
        drawing(type, singleton.get_date_range()[0])

    def update_graph(self):
        plot1 = GraphWidget(self.__parent, "Zakazeni")
        plot2 = GraphWidget(self.__parent, "Ozdrowieni")

        self.__parent.layout_tab1.addWidget(plot1, 0, 0, 3, 3)
        self.__parent.layout_tab2.addWidget(plot2, 0, 0, 3, 3)

        self.__parent.tab1.setLayout(self.__parent.layout_tab1)
        self.__parent.tab2.setLayout(self.__parent.layout_tab2)

        self.__parent.show()

        return (plot1, plot2)

    def get_img(self):
        img_data = BytesIO()
        self.__fig.savefig(img_data, format=self.__IMG_FORMAT)

        seek_offset = 0
        img_data.seek(seek_offset)

        return img_data


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
    singleton = Singleton.get_instance()

    n_of_unimportant_column = 4

    unimportant_days_before = (singleton.get_date_range()[0] - singleton.get_start_day()).days
    unimportant_days_after = (singleton.get_end_day() - singleton.get_date_range()[1]).days

    country_data_line = country_data_line.split(",")

    n_of_unimportant_column = n_of_unimportant_column + unimportant_days_before
    last_element_index = len(country_data_line) - unimportant_days_after

    n_of_patients_in_time = country_data_line[n_of_unimportant_column:last_element_index - 1]
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
