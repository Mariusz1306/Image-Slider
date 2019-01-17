from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QVBoxLayout, QLabel, QSlider)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import os

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.width = 640
        self.height = 480
        
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("Kolokwium")
        
        self.setGeometry(10, 10, self.width, self.height)

        mid = Mid()
        self.setCentralWidget(mid)
        self.show()


class Mid(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Mid, self).__init__(parent)
        self.mainLayout = QVBoxLayout()
        self.width = 640
        self.height = 480

        self.files = []
        for file in os.listdir():
            if file.endswith(".jpg"):
                self.files.append(os.path.join(os.getcwd(), file))
        
        self.label = QLabel(self)
        self.label.resize(self.width, self.height-40)
        self.pixmap = QPixmap(self.files[0])
        self.pixmap = self.pixmap.scaled(self.width, self.height-40)
        self.label.setPixmap(self.pixmap)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(len(self.files)-1)
        self.slider.setTickInterval(1)
        print(len(self.files))
        self.slider.setSingleStep(1)
        self.slider.valueChanged.connect(self.valuechange)
        
        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.slider)

        self.setLayout(self.mainLayout)

    def valuechange(self):
        value = self.slider.value()
        pixmap = QPixmap(self.files[value])
        pixmap = pixmap.scaled(self.width, self.height-40)
        self.label.setPixmap(pixmap)
        self.mainLayout


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
