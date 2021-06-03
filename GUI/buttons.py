from PyQt5.QtWidgets import QPushButton, QFileDialog, QMessageBox
from reportlab.lib.utils import ImageReader
from Backend.report import Report
from Backend.config import Singleton
from Backend.exceptions import UnableToGenerateReportException


class ReportBtn(QPushButton):
    def __init__(self, name, graph1, graph2):
        super().__init__(name)
        self.__graph1 = graph1
        self.__graph2 = graph2

        self.__pdf_generator = Report()

        self.clicked.connect(self.__btn_action)

    def __btn_action(self):
        data = Singleton.get_instance()

        self.__graph1 = self.__graph1.update_graph()[0]
        self.__graph2 = self.__graph2.update_graph()[1]
<<<<<<< HEAD
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
=======
        img_data1 = self.__graph1.get_img()
        img_data2 = self.__graph2.get_img()
        img1 = ImageReader(img_data1)
        img2 = ImageReader(img_data2)

        filename = self.__prepare_file_chooser()
        if filename:
            self.__pdf_generator.create_and_save_report(img1, img2, filename)
>>>>>>> 33b8e013a92ab7f1a3eec249dcf3f72823c6e970

    def __prepare_file_chooser(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save PDF report", filter="PDF Files (*.pdf)")
        return filename
