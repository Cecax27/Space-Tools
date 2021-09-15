"""
Main file in the module
"""

from tkinter import *


def initGui(moduleFrame):  # Main gui calls this function
    print("Certificates say hi")

    Label(moduleFrame, text="Certificados", font=(
    	"Montserrat 32 bold"), bg="#ffffff", fg="#dfa131", justify="center").place(x=500, y=30, anchor="n")


def getModule():  # Returns the info to build the button
    return "Constancias"
