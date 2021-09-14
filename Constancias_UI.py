# coding=utf-8

from tkinter import *

from spacetools.svg import *
from spacetools.csv import *


#FUNCTIONS ------------------------------------------------------

def findSvg():
	fileDirectionSvg.set(filedialog.askopenfilename(title = "Elegir plantilla", filetypes = (("Archivo SVG", "*.svg"),("Todos los archivos","*.*"))))
	svg = Svg(fileDirectionSvg.get())
	try:
		svg.read()
		infoSvg.set("Archivo encontrado.")
	except:
		infoSvg.set("No se puede abrir el archivo.")

def findCsv():
	fileDirectionCsv.set(str(filedialog.askopenfilename(title = "Elegir csv", filetypes = (("Archivo CSV", "*.csv"),("Todos los archivos","*.*")))))

	csv = Csv(fileDirectionCsv.get())
	csv.read()

	infoCsv.set("{} variables. {} variaciones.".format(csv.varNumber, len(csv.base)))

def findFolder():
	fileDirectionOutput.set(filedialog.askdirectory(title="Elegir ruta de salida"))

def start():


	csv = Csv(fileDirectionCsv.get())
	csv.read()

	nombre = formatOutput.get()

	for i in csv.base:
		print(i)
		template = Svg(fileDirectionSvg.get())
		template.read()
		template.personalize(csv.header, i)
		auxname = nombre
		for j in range(len(csv.header)):
			auxname = auxname.replace(csv.header[j], i[j])
		if pdfOutput.get() == 1:
			template.savePdf(fileDirectionOutput.get()+"/"+auxname)
		else:
			template.save(fileDirectionOutput.get()+"/"+auxname)
		del(template)




#ROOT ------------------------------------------------------

root = Tk()

root.title("Space Tools")
root.resizable(0,0)

frameLeft = Frame(root)
frameLeft.config(width=400, height=600, bg = "#1e303e")
frameLeft.grid(column=0, row=1)

frameRight = Frame(root)
frameRight.config(width=400, height=600, bg = "#ffffff")
frameRight.grid(column=1, row=1)

#VARIABLES------------------------------------------------------

fileDirectionCsv = StringVar()
fileDirectionSvg = StringVar()
fileDirectionOutput = StringVar()

infoCsv = StringVar()
infoSvg = StringVar()

formatOutput = StringVar()

pdfOutput = IntVar()

#LEFT FRAME ------------------------------------------------------

logo = PhotoImage(file="images/logo.png")
Label(frameLeft, image = logo, bd=0).place(x=29,y=22)

Label(frameLeft, text= "Bienvenido al asistente", font = ("Montserrat 16 bold"), bg = "#1e303e", fg="#ffffff").place(x=50, y=190)

separador1 = PhotoImage(file="images/separador1.png")
Label(frameLeft, image = separador1, bd=0).place(x=60,y=230)

Label(frameLeft, text= "Cree documentos en serie utilizando\nuna plantilla y una base de datos.\n\nUtilice una plantilla en formato Svg y\nuna base de datos en formato Csv.", font = ("Montserrat 10"), bg = "#1e303e", fg="#f1f1f0", justify="left").place(x=50, y=250)

Button(frameLeft, text="¿Cómo utilizar?",
	bg = "#1e303e", fg="#dfa131", bd=0, state = "normal",highlightthickness=0, highlightbackground = "#1e303e",
	font = ("Montserrat 8"), justify="left").place(x=50,y=370)

#RIGHT FRAME ------------------------------------------------------

Label(frameRight, font = "Montserrat 12 bold", text = "Base de datos CSV", bg = "white", fg="#1c2125").place(x=40,y=30)

Entry(frameRight, font = "Montserrat 10", bg = "#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
	borderwidth=10, relief=FLAT, textvariable=fileDirectionCsv).place(x=40,y=60)

imageButton = PhotoImage(file="images/boton.png")
Button(frameRight, font = ("Montserrat", 14), image = imageButton, command = findCsv,
	bg = "#ffffff", fg="#dfa131", bd=0, highlightthickness=0).place(x=320,y=75)

Label(frameRight, font = "Montserrat 10", textvariable = infoCsv, bg = "white", fg="#7b7b7e").place(x=40,y=100)

#.----------------------------------
Label(frameRight, font = "Montserrat 12 bold", text = "Plantilla SVG", bg = "white", fg="#1c2125").place(x=40,y=130)

Entry(frameRight, font = "Montserrat 10", bg = "#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
	borderwidth=10, relief=FLAT, textvariable=fileDirectionSvg).place(x=40,y=160)

Button(frameRight, font = ("Montserrat", 14), image = imageButton, command = findSvg,
	bg = "#ffffff", fg="#dfa131", bd=0, highlightthickness=0).place(x=320,y=175)

Label(frameRight, font = "Montserrat 10", textvariable = infoSvg, bg = "white", fg="#7b7b7e").place(x=40,y=200)

#.----------------------------------
Label(frameRight, font = "Montserrat 12 bold", text = "Opciones", bg = "white", fg="#1c2125").place(x=40,y=230)

Checkbutton(frameRight, text="Exportar en Pdf", font = "Montserrat 10",
	bg = "#ffffff", fg="#1c2125", bd=0, highlightthickness=0, height=2,
	variable=pdfOutput, onvalue=1, offvalue=0).place(x=40,y=260)

#.----------------------------------
separador2 = PhotoImage(file="images/separador2.png")
Label(frameRight,image = separador2, bd=0).place(x=40, y=320)
#.----------------------------------
Label(frameRight, font = "Montserrat 12 bold", text = "Ruta de salida", bg = "white", fg="#1c2125").place(x=40,y=330)

Entry(frameRight, font = "Montserrat 10", bg = "#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
	borderwidth=10, relief=FLAT, textvariable=fileDirectionOutput).place(x=40,y=360)

Button(frameRight, font = ("Montserrat", 14), image = imageButton, command = findFolder,
	bg = "#ffffff", fg="#dfa131", bd=0, highlightthickness=0).place(x=320,y=375)

#.----------------------------------
Label(frameRight, font = "Montserrat 12 bold", text = "Formato de nombre de salida", bg = "white", fg="#1c2125").place(x=40,y=430)

Entry(frameRight, font = "Montserrat 10", bg = "#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
	borderwidth=10, relief=FLAT, textvariable=formatOutput).place(x=40,y=460)

#.----------------------------------
Button(frameRight, font = "Montserrat 12 bold", text = "Iniciar",
	bg = "#3873b5", fg="#ffffff", bd=0, highlightthickness=0, width=12,borderwidth=5,relief=FLAT,
	command = start).place(x= 200, y=520)

root.mainloop()
