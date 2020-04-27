from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class TodoModel(QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        # tuples of (bool, str)
        self.todos = todos or []  # self.todos = list that is passed or a blank list
        self.tick = QImage('tick.png')

    # Have to implement this. QT will call it whenever it wants, e.g. if we say data is updated
    def data(self, index, role):
        # index: contains .row() and .column(). For this, column will be always 0
        # role: a flag from QT that indicates what is being requested.
        # role will be DisplayRole for the main data. Other things include
        # tooltips, status bars etc. See table in tutorial for options.
        # https://doc.qt.io/qt-5/qt.html#ItemDataRole-enum

        if role == Qt.DisplayRole:  # the main data view role, in this case expects a string (QString)
            status, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole: # a different role, this will update at the same time too
            status, _ = self.todos[index.row()]
            if status:
                return self.tick

    # Have to implement a way to determine how many items there are
    def rowCount(self, index):
        return len(self.todos)