from PySide2.QtWidgets import *
from PySide2.QtCore import *
from mainwindow_ui import Ui_MainWindow
from ToDoModel import TodoModel
import json


class MainWindow(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # using pyside2 https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html

        # to do list model and view
        self.model = TodoModel()  # our model class, our "Data"
        self.load()
        #self.model = TodoModel(todos=[(False, 'my first to do')]) # manually set one
        self.todoView.setModel(self.model)  # set the list in the gui to the model

        # set up signals etc here
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        text = self.todoedit.text()
        if text:
            self.model.todos.append((False, text))  # add item to the to the model object
            self.model.layoutChanged.emit()  # raise signal that view needs to be updated from model
            # self.model.layoutChanged.emit()  # used if data changed but lines did not change
            self.todoedit.setText("")  # blank out the field
            self.save()

    def delete(self):
        indexes = self.todoView.selectedIndexes()  # get lines that are selected
        if indexes:  # if any were actually selected
            index = indexes[0]  # in single select mode, will only be the first index
            del self.model.todos[index.row()]  # just like in the model, we have the row here
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()
            self.save()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0] # in single select mode, only first index, hard setting
            row = index.row()  # again, just the 1 row
            status, text = self.model.todos[row]    # gets the row's data from the list as 2 variables
            print(str(status))  # just to prove what data we get
            print(text)
            self.model.todos[row] = (True, text)    # sets the row as done
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()
            self.save()

    def load(self):
        try:
            with open('data.json', 'r') as f:
                self.model.todos = json.load(f)
        except Exception as e:
            print(e)

    def save(self):
        with open('data.json', 'w') as f:
            data = json.dump(self.model.todos, f)