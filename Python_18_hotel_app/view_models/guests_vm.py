from PySide2 import *
from PySide2.QtCore import SIGNAL

class GuestsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, service):
        super().__init__()
        self.guests_data = data
        self.columns = {
            "Name": "name", 
            "Age": "age", 
            "Card": "is_card", 
        }
        self.service = service

    def getData(self, idx):
        return self.guests_data[idx]

    def rowCount(self, *args, **kwargs):
        return len(self.guests_data)

    def columnCount(self, *args, **kwargs):
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            keys = list(self.columns.keys())
            return keys[section]

    def data(self, index, role):
        row = self.guests_data[index.row()]
        keys = list(self.columns.values())
        column = keys[index.column()]
        try:
            if role == QtCore.Qt.DisplayRole:
                return str(row[column])
        except KeyError:
            return None

    def updateRow(self, rowIdx, data):
        self.beginResetModel()
        self.service.guest_add(data)
        self.guests_data = self.service.guest_list()
        self.endResetModel()
        return True

    def removeRow(self, row_id):
        self.beginResetModel()
        name = self.guests_data[row_id]['name']
        self.service.remove_guest(name)
        self.guests_data = self.service.guest_list()
        self.endResetModel()
        return True