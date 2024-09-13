import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class GUI(QMainWindow):
    def __init__(self, path):
        super().__init__(None)
        self.path = path
        self.ui = uic.loadUi("Window/screens/" + path, self)
        self._build()
        self.ui.show()
        # self.actionSingle_Archive.triggered.connect(self.archive)

    # def archive(self):
    #     self.window = QtWidgets.QMainWindow()
    #     uic.loadUi(self.path)
    #     self.window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GUI()
    win.show()
    sys.exit(app.exec())