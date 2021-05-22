import sys

from PyQt5.QtWidgets import QCheckBox


class Cbx(QCheckBox):
    def __init__(self, name):
        super().__init__(name)

    def clicked(self, cntries):
        if self.isChecked():
            cntries.append(self)
        else:
            pass
