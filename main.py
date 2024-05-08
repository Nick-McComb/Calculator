#import numpy as np
#import math as math
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel
import sys 
from PyQt6.QtGui import QIcon, QFont
from functools import partial
from PyQt6.QtCore import Qt



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
        #self.mk_button("Sto>", 10,528)
        self.mk_button("1", 78,528)
        self.mk_button("2", 146,528)
        self.mk_button("3",214,528)
        self.mk_button("+",282,528, '#A9A7A7')
        self.mk_button("ENTER",282,564,'#A9A7A7', 12)
        self.n=0
        self.new_line_text = ""
#add screen
        self.create_widgets()

    

    def mk_button(self,text, x , y, color ='#f7fffd', font = 15):
        btn = QPushButton(text,self)
        btn.setGeometry(x,y,58,26)
        btn.setFont(QFont('Times New Roman',font))
        btn.setStyleSheet('background-color:'+color)
        btn.clicked.connect(partial(self.clicked_button,text))



    def create_widgets(self):
        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label.setGeometry(10,10,330,184)
        self.label.setStyleSheet('background-color:#a6bf9f')
        self.label.setFont(QFont('Times New Roman', 17))
    
    def clicked_button(self,something):
        current_text = self.label.text()

        if something == "ENTER":
            self.new_line_text= str(eval(self.label.text().split('\n')[self.n]))
            self.label.setText(current_text + "\n" + self.new_line_text + "\n")
            self.n+=2
        else:
                #current_text = self.label.text()
                current_text = current_text + self.new_line_text
                self.label.setText(current_text+something)
                self.new_line_text = ""
                
        



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())


