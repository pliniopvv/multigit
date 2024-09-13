from PyQt5 import QtWidgets
from PyQt5.QtCore import QStringListModel

from Window import GUI

class RepositoryList(GUI):
    def __init__(self):
        super().__init__('RepositoriesView.ui')

    def _build(self):
        self.model = QStringListModel()
        self.ui.list.setModel(self.model)

    def addItem(self, name):
        current_items = self.model.stringList()
        current_items.append(name)
        self.model.setStringList(current_items)