#import numpy as np
#import math as math
from PyQt6.QtWidgets import QWidget, QApplication
import sys 
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("calculator.png"))
        self.setFixedHeight(500)
        self.setFixedWidth(350)
        
    

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())


