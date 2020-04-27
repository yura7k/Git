from PySide2.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QGridLayout() # GRID LAYOUT 

label = QLabel('Test')
button_1 = QPushButton("(1,1) Button")
button_2 = QPushButton("(2,2) Button")
button_3 = QPushButton("(3,3) Button")

layout.addWidget(label, 0, 0) # Note the Row Column coordinates
layout.addWidget(button_1, 1, 1)
layout.addWidget(button_2, 2, 2)
layout.addWidget(button_3, 3, 3)

window.setLayout(layout)
window.show()
app.exec_()
