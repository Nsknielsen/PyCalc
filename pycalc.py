#!python3

#----TO DO----

#CORE FUNCTIONALITY

    #figure out how to clear after a calculation and save the cleared text to past_res, then each time in click_equals check if past_res
        # call click_ce to recycle code
        #this works best if i distinguish between C and CE (clear current + memory vs. clear current)
    # add "0" prior to calc sign if calc sign is first entry (this conflicts with above memory implementation,
        #maybe do it in click_equals instead with try except and adding 0)

# ERROR HANDLING
    #handle sequences like "5 + 3 - 2" with multiple calc signs - like windows calc make it call click_equals in that case, and add the final calc sign to text?

#SMOOTHER CODE:
    # to make click_regular function less messy (should do 1 thing), turn btn_list into a dictionary with "sign : function" like "1: click_num"
            # just needs to split into num, calc, comma
    #MAYBE ONE DICT JUST? also make a dict for just the 3 special buttons to make those in loop too (with the attributes sign, function, rowspan)

    # maybe use formatting like f"" to turn the 4 basic calc funcs into one that reads its calc sign from lbl_text

#EXTRA DETAILS
    # expand window when lbl_text gets too big for it OR move unto next line (multiline label how?)
            

### IMPORT LIBS ###

import tkinter as tk
import tkinter.font as tkFont
import re
from functools import partial


### CODE ###

# CLICK FUNCTIONS #

def click_regular(c, *args):               # Reacts to text input depending on type                                                      
    text = lbl_text["text"]
    if calc_check.search(c):
        if num_check.search(text[-1]) and calc_check.search(text):
            click_equals()
        elif num_check.search(text[-1]):
            text += f" {c} " 
        else:
            text = lbl_text["text"][:-3]
            text += f" {c} "
            
    elif c.isdigit():                     
        text += c
        
    elif c == ".":
        if num_check.search(text[-1]):
            text += c
        elif text[-1] == ".":
            pass
        else:
            text += f"0{c}"

    lbl_text["text"] = text

def click_equals(*args):             # Finds num1 + num2 + calculation type and calculates                                    
    try:
        calc_options = {'+': add, '-': subtract, '*': multiply, '/': divide, "%": percent}
        text = lbl_text["text"]     
        num1 = ""
        calc_choice = ""
        num2 = ""
        for c in text:
            if num_check.search(c):
                num1 += c
            elif calc_check.search(c):
                calc_choice += c
                calc_index = text.index(c)
                break
        for c in text[calc_index:]:
            if num_check.search(c):
                num2 += c
        for k in calc_options:
            if k in calc_choice:
                operation = calc_options[k]
        s = operation(num1, num2)
        lbl_text["text"] = s
        past_res.append(lbl_text["text"])               # Edited to have memory of past_res, now how to make it use that in calculations?
        print(past_res)
    except:
        pass
    
def click_ce(*args):             # Deletes all text
    lbl_text["text"] = " "
    
def click_del(*args):            # Deletes last character of text
    try:
        if lbl_text["text"][-1] == " ":
            text = lbl_text["text"][:-3]
        else:
            text = lbl_text["text"][:-1]
        lbl_text["text"] = text
    except:
        pass

        
# CALC FUNCTIONS #

def add(x, y):
    res = str(round((float(x) + float(y)), 2))
    print("k")
    return res.rstrip("0").rstrip(".") if ".0" in res else res
    

def subtract(x, y):
    res = str(round((float(x) - float(y)), 2))
    return res.rstrip("0").rstrip(".") if ".0" in res else res

def multiply(x, y):
    res = str(round((float(x) * float(y)), 2))
    return res.rstrip("0").rstrip(".") if ".0" in res else res

def divide(x, y):
    res = str(round((float(x) / float(y)), 2))
    return res.rstrip("0").rstrip(".") if ".0" in res else res

def percent(x, y):
    res = str(round(((float(x) / float(y) * 100)), 2))
    return res.rstrip("0").rstrip(".") if ".0" in res else res


# GUI LAYOUT #

    # Root and frames
root = tk.Tk()
root.title("PyCalc")
fr_btns = tk.Frame(root, relief=tk.RAISED, borderwidth=2)
fr_textlbl = tk.Frame(root)

root.rowconfigure(0, minsize=300, weight=1)
root.columnconfigure(0, minsize=300, weight=1)
root.columnconfigure(1, minsize=250, weight=1)

    # Set default font
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=15)
root.option_add("TkDefaultFont", default_font)

def printit(*args):
    print("yes")
    
    #Buttons with click_regular function
list_btns = ["7", "8", "9", "*", "4", "5", "6", "/", "1", "2", "3", "-", "0", ".", "%", "+"]
bnum = 0

for i in range(4):
    for j in range(4):
        btn = tk.Button(fr_btns, text=list_btns[bnum], command=partial(click_regular, list_btns[bnum]), width=5, height=2, cursor="hand2")
        btn.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
        root.bind(list_btns[bnum], partial(click_regular, list_btns[bnum]))
        fr_btns.rowconfigure(i, minsize=20, weight=1)   
        fr_btns.columnconfigure(j, minsize=20, weight=1)
        bnum += 1

    #Buttons with individual functions
btn_ce = tk.Button(fr_btns, text="CE", command=click_ce, width=5, height=2, cursor="hand2")
btn_ce.grid(row=0, column=5, sticky="nsew")
root.bind("<Delete>", click_ce)

btn_del = tk.Button(fr_btns, text="Del", command=click_del, width=5, height=2, cursor="hand2")
btn_del.grid(row=1, column=5, sticky="nsew")
root.bind("<BackSpace>", click_del)

btn_equals = tk.Button(fr_btns, text="=", command=click_equals, width=5, height=4, cursor="hand2")
btn_equals.grid(row=2, column=5, rowspan=2, sticky="nsew")
root.bind("<Return>", click_equals)

    # Text label
lbl_text = tk.Label(fr_textlbl, text=" ", width=7)
lbl_text.config(font=("TkDefaultFont", 20))
lbl_text.grid()

    # Gridding frames in root
fr_btns.columnconfigure(5, minsize=20, weight=1)
fr_btns.grid(row=0, column=0, sticky="nsew")
fr_textlbl.grid(row=0, column=1)


# MAINLOOP AND GLOBALS #
past_res = []                       #Not in use until memory is implemented
calc_check = re.compile(r"[\+\-\/\*\%]")
num_check = re.compile(r"[0-9\.]") # Used instead of .isdigit() to include "."
root.mainloop()
