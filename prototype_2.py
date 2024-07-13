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
'''
window = tk.Tk()

window.geometry("350x600")

icon = Image.open('calculator.png')
photo = ImageTk.PhotoImage(icon)
window.wm_iconphoto(False, photo)


for key, variable in calculator_nums.items():
    buttons[key] = tk.Button(window, text = key,height = 3)
    buttons[key].place(x=variable[0],y=variable[1])
'''

''''
self.btn = QPushButton(prim_text,self)
self.btn.setGeometry(x,y,58,26)
        self.btn.setFont(QFont('Times New Roman',font, weight=weight_num))
        self.btn.setStyleSheet("color: " +text_color + "; background-color: "+color)
        self.buttons.append(self.btn)
        self.prim_text.append(prim_text)
        self.sec_text.append(sec_text)
        self.btn.clicked.connect(partial(self.clicked_button,prim_text, sec_text))
'''''

#window.mainloop()

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
            buttons[key] = QPushButton(key,self)
            buttons[key].setGeometry(variable[0],variable[1],58,26)
            buttons[key].setFont(QFont('Times New Roman',15, weight=5000))
            buttons[key].setStyleSheet("color: black; background-color: #f7fffd")




app = QApplication([])
window = Window()
window.show()
print(buttons)
sys.exit(app.exec())
