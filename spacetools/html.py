from io import open

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class Html:

	def __init__(self, file_name):
		self.file_name = file_name
		self.__content = ""


	def read(self):
		#Check if the file is a .html
		if not self.__isHtmlFile():
			raise FileExistsError ("The file is not a .html file.")

		#Check if the file exist
		if not self.__existFile():
			raise FileNotFoundError ("The file doesn't exist.")

		#Read the file
		html_file = open(self.file_name, "r")
		self.__content = html_file.read()
		html_file.close()

	def __existFile(self):
		try:
			file = open(self.file_name, "r")
			file.close()
			return True
		except FileNotFoundError:
			return False

	def __isHtmlFile(self):
		if self.file_name[-5:] == ".html":
			return True
		else:
			return False

	def save(self, fileName):
		#Check if fileName have svg extension
		if not fileName[-5:] == ".html":
			fileName = fileName + ".html"

		file = open(fileName, "w")
		file.write(self.__content)
		file.close()

	def personalize(self, variables, values): #variables and values have to be list of strings 
		#check if the len its the same
		if len(variables) != len(values):
			return False

		for x in range(len(variables)):
			self.__content = self.__content.replace(variables[x], values[x])

		return True

	def __str__(self):
		return self.__content

class Mail():

	def __init__(self, html, adress):
		self.__html = html
		self.__adress = adress
		self.__pdfAttached = False

	def login(self, email, password):
		self.__senderEmail = email
		self.__password = password

	def send(self, subject):
		msg = MIMEMultipart()

		try:
			msg['From'] = self.__senderEmail
			msg['To'] = self.__adress
		except:
			raise ValueError ("You need login first")

		msg['Subject'] = subject

		msg.attach(MIMEText(str(self.__html), 'html'))

		if self.__pdfAttached:

			attachFile = open(self.__fileNameAttach, 'rb')
			part = MIMEBase('application','octet-stream')
			part.set_payload((attachFile).read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', "attachment;filename= %s" % self.__fileNameAttach)
			msg.attach(part)

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(self.__senderEmail, self.__password)
		texto = msg.as_string()
		server.sendmail(self.__senderEmail, self.__adress, texto)
		server.quit()

	def attachPdf(self, fileName):
		#Check if fileName have pdf extension
		if not fileName[-4:] == ".pdf":
			fileName = fileName + ".pdf"

		self.__pdfAttached = True
		self.__fileNameAttach = fileName

	'''def enviarCorreo(Receiver_Email, Asunto, body,nombre_archivo):

		Sender_Email = "space.culagos@gmail.com"
		Password = "andromeda10_"

		msg = MIMEMultipart()
		msg['From'] = Sender_Email
		msg['To'] = Receiver_Email
		msg['Subject'] = Asunto
		
		msg.attach(MIMEText(str(self.__html), 'html'))

		adjunto = open(nombre_archivo, 'rb')
		parte = MIMEBase('application','octet-stream')
		parte.set_payload((adjunto).read())
		encoders.encode_base64(parte)
		parte.add_header('Content-Disposition', "attachment;filename= %s" % nombre_archivo)
		msg.attach(parte)

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(Sender_Email, Password)
		texto = msg.as_string()
		server.sendmail(Sender_Email, Receiver_Email, texto)
		server.quit()'''


