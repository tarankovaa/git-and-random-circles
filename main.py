import sys
from random import randint


from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.setFixedSize(700, 500)
        self.setWindowTitle('Git и случайные окружности')

        self.paint_btn = QPushButton('Рисовать', self)
        self.paint_btn.resize(75, 23)
        self.paint_btn.move(10, 10)


class Main(MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False
        self.paint_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(10, 300)
        qp.drawEllipse(randint(0, 700 - a), randint(40, 500 - a), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
