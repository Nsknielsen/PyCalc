#!python3

#----TO DO----

#PRIORITY
#figure out why it won't calculate again / how to clear
        #the problem is in skipping the "if not first" block
# gør lbl_res[text] til den nye num1 efter første regning, medminder "ce" klikkes
# gør teksten på lbl_res større


    #----SMOOTHER CODE----
    #later turn num1, calc, num2 into indexes in calculation[] (learn to build string in a list)
    # make calc funcs "return" res and have just one line for updating it somewhere?
    
    #EKSTRA:
    #make gui resizable same way as the realpython tkinter example of text editor
    #make an if gate in click() for scenarios like second calc type clicked (float or int?), and for "," with digit before it
                #(check last index in lbl_res["text"] before reacting to btns)
    #forbind keystrokes til knapper (gerne ét sted - måske kan tk events håndtere keystrokes?)

    #BONUS CALCULATION FUNCTIONALITY
    #implementer at gå tilbage/fortryde med ce

#VERSION 2 - Object-Oriented
   #learn about OOP and make this program OO


### IMPORT LIBS ###

import tkinter as tk
import re
from functools import partial


### CODE ###

# CLICK FUNCTION #
def click(c):               
    first = True
    if not first:
       lbl_res.config(text="")
    calc_check = re.compile(r"[\+\-\/\*]")
    num_check = re.compile(r"[0-9\,]")
    calc_options = {'+': add, '-': subtract, '*': multiply, '/': divide}
    if calc_check.search(c):                   
        lbl_res["text"] += f" {c} "     
    elif c.isdigit():                     
        lbl_res["text"] += c                
    elif c == "=":                          
        raw_input = lbl_res["text"]     
        num1 = ""
        calc_choice = ""
        num2 = ""
        for a in raw_input:
            if num_check.search(a):
                num1 += a
            elif calc_check.search(a):
                calc_choice += a
                calc_index = raw_input.index(a)
                break
        for a in raw_input[calc_index:]:
            if num_check.search(a):
                num2 += a
        for k in calc_options:
            if k in calc_choice:
                calculation = calc_options[k]
        calculation(num1, num2)
    first = False
    
# CALC FUNCS #
def add(x, y):
    lbl_res["text"] = str((int(x) + int(y)))

def subtract(x, y):
    lbl_res["text"] = str((int(x) - int(y)))  

def multiply(x, y):
    lbl_res["text"] = ((int(x) * int(y)))
    
def divide(x, y):
    lbl_res["text"] = ((int(x) / int(y)))



# GUI LAYOUT #

    # Root and frames
root = tk.Tk()
root.title("PyCalc")
fr_btns = tk.Frame(root, relief=tk.RAISED, borderwidth=2)
fr_res = tk.Frame(root, borderwidth=2)

    #Buttons
list_btns = ["7", "8", "9", "*", "4", "5", "6", "/", "1", "2", "3", "-", "0", ",", "=", "+"]

bnum = 0
for i in range(4):
    for j in range(4):
        btn = tk.Button(fr_btns, text=list_btns[bnum], command=partial(click, list_btns[bnum]), width=5, height=2, cursor="hand2")
        btn.grid(row=i, column=j)
        bnum += 1

    # Result label
lbl_res = tk.Label(fr_res, width=10)
lbl_res.grid()

    # Placing frames in root
fr_btns.grid(row=0, column=0, sticky="ns")
fr_res.grid(row=0, column=1)

# MAINLOOP #
root.mainloop()
