from designe import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

from PyQt6.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

class Sender(QtWidgets.QMainWindow):

    signal_sender = Signal(str)

    def __init__(self):
        super(Sender, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.btn_click)

    @Slot(str)
    def put_text(self, text):
        self.ui.textEdit.setText(text)

    def btn_click(self):
        text = self.ui.textEdit.toPlainText()
        #self.ui.btn.clicked.emit(text)
        self.signal_sender.emit(text)

