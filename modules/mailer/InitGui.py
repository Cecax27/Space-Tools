"""
Main file in the module
"""

from tkinter import *


def initGui(moduleFrame):  # Main gui calls this function
    print("Mailer say hi")

    Label(moduleFrame, text="Correos", font=(
    	"Montserrat 32 bold"), bg="#ffffff", fg="#dfa131", justify="center").place(x=500, y=30, anchor="n")


def getModule():  # Returns the info to build the button
    return "Correos"
