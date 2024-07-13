import numpy as np
import math as math
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel
import sys 
from PyQt6.QtGui import QIcon, QFont
from functools import partial
from PyQt6.QtCore import Qt
from libraries import buttons



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
#some variables
        self.n=0
        self.new_line_text = ""
        self.hidden_text = ""
#list of buttons/text
        self.buttons = []
        self.prim_text = []
        self.sec_text = []
#making buttons 
        #self.mk_button("Sto>", 10,528)
        self.mk_button("0",78,564)
        self.mk_button(".",146,564)
        self.mk_button("1", 78,528)
        self.mk_button("2", 146,528)
        self.mk_button("3",214,528)
        self.mk_button("4", 78,492)
        self.mk_button("5", 146,492)
        self.mk_button("6", 214,492)
        self.mk_button("7", 78,456)
        self.mk_button("8", 146,456)
        self.mk_button("9",214,456)
        self.mk_button("(", 146,420,'#303332', 13, 5000, "white")
        self.mk_button(")",214,420, '#303332', 13, 5000, "white")
        self.mk_button("^",282,384,'#303332', 15, 5000, "white","π" )
        self.mk_button("2nd",10,276,'#788b9c', 10, 551, "white")
        self.mk_button("SIN", 78,384,'#303332', 11, 5000, "white")
        self.mk_button("COS", 146,384,'#303332', 11, 5000, "white")
        self.mk_button("TAN",214,384, '#303332', 11, 5000, "white")

        

#MDAS
        self.mk_button("+",282,528, '#A9A7A7', 18)
        self.mk_button("-",282,492, '#A9A7A7',20)
        self.mk_button("*",282,456, '#A9A7A7', 18)
        self.mk_button("/",282,420, '#A9A7A7',20)
#CLEAR/ENTER
        self.mk_button("ENTER",282,564,'#A9A7A7', 10, 551, "black", "ENTER")
        self.mk_button("CLEAR",282,348,'#303332', 10, 551, "white", "CLEAR")
#add screen
        self.create_widgets()

    

    def mk_button(self,prim_text, x , y, color ='#f7fffd', font = 15, weight_num = 5000, text_color = "black", sec_text = ""):
        self.btn = QPushButton(prim_text,self)
        self.btn.setGeometry(x,y,58,26)
        self.btn.setFont(QFont('Times New Roman',font, weight=weight_num))
        self.btn.setStyleSheet("color: " +text_color + "; background-color: "+color)
        self.buttons.append(self.btn)
        self.prim_text.append(prim_text)
        self.sec_text.append(sec_text)
        self.btn.clicked.connect(partial(self.clicked_button,prim_text, sec_text))




    def create_widgets(self):
        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label.setIndent(10)
        self.label.setGeometry(10,10,330,184)
        self.label.setStyleSheet('background-color:#a6bf9f')
        self.label.setFont(QFont('Times New Roman', 17))
    
    def clicked_button(self,something, second_something):
        current_text = self.label.text()

#config to put calculator back to standard buttons
        if something == "2nd" and self.n == 1:
             self.n = 0
             for i in range(len(self.buttons)):
                self.buttons[i].setText(self.prim_text[i])
             
#config to put calculator into 2nd
        elif something == "2nd" and self.n == 0:
             self.n =1
             
             for i in range(len(self.buttons)):
                self.buttons[i].setText(self.sec_text[i])

#config for ENTER/CLEAR
        elif something == "ENTER":
            self.new_line_text= str(eval(self.hidden_text))
            self.label.setText(current_text + "\n" + self.new_line_text + "\n")
            self.hidden_text = ""
        elif something == "CLEAR":
             current_text = ""
             self.new_line_text = ""
             self.hidden_text = ""
             self.label.setText(current_text)
#config for standard calculator
        elif something != "2nd" and self.n==0:
#config for ASDM
                if something == "+" or something == "-" or something == "/" or something == "*":
                    current_text = current_text + self.new_line_text 
                    self.hidden_text = self.hidden_text + self.new_line_text 
                    self.label.setText(current_text+something)
                    self.hidden_text = self.hidden_text + something
#config for sin, cos, tan multiplied by an int/symbol
                elif len(current_text) > 0 and (something == "SIN" or something == "COS" or something == "TAN") and (current_text[-1].isdigit() or current_text[-1] == "π"):
                    self.hidden_text = self.hidden_text + "*np." + something.lower() + "("
                    self.label.setText(current_text+ something.lower() + "(")
#config for sin, cos, tan 
                elif something == "SIN" or something == "COS" or something == "TAN":
                    self.hidden_text = self.hidden_text + "np." + something.lower() + "("
                    self.label.setText(current_text+ something.lower() + "(")
#config for parenthesis/symbols (including with multiplication) [EX: (9)4, π4, 4π, 4(9), (4)(5)]
                elif len(current_text) > 0 and something == "(" and (current_text[-1].isdigit() or current_text[-1] == "π" or current_text[-1] == ")") or len(current_text) > 0 and something.isdigit() and (current_text[-1] == ")" or current_text[-1] == "π"): 
                     self.hidden_text = self.hidden_text + "*" + something
                     self.label.setText(current_text+something)
#config for everything else
                else:
                    self.label.setText(current_text+something)
                    self.hidden_text = self.hidden_text + something
                self.new_line_text = ""
                print(self.hidden_text)
                
                
#config for calculator in 2nd
        elif something != "2nd" and self.n ==1:
#config for multiplying something by π [EX: 9π] or parenthesis [EX: (9)π]
            if len(current_text) > 0 and second_something == "π" and current_text[-1].isdigit() or len(current_text) > 0 and second_something == "π" and current_text[-1] == ")":
                self.label.setText(current_text+second_something)
                self.hidden_text = self.hidden_text + "*np.pi"
                self.new_line_text = ""
                print(self.hidden_text)
#config for π (not direct multiplication)
            elif second_something == "π":
                self.label.setText(current_text+second_something)
                self.hidden_text = self.hidden_text + "np.pi"
                self.new_line_text = ""
                print(self.hidden_text)
#config for everything else
            else:
                self.label.setText(current_text+second_something)
                self.hidden_text = self.hidden_text + second_something
                self.new_line_text = ""
                print("helllllo")
                

x = "(4)*4"
print(eval(x))
app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())


