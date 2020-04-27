from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap

app = QApplication([])
window = QWidget()

#Add a Label:
label = QLabel()

label2 = QLabel("1234")


#Add a pixmap instance to the label:
label.setPixmap(QPixmap("./Drone.p2D.JPG"))
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(label2)

window.setLayout(layout)
window.show()
app.exec_()