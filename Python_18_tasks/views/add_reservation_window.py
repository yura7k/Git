from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt
from services.apartment_service import Apartment_service
from services.guest_service import Guest_service

class AddReservationWindow(QMdiSubWindow):
    object = None
    apts_list = []
    user_list = []
    
    def __init__(self, mdi):
        if not AddReservationWindow.object:
            super().__init__()
            AddReservationWindow.object = self
            self.setAttribute(Qt.WA_DeleteOnClose, True)
            self.Render(mdi)
        self = AddReservationWindow.object

        self.showMaximized()

    def closeEvent(self, event):
        AddReservationWindow.object = None

    def Render(self, mdi):
        widget = QWidget()
        grid = QGridLayout()
        grid.setRowMinimumHeight(1, 50)
        grid.setRowMinimumHeight(3, 50)

        apt_label = QLabel("Apt name")
        grid.addWidget(apt_label, 0, 0)
        
        self.get_apartments()
        self.apt_line_edit = QLineEdit(self)
        self.apt_line_edit.setPlaceholderText("select apt")
        completer = QCompleter(self.apts_list, self.apt_line_edit)
        self.apt_line_edit.setCompleter(completer)
        grid.addWidget(self.apt_line_edit, 1, 0)


        user_name_label = QLabel("User name")
        grid.addWidget(user_name_label, 2, 0)
        
        self.get_guests()
        self.user_line_edit = QLineEdit(self)
        self.user_line_edit.setPlaceholderText("select user")
        completer2 = QCompleter(self.user_list, self.user_line_edit)
        self.user_line_edit.setCompleter(completer2)
        grid.addWidget(self.user_line_edit, 3, 0)


        new_user_btn = QPushButton("New User")
        grid.addWidget(new_user_btn, 3, 1)

        check_in_label = QLabel("Check-in")
        grid.addWidget(check_in_label, 0, 2)
        check_in = QDateEdit()
        grid.addWidget(check_in, 1, 2)

        check_out_label = QLabel("Check-out")
        grid.addWidget(check_out_label, 2, 2)
        check_out = QDateEdit()
        grid.addWidget(check_out, 3, 2)

        save_btn = QPushButton("Save")
        grid.addWidget(save_btn, 3, 3, Qt.AlignRight)

        filler = QSpacerItem(150, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        grid.addItem(filler, 4, 0)

        widget.setLayout(grid)
        self.setWidget(widget)
        self.setWindowTitle("Add Reservation")
        mdi.addSubWindow(self)

    def get_apartments(self):
        apt_service = Apartment_service()
        self.apts_list = apt_service.get_apartments()

    def get_guests(self):
        guest_service = Guest_service()
        self.user_list = guest_service.get_guests()