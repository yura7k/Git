from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit, QCompleter
from PySide2.QtCore import QSize
 
 
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(480, 80)) 
        self.setWindowTitle("Auto complete")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
 
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
 
        grid_layout.addWidget(QLabel("Test test", self), 0, 0)
 
        lineEdit = QLineEdit(self)
        strList = ['Python', 'PyQt5', 'Qt', 'Django', 'QML'] 
        completer = QCompleter(strList, lineEdit)
        lineEdit.setCompleter(completer)    
        grid_layout.addWidget(lineEdit, 0, 1)
 
 
if __name__ == "__main__":
    import sys
 
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())