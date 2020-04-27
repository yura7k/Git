import datetime
from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt
from services.apartment_service import Apartment_service
from services.guest_service import Guest_service
from services.booking_service import Booking_service
from view_models.apartments_vm import ApartmentsTableModel


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
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.apt_line_edit.setCompleter(completer)
        grid.addWidget(self.apt_line_edit, 1, 0)

        user_name_label = QLabel("User name")
        grid.addWidget(user_name_label, 2, 0)
        
        self.get_guests()
        self.user_line_edit = QLineEdit(self)
        self.user_line_edit.setPlaceholderText("select user")
        completer2 = QCompleter(self.user_list, self.user_line_edit)
        completer2.setCaseSensitivity(Qt.CaseInsensitive)
        self.user_line_edit.setCompleter(completer2)
        grid.addWidget(self.user_line_edit, 3, 0)

        new_user_btn = QPushButton("New User")
        grid.addWidget(new_user_btn, 3, 1)

        check_in_label = QLabel("Check-in")
        grid.addWidget(check_in_label, 0, 2)
        self.check_in = QDateEdit()
        grid.addWidget(self.check_in, 1, 2)

        check_out_label = QLabel("Check-out")
        grid.addWidget(check_out_label, 2, 2)
        self.check_out = QDateEdit()
        grid.addWidget(self.check_out, 3, 2)

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.SaveBooking)
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

    def parceDate(self, data):
        splitData = data.split(".")
        date = datetime.date(int(splitData[2]), int(splitData[1]), int(splitData[0]))
        return date


    @Slot()
    def SaveBooking(self):
        guest = Guest_service()
        guest_id = guest.search_guest(guest_name = self.user_line_edit.text())
        
        Apartments = Apartment_service()
        apartments = Apartments.search_apartment(name = self.apt_line_edit.text())
       
        apartment = apartments[0]
        apartment_price = apartment.price
        
        if (apartments == None or len(apartments) == 0):
            print("Error")
            return

        data = {
            "name": self.apt_line_edit.text(),
            "guest_name": self.user_line_edit.text(),
            "guest_id": guest_id,
            "booked_date": datetime.datetime.now(),
            "chek_in_date": self.parceDate(data = self.check_in.text()),
            "chek_in_date": self.parceDate(data = self.check_out.text()),
            "price": apartment_price
        }
        
        #self.model.updateRow(self.rowIdx, data)
       
        booking = Booking_service()
        booking.booking_add(data)