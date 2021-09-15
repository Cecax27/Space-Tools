"""
This is the main file
"""

from tkinter import *

from modules.certificates import InitGui as certificates
from modules.mailer import InitGui as mailer


def mainGui():  # Start the app gui
    #ROOT ------------------------------------------------------
    global root
    root = Tk()

    root.title("Space Tools")
    root.resizable(0, 0)

    global frame
    frame = Frame(root)
    frame.config(width=280, height=800, bg="#1e303e")
    frame.grid(column=0, row=0)

    global moduleFrame
    moduleFrame = Frame(root)

    createModuleFrame()

    loadModules()

    root.mainloop()


def createModuleFrame():
    global moduleFrame

    moduleFrame = Frame(root)
    moduleFrame.config(width=1000, height=800, bg="#ffffff")
    moduleFrame.grid(column=1, row=0)


def loadModules():  # Put the modules into the gui
    print("Cargando modulos")
    createModuleButton(certificates.getModule(), loadCertificates)
    createModuleButton(mailer.getModule(), loadMailer)


def createModuleButton(textLabel, function):
    global moduleCount
    global frame

    Button(frame, font="Montserrat 12 bold", text=textLabel,
           bg="#3873b5", fg="#ffffff", bd=0, highlightthickness=0, width=12, borderwidth=5, relief=FLAT,
           command=function).place(x=50, y=moduleCount*60+30)
    moduleCount += 1
#-------------MODULES----------------------


def loadCertificates():  # Action when click on Certificates
    createModuleFrame()
    global moduleFrame
    certificates.initGui(moduleFrame)


def loadMailer():  # Action when click on Mailer
    createModuleFrame()
    global moduleFrame
    mailer.initGui(moduleFrame)


moduleCount = 0
mainGui()
