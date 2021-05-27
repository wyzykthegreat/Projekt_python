global FILENAME_RECOVERED
global FILENAME_NEW_CASES
global DATA
FILENAME_RECOVERED = "covid_19_recovered.csv"
FILENAME_NEW_CASES = "covid_19_cases.csv"

import datetime

class Singleton():
    def __init__(self):
        self.countries = []
        self.date_range = ()

    def add_country(self, country_name):
        self.countries.append(country_name)

    def set_date_range(self, start_date: datetime, end_date: datetime):
        self.date_range = (start_date, end_date)