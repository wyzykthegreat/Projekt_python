from datetime import date
from Backend.updates import LoadInitData

global FILENAME_RECOVERED
global FILENAME_NEW_CASES
FILENAME_RECOVERED = "covid_19_recovered.csv"
FILENAME_NEW_CASES = "covid_19_cases.csv"


class Singleton():
    __instance = None

    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance == None:
            self.__countries = []

            self.__date_range = None
            self.__prepare_date_range()

            self.__start_day = self.__date_range[0]
            self.__end_day = self.__date_range[1]

            Singleton.__instance = self

    def add_country(self, country_name):
        self.__countries.append(country_name)

    def remove_country(self, country_name):
        self.__countries.remove(country_name)

    def get_start_day(self):
        return self.__start_day

    def get_end_day(self):
        return self.__end_day

    def set_date_range(self, start_date: date, end_date: date):
        self.__date_range = (start_date, end_date)

    def print_data(self):
        print(f"Countries: {self.__countries}\nDate_range: {self.__date_range}")

    def __prepare_date_range(self):
        dates = LoadInitData(FILENAME_RECOVERED).get_date_range()
        start_date_str = dates[0]
        end_date_str = dates[1]

        start_date_arr = start_date_str.split("/")
        end_date_arr = end_date_str.split("/")

        for i in range(3):
            start_date_arr[i] = int(start_date_arr[i])
            end_date_arr[i] = int(end_date_arr[i])

        start_date = date(2000+start_date_arr[2], start_date_arr[0], start_date_arr[1])
        end_date = date(2000+end_date_arr[2], end_date_arr[0], end_date_arr[1])

        self.set_date_range(start_date, end_date)

    def get_date_range(self):
        return self.__date_range

    def get_countries_list(self):
        return self.__countries

    def get_n_of_days(self):
        delta = self.__end_day - self.__start_day
        return (delta.days)

    def remove_all_countries(self):
        self.__countries = []