import requests

class Update_Web_Data:
    def __init__(self):
        pass

    def update_new_cases(self):
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
        filename = 'covid_19_cases.csv'
        self.download(url, filename)

    def update_recovered(self):
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
        filename = 'covid_19_recovered.csv'
        self.download(url, filename)


    def download(self, url, filename):
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)



class LoadInitData: #do wczytywania parametrow poczatkowych singletona#
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            line = f.readline()
            line = line.split(",")
            self.__dates_line = line[4:]

    def get_date_range(self):
        n = len(self.__dates_line)
        return (self.__dates_line[0], self.__dates_line[n-1])

