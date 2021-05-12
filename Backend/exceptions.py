#zrobione wszystko z pdfa

class UnableToGenerateReportException(Exception):
    def __init__(self, arg_name):
        msg = f"Error! UnableToGenerateReportException (arg name: {arg_name})"
        super().__init__(msg)

class UnableToDownloadNewestData(Exception):
    def __init__(self, arg_name):
        msg = f"Error! UnableToDownloadNewestData (arg name: {arg_name})"
        super().__init__(msg)

class UnableToAddMoreCountriesToGraph(Exception):
    def __init__(self, arg_name):
        msg = f"Error! UnableToAddMoreCountriesToGraph (arg name: {arg_name})"
        super().__init__(msg)