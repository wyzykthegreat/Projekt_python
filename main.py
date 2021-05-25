import sys
from PyQt5.QtWidgets import QApplication
from GUI.window import Window
from Backend.updates import Update_Web_Data

if __name__ == "__main__":
    Update_Web_Data().update_new_cases()
    Update_Web_Data().update_recovered()

    app = QApplication([])

    tabs_app = Window()

    sys.exit(app.exec_())