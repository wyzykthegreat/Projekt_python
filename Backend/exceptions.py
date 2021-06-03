class UnableToGenerateReportException(Exception):
    def __init__(self):
        msg = f"Unable to generate report (no countries were selected)"
        super().__init__(msg)

class UnableToAddMoreCountriesToGraph(Exception):
    def __init__(self):
        msg = f"Unable to add more countries to the graph (there can be only 6 countries plotted at a time)"
        super().__init__(msg)