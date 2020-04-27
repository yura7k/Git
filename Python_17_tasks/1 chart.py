from PySide2 import QtGui
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from random import randint 

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

# Initialize chart
chart = QtCharts.QChart()
lineSeries = QtCharts.QLineSeries()]
lineSeries2 = QtCharts.QLineSeries()

# Make some random data points
dataSeries = [(i+1, randint(0, 99999)) for i in range(200)]
dataSeries2 = [(i+1, randint(0, 99999)) for i in range(200)]

# load data into chart:
for point in dataSeries:
    lineSeries.append(point[0],point[1])

# load data into chart:
for point in dataSeries2:
    lineSeries2.append(point[0],point[1])

# Add Some Chart Options
chart.addSeries(lineSeries)
chart.addSeries(lineSeries2)
chart.setTitle("Random Numbers from 0-99999")
chart.createDefaultAxes()

# Create a container (similar to a widget)
chartView = QtCharts.QChartView(chart)
chartView.setRenderHint(QPainter.Antialiasing)

# Some Chart Styling
lineSeries.setColor(QtGui.QColor("red"))
lineSeries2.setColor(QtGui.QColor("black"))
chartView.chart().setBackgroundBrush(QtGui.QColor("ivory"))
layout.addWidget(chartView)

window.setLayout(layout)
window.show()
window.resize(600, 400)
app.exec_()