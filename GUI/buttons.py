from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QGridLayout, QCheckBox, QLabel, QScrollArea, \
    QFormLayout, QGroupBox, QPushButton, QHBoxLayout
from GUI.graph import get_countries


class PushButton(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        layout.addWidget(ReportBtn())
        # layout.spacing = 2
        layout.addWidget(UpdateBtn())

        self.setLayout(layout)


class UpdateBtn(QPushButton):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        UpdateButton = QPushButton("Zaaktualizuj dane")
        UpdateButton.clicked.connect(lambda _: print("To bedzie aktualizowac"))
        layout.addWidget(UpdateButton)
        self.setLayout(layout)


class ReportBtn(QPushButton):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        ReportButton = QPushButton("PDF")

        ReportButton.clicked.connect(lambda _: print("PDF"))
        layout.addWidget(ReportButton)
        self.setLayout(layout)

    def sprawdzanie(self):
        size = get_countries("time_series_covid19_confirmed_global.csv")
