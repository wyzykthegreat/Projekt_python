from datetime import date
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen.canvas import Canvas


class Report:

    def __init__(self):
        self.__author = "SWK"
        self.__title = f"Covid raport ({date.today()})"

    def create_and_save_report(self, img1, img2, filepath, pagesize=A3):
        pdf_template = self.__create_pdf_template(filepath, img1, img2, pagesize)
        pdf_template.setAuthor(self.__author)
        pdf_template.setTitle(self.__title)
        pdf_template.save()

    def __create_pdf_template(self, filepath, img1, img2, pagesize):
        canvas = Canvas(filepath, pagesize=pagesize)
        canvas.setFont("Times-Roman", 40)
        title = self.__title

        title_magic_offset_y = 50
        title_x = A3[0] / 2
        title_y = A3[1] - title_magic_offset_y

        canvas.drawCentredString(title_x, title_y, title)
        canvas.drawImage(img1, 200, 600)
        canvas.drawImage(img2, 200, 100)
        return canvas
