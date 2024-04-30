#import numpy as np
#import math as math
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel
import sys 
from PyQt6.QtGui import QIcon, QFont

#def mk_button(btn , x , y):
    #btn.setGeometry(x,y,58,26)
    #btn.setFont(QFont('Times New Roman',15))
    #btn.setStyleSheet('background-color:#f7fffd')
    #btn.clicked.connect(self.clicked_button())

class Window(QWidget):
    def __init__(self):
        super().__init__()
#icon & title
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("calculator.png"))
#dimensions
        self.setFixedHeight(600)
        self.setFixedWidth(350)
        self.setStyleSheet('background-color:black')
#making buttons
        self.mk_button("0",78,564)
        self.mk_button(".",146,564)
        self.mk_button("Sto>", 10,528)
        self.mk_button("1", 78,528)
        self.mk_button("2", 146,528)
        self.mk_button("3",214,528)
        self.mk_button("+",282,528)
#add screen
        self.create_widgets()
    
    def mk_button(self,text, x , y):
        btn = QPushButton(text,self)
        btn.setGeometry(x,y,58,26)
        btn.setFont(QFont('Times New Roman',15))
        btn.setStyleSheet('background-color:#f7fffd')
        #btn.clicked.connect(self.clicked_button(text))

    def create_widgets(self):
        #self.mk_button(1,78,564)
      

    


        #btn1.setGeometry(78,564,58,26)
        #btn1.setFont(QFont('Times New Roman',15))
        #btn1.setStyleSheet('background-color:#f7fffd')
        #btn1.setFixedSize(100,80)

        self.label = QLabel("", self)
        self.label.setGeometry(10,10,330,184)
        self.label.setStyleSheet('background-color:#a6bf9f')

    def clicked_button(self,text):
        self.label.setText(text)
        

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())


