from PySide2.QtWidgets import QApplication
import sys
import mainwindow_app


def main():
    # pyside2 setup
    app = QApplication(sys.argv)
    window = mainwindow_app.MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()