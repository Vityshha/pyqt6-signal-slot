from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

from PyQt6.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

from Receiver import Receiver
from Sender import Sender

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui_sender = Sender()
        self.ui_receiver = Receiver()

        self.init_connect()


    def init_connect(self):
        self.ui_sender.signal_sender.connect(self.ui_receiver.put_text)
        self.ui_receiver.signal_receiver.connect(self.ui_sender.put_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.ui_sender.show()
    main.ui_receiver.show()
    sys.exit(app.exec())