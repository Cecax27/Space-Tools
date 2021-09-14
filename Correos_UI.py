from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from spacetools.svg import *
from spacetools.csv import *
from spacetools.html import *


#FUNCTIONS ------------------------------------------------------

def login():

	global rootLogin
	rootLogin = Toplevel(root)
	rootLogin.title("Iniciar sesión")
	rootLogin.resizable(0, 0)

	frameLogin = Frame(rootLogin)
	frameLogin.config(width=400, height=400, bg="#1e303e")
	frameLogin.pack()

	Label(frameLogin, text="Iniciar sesión", font=("Montserrat 16 bold"),
            bg="#1e303e", fg="#ffffff", justify="center").place(x=200, y=50, anchor="n")

	Label(frameLogin, text="Correo electrónico", font=("Montserrat 12 bold"),
            bg="#1e303e", fg="#ffffff", justify="center").place(x=200, y=120, anchor="n")

	Entry(frameLogin, font="Montserrat 12", bg="#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
            borderwidth=10, relief=FLAT, textvariable=email, justify="center").place(x=200, y=150, anchor="n")

	Label(frameLogin, text="Contraseña", font=("Montserrat 12 bold"),
            bg="#1e303e", fg="#ffffff", justify="center").place(x=200, y=220, anchor="n")

	Entry(frameLogin, font="Montserrat 12", bg="#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
            borderwidth=10, relief=FLAT, textvariable=password, justify="center", show="*").place(x=200, y=250, anchor="n")

	Button(frameLogin, font="Montserrat 12 bold", text="Entrar",
            bg="#dfa131", fg="#ffffff", bd=0, highlightthickness=0, width=12, borderwidth=5, relief=FLAT,
            command=loginEntry, justify="center").place(x=200, y=320, anchor="n")

	rootLogin.mainloop()


def loginEntry():
	rootLogin.destroy()
	loginButton.set("Cambiar cuenta")


def findHtml():

	fileDirectionHtml.set(filedialog.askopenfilename(title="Elegir plantilla", filetypes=(
		("Archivo HTML", "*.html"), ("Todos los archivos", "*.*"))))
	html = Html(fileDirectionHtml.get())
	try:
		html.read()
		infoHtml.set("Archivo encontrado.")
	except:
		infoHtml.set("No se puede abrir el archivo.")


def findCsv():
	fileDirectionCsv.set(str(filedialog.askopenfilename(title="Elegir csv", filetypes=(
		("Archivo CSV", "*.csv"), ("Todos los archivos", "*.*")))))

	csv = Csv(fileDirectionCsv.get())
	csv.read()

	infoCsv.set("{} variables. {} variaciones.".format(
		csv.varNumber, len(csv.base)))


def findFolder():
	fileDirectionOutput.set(
		filedialog.askdirectory(title="Elegir ruta de salida"))


def start():

	#Check if the login is done
	if email.get() == "" or password.get() == "":
		messagebox.showerror(title="Error", message="No ha iniciado sesión")
		return False

	#read the csv
	global csv
	csv = Csv(fileDirectionCsv.get())

	try:
		csv.read()
	except FileExistsError:
		messagebox.showerror(title="Error", message="No hay archivo CSV")
		return False

	#read the Html
	try:
		html = Html(fileDirectionHtml.get())
		html.read()
	except FileExistsError:
		messagebox.showerror(title="Error", message="No hay archivo HTML")
		return False

	#Check the subject
	if subject.get() == "":
		messagebox.showerror(title="Error", message="Inserte un asunto")
		return False

	#Check the adress
	if toAdress.get() == "":
		messagebox.showerror(title="Error", message="Inserte una dirección de envío")
		return False

	global ammountMails
	ammountMails = len(csv.base)

	global rootSending
	rootSending = Toplevel(root)
	rootSending.title("Enviando correos")
	rootSending.resizable(0, 0)

	global display
	display = StringVar(rootSending)

	if ammountMails > 1:
		display.set("Se enviarán {} correos".format(ammountMails))
	else:
		display.set("Se enviará {} correo".format(ammountMails))

	global frameSending
	frameSending = Frame(rootSending)
	frameSending.config(width=500, height=300, bg="#1e303e")
	frameSending.pack()

	Label(frameSending, textvariable=display, font=("Montserrat 16 bold"),
            bg="#1e303e", fg="#ffffff", justify="center").place(x=250, y=90, anchor="n")

	Button(frameSending, font="Montserrat 12 bold", text="Cancelar",
            bg="#7b7b7e", fg="#ffffff", bd=0, highlightthickness=0, width=12, borderwidth=5, relief=FLAT,
            command=cancel, justify="center").place(x=240, y=160, anchor="e")

	Button(frameSending, font="Montserrat 12 bold", text="Iniciar",
            bg="#3873b5", fg="#ffffff", bd=0, highlightthickness=0, width=12, borderwidth=5, relief=FLAT,
            command=accept, justify="center").place(x=260, y=160, anchor="w")

	rootSending.mainloop()


def accept():

	global frameSending
	frameSending.destroy()

	global displaySecond
	global displayThird
	displaySecond = StringVar(rootSending)
	displayThird = StringVar(rootSending)

	global display
	display.set("Enviando correos")

	frameSending = Frame(rootSending)
	frameSending.config(width=500, height=300, bg="#1e303e")
	frameSending.pack()

	Label(frameSending, textvariable=display, font=("Montserrat 16 bold"),
            bg="#1e303e", fg="#ffffff", justify="center").place(x=250, y=90, anchor="n")

	Label(frameSending, textvariable=displaySecond, font=("Montserrat 12"),
            bg="#1e303e", fg="#ffffff", justify="center").place(x=250, y=170, anchor="n")

	Label(frameSending, textvariable=displayThird, font=("Montserrat 12"),
            bg="#1e303e", fg="#dfa131", justify="center").place(x=250, y=200, anchor="n")

	root.after(1, send)


def send():
	global ammountMails
	global csv
	global displaySecond
	global displayThird
	for x in range(ammountMails):
		actualAdress = toAdress.get()

		for y in range(len(csv.header)):
			actualAdress = actualAdress.replace(
				csv.header[y], csv.base[x][y])

		displaySecond.set("Enviando a {}".format(actualAdress))
		displayThird.set("{}/{}".format(x+1, ammountMails))

		sendOne(csv.base[x], actualAdress)


def sendOne(values, toAdress):

	template = Html(fileDirectionHtml.get())

	template.read()

	template.personalize(csv.header, values)

	newEmail = Mail(template, toAdress)

	newEmail.login(email.get(), password.get())

	#newEmail.attachPdf(i[5]+".pdf")

	thissubject = subject.get()

	for x in range(len(values)):
		thissubject = thissubject.replace(csv.header[x], values[x])

	newEmail.send(thissubject)

	print("Se envió un correo a "+toAdress)


def cancel():

	rootSending.destroy()


#ROOT ------------------------------------------------------

root = Tk()

root.title("Space Tools")
root.resizable(0, 0)

frameLeft = Frame(root)
frameLeft.config(width=400, height=800, bg="#1e303e")
frameLeft.grid(column=0, row=1)

frameRight = Frame(root)
frameRight.config(width=400, height=800, bg="#ffffff")
frameRight.grid(column=1, row=1)

#VARIABLES------------------------------------------------------

#file directions
fileDirectionCsv = StringVar()
fileDirectionHtml = StringVar()
fileDirectionOutput = StringVar()

#account info
email = StringVar()
password = StringVar()

#mail info
subject = StringVar()
toAdress = StringVar()

#labels
loginButton = StringVar()
loginButton.set("Iniciar sesión")
infoCsv = StringVar()
infoHtml = StringVar()

pdfOutput = IntVar()

#LEFT FRAME ------------------------------------------------------

logo = PhotoImage(file="images/logo.png")
Label(frameLeft, image=logo, bd=0).place(x=30, y=30)

Label(frameLeft, text="Bienvenido al asistente", font=(
	"Montserrat 16 bold"), bg="#1e303e", fg="#ffffff").place(x=50, y=260)

separador1 = PhotoImage(file="images/separador1.png")
Label(frameLeft, image=separador1, bd=0).place(x=60, y=290)

Label(frameLeft, text="""Envie correos electrónicos
personalizados.

Utilice una base de datos Csv y una
plantilla Html. También puede adjuntar
archivos Pdf.""", font=("Montserrat 10"), bg="#1e303e", fg="#f1f1f0", justify="left").place(x=50, y=320)

Button(frameLeft, text="¿Cómo utilizar?",
       bg="#1e303e", fg="#dfa131", bd=0, state="normal", highlightthickness=0, highlightbackground="#1e303e",
       font=("Montserrat 8"), justify="left").place(x=50, y=440)

#RIGHT FRAME ------------------------------------------------------

Button(frameRight, font="Montserrat 12 bold", textvariable=loginButton,
       bg="#a9aaab", fg="#ffffff", bd=0, highlightthickness=0, width=12, borderwidth=5, relief=FLAT,
       command=login).place(x=40, y=40)

#.----------------------------------

Label(frameRight, font="Montserrat 12 bold", text="Base de datos CSV",
      bg="white", fg="#1c2125").place(x=40, y=120)

Entry(frameRight, font="Montserrat 10", bg="#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
      borderwidth=10, relief=FLAT, textvariable=fileDirectionCsv).place(x=40, y=150)

imageButton = PhotoImage(file="images/boton.png")
Button(frameRight, font=("Montserrat", 14), image=imageButton, command=findCsv,
       bg="#ffffff", fg="#dfa131", bd=0, highlightthickness=0).place(x=320, y=175)

Label(frameRight, font="Montserrat 10", textvariable=infoCsv,
      bg="white", fg="#7b7b7e").place(x=40, y=190)

#.----------------------------------
Label(frameRight, font="Montserrat 12 bold", text="Plantilla HTML",
      bg="white", fg="#1c2125").place(x=40, y=240)

Entry(frameRight, font="Montserrat 10", bg="#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
      borderwidth=10, relief=FLAT, textvariable=fileDirectionHtml).place(x=40, y=270)

Button(frameRight, font=("Montserrat", 14), image=imageButton, command=findHtml,
       bg="#ffffff", fg="#dfa131", bd=0, highlightthickness=0).place(x=320, y=285)

Label(frameRight, font="Montserrat 10", textvariable=infoHtml,
      bg="white", fg="#7b7b7e").place(x=40, y=310)

#.----------------------------------
Button(frameRight, font="Montserrat 12 bold", text="Adjuntar PDF",
       bg="#dfa131", fg="#ffffff", bd=0, highlightthickness=0, width=12, borderwidth=5, relief=FLAT,
       command=start).place(x=40, y=350)
#.----------------------------------

separador2 = PhotoImage(file="images/separador2.png")
Label(frameRight, image=separador2, bd=0).place(x=40, y=420)

#.----------------------------------
Label(frameRight, font="Montserrat 12 bold", text="Asunto",
      bg="white", fg="#1c2125").place(x=40, y=450)

Entry(frameRight, font="Montserrat 10", bg="#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
      borderwidth=10, relief=FLAT, textvariable=subject).place(x=40, y=480)

#.----------------------------------
Label(frameRight, font="Montserrat 12 bold", text="Dirección de envío",
      bg="white", fg="#1c2125").place(x=40, y=540)

Entry(frameRight, font="Montserrat 10", bg="#f1f1f0", fg="#1c2125", bd=0, width=28, highlightthickness=0,
      borderwidth=10, relief=FLAT, textvariable=toAdress).place(x=40, y=570)

#.----------------------------------
Button(frameRight, font="Montserrat 12 bold", text="Iniciar",
       bg="#3873b5", fg="#ffffff", bd=0, highlightthickness=0, width=12, borderwidth=5, relief=FLAT,
       command=start).place(x=200, y=730)

root.mainloop()
