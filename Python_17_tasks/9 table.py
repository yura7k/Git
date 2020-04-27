from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PySide2.QtCore import QSize, Qt
 
 
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(480, 80))           
        self.setWindowTitle("Test QTableWidget")   
        central_widget = QWidget(self)          
        self.setCentralWidget(central_widget)    
 
        grid_layout = QGridLayout()          
        central_widget.setLayout(grid_layout) 
 
        table = QTableWidget(self) 
        table.setColumnCount(3)
        table.setRowCount(1)
 
        table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])
 
        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        table.horizontalHeaderItem(2).setToolTip("Column 3 ")
 
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
 
        table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
 
        table.resizeColumnsToContents()
 
        grid_layout.addWidget(table, 0, 0)
 
 
if __name__ == "__main__":
    import sys
 
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())