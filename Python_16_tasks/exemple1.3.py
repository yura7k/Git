from PySide2.QtWidgets import *
from PySide2.QtCore import Slot

@Slot() # slot decorator 
def onClick(): # A slot is basically a function you call 
  label.setText("You clicked the button")

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button = QPushButton("I'm just a Button man")
label = QLabel('¯\_(ツ)_/¯')
button.clicked.connect(onClick) # clicked signal
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()