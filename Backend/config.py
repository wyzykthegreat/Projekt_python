from datetime import date, timedelta
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
            self.countries = []
            self.date_range = self.__prepare_date_range()
            self.start_day = self.date_range[0]
            self.end_day = self.date_range[1]
            self.n_of_days = self.__date_diff()
            Singleton.__instance = self

    def add_country(self, country_name):
        self.countries.append(country_name)

    def set_date_range(self, start_date: date, end_date: date):
        self.date_range = (start_date, end_date)

    def print_data(self):
        print(f"Countries: {self.countries}\nDate_range: {self.date_range}")

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

        return (start_date, end_date)

    def __date_diff(self):
        delta = self.date_range[1] - self.date_range[0]
        return (delta.days)