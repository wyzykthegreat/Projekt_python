import sys
from PyQt5.QtWidgets import QApplication
from GUI.window import Window

if __name__ == "__main__":
    app = QApplication([])

    tabs_app = Window()

    sys.exit(app.exec_())