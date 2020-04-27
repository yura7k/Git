from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap

app = QApplication([])
window = QWidget()

#Add a Label:
label = QLabel()

#Add a pixmap instance to the label:
label.setPixmap(QPixmap("./4.png"))
layout = QVBoxLayout()

layout.addWidget(label)
window.setLayout(layout)
window.show()
app.exec_()