from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt

@Slot() #slot decorator
def sliderValue(val):
    label.setText('Slider Value: ' + str(val))

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

slider = QSlider(Qt.Horizontal)
slider.setMinimum(20)
slider.setMaximum(200)
slider.valueChanged[int].connect(sliderValue) #valueChanged signal

label = QLabel('Slider Value:')
layout.addWidget(label)
layout.addWidget(slider)
window.setLayout(layout)
window.show()
app.exec_()
