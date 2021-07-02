#!python3
#----TO DO----
#brug regex til at genkende regnetegn og tal (+, -, *, /) og lave do-while hvis et bogstav eller andet tegn er med
# opdel det så get_num, alt det før selve udregningen, er én funktion jeg kun skal skrive én gang uafhængigt af regneformerne
    #-> lære derfor at få variabler med ud af en funktion - måske ved udenfor at have "x = get_num.a"
# lav en DICT med kommandoerne a/s/m/d fra starten, tjek så "hvilken plads har input i listen = hvilken funktion skal kaldes" og "while input not in list"
#gør den i stand til regnestykker med mere end 1 tal
#implementer parenteser


#det med dicten: for int i (i < 4) - if input == calcs[i], call that function
    # sådan her: calc_funcs = {
                                "a": add,
                                "s": subtract,
                                "m": multiply,
                                "d": divide}
          https://stackoverflow.com/questions/41023467/call-functions-from-list-python                          

# Import libraries

import sys
import time

#----FLOW FUNCs----
# Ask for calc type
def ask():
    type = ""
    while type != "p" and type != "m":
        type = input("""Type \"a\" for addition -  \"s\" for subtraction - \"m"\ for
multiplication - "d" for division \n""")
        if type == "a":
            add()
        elif type == "s":
            subtract()
        elif type == "m":
            multiply()
        elif type == "d":
            divide()
        break

def more():
    next = ""
    time.sleep(1)
    while next != "y" and next != "n":
        next = input("Do you want to calculate again? Type y/n \n")
        if next == "y":
            ask()
        else:
            sys.exit()

#----CALC FUNCS----   
# Plus function

def add():
    x = ""
    y = ""
    while not x.isdigit():
        x = input("First number: ")
    while not y.isdigit():
        y = input("Second number: ")
    print(int(x) + int(y))

# Minus function
def subtract():
    x = ""
    y = ""
    while not x.isdigit():
        x = input("First number: ")
    while not y.isdigit():
        y = input("Second number: ")
    print(int(x) - int(y))
    return

# Multiply function
def multiply():
    x = ""
    y = ""
    while not x.isdigit():
        x = input("First number: ")
    while not y.isdigit():
        y = input("Second number: ")
    print(int(x)* int(y))

# Divide function
def divide():
    x = ""
    y = ""
    while not x.isdigit():
        x = input("First number: ")
    while not y.isdigit():
        y = input("Second number: ")
    print(int(x)/ int(y))

# ----MAIN----
ask()
while True:
    more()
