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
    expr = re.sub(r'([a-zA-Z])(\()', r'\1*(', expr)
    #inserts * between parenthesis
    expr = re.sub(r'(\))(\()', r'\1*(', expr)
    
    return(expr)


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
        self.create_btns()

    def create_btns(self):
        for key, variable in calculator_nums.items():
            buttons[key] = {}
            buttons[key]["object_id"] = QPushButton(key,self)
            buttons[key]["object_id"].setGeometry(variable[0],variable[1],58,26)
            buttons[key]["object_id"].setFont(QFont('Times New Roman',15, weight=5000))
            buttons[key]["object_id"].setStyleSheet("color: black; background-color: #f7fffd")
            buttons[key]["object_text"] = key
            buttons[key]["x"] = variable[0]
            buttons[key]["y"] = variable[1]

    


            




app = QApplication([])
window = Window()
window.show()
print(preprocess_check('(4)(3)'))
#print(eval('(4)(3)'))
sys.exit(app.exec())
