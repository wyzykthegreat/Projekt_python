from datetime import date

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
            self.date_range = (1, 5)
            Singleton.__instance = self

    def add_country(self, country_name):
        self.countries.append(country_name)

    def set_date_range(self, start_date, end_date):
        self.date_range = (start_date, end_date)

    def print_data(self):
        print(f"Countries: {self.countries}\nDate_range: {self.date_range}")
