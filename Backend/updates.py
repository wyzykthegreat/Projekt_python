import requests
import Backend.data
from Backend.exceptions import UnableToDownloadNewestData
from GUI.tabs import TabsWidget
from Backend.data import Parameters

class Read_parmeters():
    pass
    #data.Parameters
    #wczytuje parametry ustawione przez uzytkownika

    def read_selected_tab(self, tabsWidget: TabsWidget, parameters: Parameters):
        parameters.set_selected_tab(tabsWidget.get_selected_tab())

    def read_selected_countries(self):
        pass

    def read_date_range(self):
        pass

class Update_Web_Data():
    def __init__(self):
        pass

    def update_new_cases(self):

        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
        filename = 'covid_19_cases.csv'
        #rozbic to na download i save(bardziej poprawnie)? #fixme
        self.download(url, filename)

    def update_recovered(self):
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
        filename = 'covid_19_recovered.csv'
        #rozbic to na download i save(bardziej poprawnie)? #fixme
        self.download(url, filename)


    def download(self, url, filename):
        # gdzie i jak tu wsadzic exception? #fixme
        try:
            r = requests.get(url, allow_redirects=True)
            # gdybysmy chcieli zrobic na to osobny folder https://stackabuse.com/creating-and-deleting-directories-with-python/ #fixme
            open(filename, 'wb').write(r.content)
        except UnableToDownloadNewestData as err:
            # może zrobić wyskakujące okienko z błędem?  to chyba w module exceptions te okienka#fixme
            print(f"Error catched: {err}")

class Update_graph_data():
    def __init__(self):
        pass

    def set_graph_type(self):
        pass

    def set_dates_vector(self):
        pass

    def set_countries_vector(self):
        pass

    def set_data_vector(self):
        pass