from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont, QPixmap
from services.booking_service import Booking_service
from services.apartment_service import Apartment_service

class MainWindow(QMdiSubWindow):
    def __init__(self, mdi):
        super().__init__()

        widget = QWidget()
        hbox = QHBoxLayout()

        vboxLeft = QVBoxLayout()
        table = self.RenderBookingList()
        vboxLeft.addWidget(table)
        vboxLeft.setMargin(15)
        hbox.addLayout(vboxLeft)

        vbox = QVBoxLayout()
        vbox.setMargin(15)
        calendar = QCalendarWidget()
        vbox.addWidget(calendar)

        font = QFont("Helvetica", 14, 1, True)
        count_apt = "Apartments available - " + self.apartment_count()
        label_apartments = QLabel(count_apt)
        label_apartments.setMinimumHeight(50)
        label_apartments.setFont(font)
        vbox.addWidget(label_apartments)

        count_book = "Bookings created - " + self.booking_count()
        label_bookings = QLabel(count_book)
        label_bookings.setMinimumHeight(50)
        label_bookings.setFont(font)
        vbox.addWidget(label_bookings)
        
        hbox.addLayout(vbox)

        widget.setLayout(hbox)
        self.setWidget(widget)
        mdi.addSubWindow(self)
        
        self.setWindowFlags(~Qt.WindowMinMaxButtonsHint & ~Qt.WindowCloseButtonHint)
        self.setAttribute(Qt.WA_DeleteOnClose, True)

    def RenderBookingList(self):
        list = QListWidget()
        service = Booking_service()
        for row in service.booking_list():
            item = QListWidgetItem() 
            widget = self.RenderItem(
                row['name'], 
                row['user_name'], 
                row['check_in'], 
                row['check_out']
            )
            item.setSizeHint(widget.sizeHint())   
            list.addItem(item)
            list.setItemWidget(item, widget)
        return list

    def RenderItem(self, name, user_name, check_in, check_out):
        widget = QWidget()
        widgetLayout = QHBoxLayout()
        widgetVerticalLayout = QVBoxLayout()

        image_label = QLabel("image placeholder")
        image_label.setPixmap(QPixmap("./Python_18_hotel_app/icon.jpg"))
        image_label.setMaximumWidth(50)
        widgetLayout.addWidget(image_label)

        apt_label = QLabel("{} - {}".format(name, user_name))
        checkin_label = QLabel("{} - {}".format(check_in, check_out))
        widgetVerticalLayout.addWidget(apt_label)
        widgetVerticalLayout.addWidget(checkin_label)
        widgetLayout.addLayout(widgetVerticalLayout)

        widget.setLayout(widgetLayout)
        return widget

    def booking_count(self):
        bookings = Booking_service()
        count = len(bookings.booking_list())
        return str(count)
    
    def apartment_count(self):
        apartments = Apartment_service()
        count = len(apartments.apartments_list())
        return str(count)