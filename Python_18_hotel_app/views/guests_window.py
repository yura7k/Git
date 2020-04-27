from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QDoubleValidator
from view_models.guests_vm import GuestsTableModel
from services.guest_service import Guest_service

class GuestsWindow(QMdiSubWindow):
    object = None
    rowIdx = -1
    
    def __init__(self, mdi):
        if not GuestsWindow.object:
            super().__init__()
            GuestsWindow.object = self
            self.setAttribute(Qt.WA_DeleteOnClose, True)
            self.Render(mdi)
        self = GuestsWindow.object

        self.showMaximized()

    def closeEvent(self, event):
        GuestsWindow.object = None

    def Render(self, mdi):
        widget = QWidget()
        vbox = QHBoxLayout()

        self.table = self.RenderGuestsTable()

        grid = QGridLayout()
        grid.setMargin(20)
        grid.rowMinimumHeight(40)

        name_label = QLabel("Name")
        self.name_field = QLineEdit()
        
        age_label = QLabel("Age")
        self.age_field = QLineEdit()
        self.age_field.setValidator(QDoubleValidator(0, 100, 2))
        
        self.card_chekboks = QCheckBox("Is Card")
        self.card_chekboks.stateChanged.connect(self.is_card_change)

        grid.addWidget(name_label, 0, 0, 1, 0)
        grid.addWidget(self.name_field, 1, 0, 1, 0)

        grid.addWidget(age_label, 2, 0, 1, 0)
        grid.addWidget(self.age_field, 3, 0, 1, 0)

        grid.addWidget(self.card_chekboks, 5, 0, 1, 0)
        
        new_btn = QPushButton("New")
        new_btn.clicked.connect(self.NewRow)
        grid.addWidget(new_btn, 6, 0)
               
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.SaveRow)
        grid.addWidget(save_btn, 6, 1)

        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(self.RemoveRow)
        grid.addWidget(delete_btn, 6, 2)

        filler = QSpacerItem(150, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        grid.addItem(filler, 8, 0)

        vbox.addWidget(self.table)
        vbox.addLayout(grid)

        widget.setLayout(vbox)
        self.setWidget(widget)
        
        self.setWindowTitle("Guests")
        mdi.addSubWindow(self)

    def RenderGuestsTable(self):
        table = QTableView(self) 
        table.setMaximumWidth(500)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.clicked.connect(self.RowSelected)

        guests = Guest_service()
        self.guests_data = guests.guest_list()
        self.model = GuestsTableModel(self.guests_data, guests)
        table.setModel(self.model)

        return table

    def is_card_change(self):
        pass

    @Slot()
    def RowSelected(self, arg):
        self.rowIdx = arg.row()
        model = arg.model()

        row = model.getData(self.rowIdx)
        self.name_field.setText(row['name'])
        self.age_field.setText(str(row['age']))
        if row['is_card'] == True:
            self.card_chekboks.setChecked(True)
        else:
            self.card_chekboks.setChecked(False)

    @Slot()
    def RemoveRow(self):
        if self.rowIdx < 0:
            return
        
        self.model.removeRow(self.rowIdx)

    @Slot()
    def SaveRow(self):
        if (self.card_chekboks.isChecked()):
            is_card = True
        else:
            is_card = False
        data = {
            "name": self.name_field.text(),
            "age": self.age_field.text(),
            "is_card": is_card
        }
        self.model.updateRow(self.rowIdx, data)

    @Slot()
    def NewRow(self):
        self.rowIdx = -1
        self.name_field.setText('')
        self.age_field.setText('')
        self.card_chekboks.setChecked(False)