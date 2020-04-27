#Let's add a different widget, a common slider...
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout() 
# Define slider widget, note the orientation argument:
slider = QSlider(Qt.Horizontal) 
button = QPushButton("I'm just a Button man")
layout.addWidget(QLabel('Hello World!'))
layout.addWidget(slider) #Add the slider
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()