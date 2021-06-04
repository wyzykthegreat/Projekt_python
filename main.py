import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from GUI.window import Window
from Backend.updates import Update_Web_Data
from requests.exceptions import ConnectionError

if __name__ == "__main__":
    app = QApplication([])

    try:
        Update_Web_Data().update_new_cases()
        Update_Web_Data().update_recovered()
    except ConnectionError as err:
        msg = QMessageBox()
        msg.setWindowTitle("Caught error")
        msg.setText("Unable to download newest data (check your Internet connection)")
        msg.exec_()
        sys.exit(app.exec_())


    tabs_app = Window()

    sys.exit(app.exec_())
