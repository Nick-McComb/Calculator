from libraries import *
import numpy as np
import math as math
import tkinter as tk
from PIL import Image, ImageTk
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel
import sys 
from PyQt6.QtGui import QIcon, QFont
from functools import partial
from PyQt6.QtCore import Qt
import re


def preprocess_check(expr): 
    #inserts * between digit and parenthesis
    expr = re.sub(r'(\d)(\()', r'\1*(', expr)
    #inserts * between parenthesis and digit
    expr = re.sub(r'(\))(\d)', r')*\2', expr)
    #inserts * between variable and digit
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)
    #inserts * between digit and variable
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    #inserts * between parenthesis and variable
    expr = re.sub(r'(\))([a-zA-Z])', r')*\2',expr)
    #inserts * between variable and parenthesis
    #expr = re.sub(r'([a-zA-Z])(\()', r'\1*(', expr)
    #inserts * between parenthesis
    expr = re.sub(r'(\))(\()', r'\1*(', expr)
    
    return(expr)

'''def btn_location(calculator_nums):
    pass'''

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
#make number buttons
        self.create_btns()
#make screen
        self.create_screen()

    def create_screen(self):
        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label.setIndent(10)
        self.label.setGeometry(10,10,330,184)
        self.label.setStyleSheet('background-color:#a6bf9f')
        self.label.setFont(QFont('Times New Roman', 17))

#creates standard buttons
    def create_btns(self):
        for key, variable in calculator_nums.items():
            buttons[key] = {}
            buttons[key]["object_id"] = QPushButton(key,self)
            buttons[key]["object_id"].setGeometry(variable[0],variable[1],58,26)
            buttons[key]["object_id"].setFont(QFont('Times New Roman',15, weight=5000))
            buttons[key]["object_id"].setStyleSheet("color: black; background-color: #f7fffd")

#work in progress trying to create for special cases
            if (len(variable)>2):
                buttons[key]["object_text"] = variable[2]
                buttons[key]["displayed_text"] = variable[3]
            else:
                buttons[key]["object_text"] =  key
                buttons[key]["displayed_text"] = key
                
            #buttons[key]["object_text"] = key
            buttons[key]["x"] = variable[0]
            buttons[key]["y"] = variable[1]
            buttons[key]["object_id"].clicked.connect(partial(self.btn_pressed, buttons[key]["object_text"], buttons[key]["displayed_text"]))

    def btn_pressed(self,object_text,displayed_text):
        self.expr = self.label.text()
        self.expr += object_text
        displayed = self.label.text()
        displayed += displayed_text
        self.label.setText(displayed)
        print(self.expr)
        processed_expr = preprocess_check(self.expr)
        print(processed_expr)

    def enter_pressed(self):
        processed_expr = preprocess_check(self.expr)
        print(processed_expr)
        pass

    

    
    

        

    


            




app = QApplication([])
window = Window()
window.show()
#print("456".isdigit())
#print(preprocess_check('(4)(3)'))
#print(eval('(4)(3)'))
x = "x(6)"
print(preprocess_check(x))
#print(eval("np.sin(3)6"))
sys.exit(app.exec())
