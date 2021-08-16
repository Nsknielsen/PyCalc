#!python3

### IDEER TIL RENERE KODE ###

#Kog de forskellige calculation functions ned til én for at undgå gentagelse i koden.

#Lav de resterende knapper med et loop ved at have en dictionary med par af knaptekst og funktion som: {"CE" : click_ce}. 
    #Kræver 3 elementer i dictionary el. en variabel der undervejs i loopet sænkes under et if-tjeks grænse
    #fordi "="-knappen er større i GUI end de andre.


### IMPORT LIBRARIES ###

import tkinter as tk                #GUI værktøj
import tkinter.font as tkFont       #Ændre skrifttype i GUI
import re                           #Regex til at tjekke input
from functools import partial       #Brugt til at kunne give knapperne en funktion med argumenter igennem et for-loop.



### PYCALC CODE ###

# GLOBAL VARIABLES #                #Regex-tjek anvendes i click_equals() samt i loopet der laver knapper. 
                                            
calc_check = re.compile(r"[\+\-\/\*\%]")
num_check = re.compile(r"[0-9\.]")  # Bruger num_check i stedet for isdigit() for at inkludere "." i tallene i click_equals()

first = True                        #Bruges til at tjekke om brugeren bygger videre på foregående regnestykke eller starter et nyt


# CLICK FUNCTIONS #

def click_calc(c, *args):           # Indsætter/erstatter regnetegn                                                         
    global first
    text = lbl_text["text"]

    if len(text) == 1 and text[-1] == " ":
            text += f"0 {c} " 

    elif num_check.search(text[-1]) and not calc_check.search(text):
            text += f" {c} "
            
    else:
        tlist = list(text)
        for i in range(len(tlist)):
            if calc_check.search(tlist[i]):
                tlist[i] = c
                text = "".join(tlist)
                break
    if not first:
        first = True
    lbl_text["text"] = text

    
def click_num(c, *args):            # Indsætter tal                     
    set_first()
    lbl_text["text"] += c

        
def click_comma(c, *args):          # Indsætter komma og eventuelt foranstående 0.
    set_first()
    text = lbl_text["text"] 
    if num_check.search(text[-1]):
        text += c
    elif text[-1] == ".":
        pass
    else:
        text += f"0{c}"
    lbl_text["text"] = text

def click_equals(*args):             # Aflæser lbl_text og kalder den passende regneform                                
    global first
    try:
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

        calc_options = {'+': add, '-': subtract, '*': multiply, '/': divide, "%": percent}       
        for k in calc_options:          
            if k in calc_choice:
                operation = calc_options[k]              
        lbl_text["text"] = operation(num1, num2)
        first = False
    except:
        pass

    
def click_ce(*args):             # Sletter al text i lbl_text
    lbl_text["text"] = " "


def click_del(*args):            # Sletter sidste tegn i lbl_text
    try:
        if lbl_text["text"][-1] == " ":
            text = lbl_text["text"][:-3]
        else:
            text = lbl_text["text"][:-1]
        lbl_text["text"] = text
    except:
        pass

        
# CALCULATION FUNCTIONS #                   # Regnefunktioner til forskellige regnetyper

def add(x, y):                             
    res = str(round((float(x) + float(y)), 2))
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
    res = res.rstrip("0").rstrip(".") if ".0" in res else res
    return res + "%"


# OTHER FUNCTIONS #

def set_first():                        #Bruges i click_num() og click_comma() til at sætte first = True 
    global first                        #for at vide om brugeren vil bygge videre på det tidligere regnestykke eller ej
    if not first:                       
        click_ce()
        first = True

        
# GUI LAYOUT #

    # Root window and primary frames in grid
root = tk.Tk()                                              # Vindue
root.title("PyCalc")

root.rowconfigure(0, minsize=300, weight=1)
root.columnconfigure(0, minsize=300, weight=1)
root.columnconfigure(1, minsize=250, weight=1)

fr_btns = tk.Frame(root, relief=tk.RAISED, borderwidth=2)   #Ramme til knapper
fr_btns.columnconfigure(5, minsize=20, weight=1)
fr_btns.grid(row=0, column=0, sticky="nsew")

fr_textlbl = tk.Frame(root)                                 #Ramme til tekst
fr_textlbl.grid(row=0, column=1)


    # Set default font
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=15)
root.option_add("TkDefaultFont", default_font)

    
    #Buttons with text-adding functions
list_btns = ["7", "8", "9", "*", "4", "5", "6", "/", "1", "2", "3", "-", "0", ".", "%", "+"]
bnum = 0

for i in range(4):              # Først have jeg én clickfunktion til tekstinput (tal, regnetegn, komma), men den blev meget lang 
    for j in range(4):          # så nu tjekker den knappens tegntype her i stedet (også for kun at gøre det én gang).
        b = list_btns[bnum]
        if b.isdigit():
            com = click_num
        elif calc_check.search(b):
            com = click_calc
        elif b == ".":
            com = click_comma
        btn = tk.Button(fr_btns, text=b, command=partial(com, b), width=5, height=2, cursor="hand2")
        btn.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
        root.bind(b, partial(com, b))
        fr_btns.rowconfigure(i, minsize=20, weight=1)   
        fr_btns.columnconfigure(j, minsize=20, weight=1)
        bnum += 1


    #Buttons with individual functions
btn_ce = tk.Button(fr_btns, text="CE", command=click_ce, width=5, height=2, cursor="hand2")         #CE-knap
btn_ce.grid(row=0, column=5, sticky="nsew")
root.bind("<Delete>", click_ce)

btn_del = tk.Button(fr_btns, text="Del", command=click_del, width=5, height=2, cursor="hand2")      #Slet-knap
btn_del.grid(row=1, column=5, sticky="nsew")
root.bind("<BackSpace>", click_del)
           
btn_equals = tk.Button(fr_btns, text="=", command=click_equals, width=5, height=2, cursor="hand2")  #"="-knap
btn_equals.grid(row=2, column=5, rowspan=2, sticky="nsew")
root.bind("<Return>", click_equals)


    # Text label
lbl_text = tk.Label(fr_textlbl, text=" ", width=10)
lbl_text.config(font=("TkDefaultFont", 20))
lbl_text.grid()

# MAINLOOP#
root.mainloop()
