from PyQt5.QtWidgets import QPushButton, QFileDialog, QMessageBox
from reportlab.lib.utils import ImageReader
from Backend.report import Report
from Backend.config import Singleton
from Backend.exceptions import UnableToGenerateReportException
from GUI.countries_list import ListWidget
from GUI.graph import GraphWidget


class ReportBtn(QPushButton):
    def __init__(self, parent, name):
        super().__init__(name)
        self.__parent = parent
        self.__graph1 = GraphWidget(self.__parent, "Zakazeni")
        self.__graph2 = GraphWidget(self.__parent, "Ozdrowieni")

        self.__pdf_generator = Report()

        self.clicked.connect(self.__btn_action)

    def __btn_action(self):
        data = Singleton.get_instance()

        self.__graph1 = self.__graph1.update_graph()[0]
        self.__graph2 = self.__graph2.update_graph()[1]
        try:
            if data.get_countries_list() == []:
                raise UnableToGenerateReportException()
            else:
                img_data1 = self.__graph1.get_img()
                img_data2 = self.__graph2.get_img()
                img1 = ImageReader(img_data1)
                img2 = ImageReader(img_data2)
                filename = self.__prepare_file_chooser()
                if filename:
                    self.__pdf_generator.create_and_save_report(img1, img2, filename)
        except UnableToGenerateReportException as err:
            msg = QMessageBox()
            msg.setWindowTitle("Caught error")
            msg.setText(f"{err}")
            msg.exec_()

    def __prepare_file_chooser(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save PDF report", filter="PDF Files (*.pdf)")
        return filename

class UncheckBtn(QPushButton):
    def __init__(self, parent, list_widget: ListWidget, name):
        super().__init__(name)
        self.__cbx_list = list_widget.get_cbx_group()
        self.__parent = parent

        self.clicked.connect(self.__btn_action)

    def __btn_action(self):
        data = Singleton.get_instance()

        for cbx in self.__cbx_list:
            cbx.setChecked(False)

        data.remove_all_countries()

        self.__update_graph()

    def __update_graph(self):
        plot = GraphWidget(self.__parent, "Ozdrowieni")
        plot.update_graph()