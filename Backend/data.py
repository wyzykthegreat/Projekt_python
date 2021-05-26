import Backend.config as config
import datetime

class Parameters():
    def __init__(self):
        self.__selected_tab = None
        self.__selected_countries = config.COUNTRIES
        self.__selected_date_range = ()


    def set_selected_tab(self, selected_tab: str):
        self.__selected_tab = selected_tab


    def set_date_range(self, start_date: datetime, end_date: datetime):
        pass

    def get_selected_tab(self):
        return self.__selected_tab

    def get_selected_countries(self):
        return self.__selected_countries

    def get_date_range(self):
        return self.__selected_date_range


class Graph_data():
    pass

    def set_graph_type(self):
        pass

    def set_dates_vector(self):
        pass

    def set_countries_vector(self):
        pass

    def set_data_vector(self):
        pass

    def get_graph_type(self):
        pass

    def get_dates_vector(self):
        pass

    def get_countries_vector(self):
        pass

    def get_data_vector(self):
        pass