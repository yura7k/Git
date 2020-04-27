import sys
import random
from collections import deque
from PySide2 import QtWidgets, QtCore, QtGui, QtMultimedia


class Snake(QtWidgets.QWidget):
    BLOCK_SIZE = 20
    CIRCLE_RADIUS = BLOCK_SIZE // 2
    NUM_BLOCKS_X = 20
    NUM_BLOCKS_Y = 20
    BOARD_WIDTH = BLOCK_SIZE * NUM_BLOCKS_X
    BOARD_HEIGHT = BLOCK_SIZE * NUM_BLOCKS_Y
    GAME_SPEED = 1
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self):
        super().__init__()
        self.setStyleSheet("QWidget { background-color: black }")
        self.setFixedSize(Snake.BOARD_WIDTH, Snake.BOARD_HEIGHT)
        self.game_active = True
        self.timer = QtCore.QBasicTimer()
        self.direction = Snake.RIGHT
        # each tuple (x, y) corresponds to the top left corner of the block (circle)
        self.snake_coords = deque()
        self.snake_coords.append((Snake.BLOCK_SIZE * Snake.NUM_BLOCKS_X // 2,
                                  Snake.BLOCK_SIZE * Snake.NUM_BLOCKS_Y // 2))
        self.food = None
        self.new_food()

        self.score_sound = QtMultimedia.QSound("score.wav")

        self.start_button = QtWidgets.QPushButton("Start", self)
        self.start_button.setStyleSheet("QWidget { background-color: white }")
        self.start_button.move(self.geometry().center() - self.start_button.geometry().center())
        self.start_button.clicked.connect(self.start_game)
        self.game_over_label = QtWidgets.QLabel("Game Over...", self)
        self.game_over_label.setStyleSheet("QLabel {color: yellow; font: 36pt}")
        self.game_over_label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.game_over_label.adjustSize()
        self.game_over_label.move((self.width() - self.game_over_label.width()) // 2, 0)
        self.game_over_label.hide()

        self.setWindowTitle("Snake game")
        self.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_W:
            if self.direction != Snake.DOWN:
                self.direction = Snake.UP
        elif event.key() == QtCore.Qt.Key_S:
            if self.direction != Snake.UP:
                self.direction = Snake.DOWN
        elif event.key() == QtCore.Qt.Key_A:
            if self.direction != Snake.RIGHT:
                self.direction = Snake.LEFT
        elif event.key() == QtCore.Qt.Key_D:
            if self.direction != Snake.LEFT:
                self.direction = Snake.RIGHT
        elif event.key() == QtCore.Qt.Key_Escape:
            QtCore.QCoreApplication.instance().quit()
        elif event.key() == QtCore.Qt.Key_Space:
            if self.start_button.isVisible():
                self.start_game()

    def timerEvent(self, event):
        if self.direction == Snake.UP:
            x, y = self.snake_coords[0]
            # Up is in -y direction
            new_coord = (x, y - Snake.BLOCK_SIZE)
        elif self.direction == Snake.DOWN:
            x, y = self.snake_coords[0]
            new_coord = (x, y + Snake.BLOCK_SIZE)
        elif self.direction == Snake.LEFT:
            x, y = self.snake_coords[0]
            new_coord = (x - Snake.BLOCK_SIZE, y)
        else:
            x, y = self.snake_coords[0]
            new_coord = (x + Snake.BLOCK_SIZE, y)
        self.check_collision(new_coord)
        if self.game_active:
            if not self.check_food():
                self.snake_coords.pop()
            self.repaint()

    def check_food(self):
        if self.snake_coords[0] == self.food:
            self.score_sound.play()
            self.new_food()
            return True
        else:
            return False

    def new_food(self):
        while True:
            new_coord = (Snake.BLOCK_SIZE * random.randint(0, Snake.NUM_BLOCKS_X - 1),
                         Snake.BLOCK_SIZE * random.randint(0, Snake.NUM_BLOCKS_Y - 1))
            if new_coord not in self.snake_coords:
                self.food = new_coord
                break

    def check_collision(self, new_coord):
        x, y = new_coord
        if new_coord in self.snake_coords or x < 0 or y < 0 or x >= Snake.BOARD_WIDTH or y >= Snake.BOARD_HEIGHT:
            self.game_active = False
            self.game_over()
        else:
            self.snake_coords.appendleft(new_coord)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw_food(painter)
        self.draw_snake(painter)
        painter.end()

    def draw_snake(self, painter):
        painter.setPen(QtGui.QColor("green"))
        painter.setBrush(QtGui.QColor("lightgreen"))
        for x, y in self.snake_coords:
            painter.drawRect(x, y, Snake.BLOCK_SIZE, Snake.BLOCK_SIZE)

    def draw_food(self, painter):
        painter.setPen(QtGui.QColor("red"))
        painter.setBrush(QtGui.QColor("red"))
        painter.drawEllipse(*self.food, Snake.BLOCK_SIZE, Snake.BLOCK_SIZE)

    def start_game(self):
        if self.game_active:
            self.timer.start(int(100 / Snake.GAME_SPEED), self)
            self.start_button.hide()
        else:
            self.reset_game()
            self.game_active = True
            self.timer.start(int(100 / Snake.GAME_SPEED), self)
            self.start_button.hide()
            self.game_over_label.hide()

    def reset_game(self):
        self.snake_coords.clear()
        self.snake_coords.append((Snake.BLOCK_SIZE * Snake.NUM_BLOCKS_X // 2,
                                  Snake.BLOCK_SIZE * Snake.NUM_BLOCKS_Y // 2))
        self.new_food()
        self.direction = Snake.RIGHT

    def game_over(self):
        self.timer.stop()
        self.game_over_label.show()
        self.start_button.setText("New game")
        self.start_button.adjustSize()
        self.start_button.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    snake_game = Snake()
    sys.exit(app.exec_())