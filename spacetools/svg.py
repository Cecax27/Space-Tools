import os
from io import open

class Svg:

	def __init__(self, file_name):
		self.file_name = file_name
		self.__content = ""


	def read(self):
		#Check if the file is a .svg
		if not self.__isSvgFile():
			raise FileExistsError ("The file is not a .svg file.")

		#Check if the file exist
		if not self.__existFile():
			raise FileNotFoundError ("The file doesn't exist.")

		#Read the file
		svg_file = open(self.file_name, "r")
		self.__content = svg_file.read()
		svg_file.close()

	def __existFile(self):
		try:
			file = open(self.file_name, "r")
			file.close()
			return True
		except FileNotFoundError:
			return False

	def __isSvgFile(self):
		if self.file_name[-4:] == ".svg":
			return True
		else:
			return False

	def save(self, fileName):
		#Check if fileName have svg extension
		if not fileName[-4:] == ".svg":
			fileName = fileName + ".svg"

		file = open(fileName, "w")
		file.write(self.__content)
		file.close()

	def savePdf(self, fileName):
		#Check if temp.svg exist
		try:
			file = open("tmp.svg", "x")
			file.close()
		except FileExistsError:
			return False

		#Check if fileName have pdf extension
		if not fileName[-4:] == ".pdf":
			fileName = fileName + ".pdf"

		#Save a temp file in tmp.svg
		self.save("tmp.svg")
		
		#Convert the svg file to a pdf file with inkscape	
		os.system("inkscape tmp.svg --export-type=pdf")
		#Remove the tmp file
		os.remove("tmp.svg")
		#Change the name of the pdf file to fileName
		os.system("mv tmp.pdf "+fileName.replace(" ","_"))
		return True

	def personalize(self, names, base): #names and base have to be list of strings 
		#check if the len its the same
		if len(names) != len(base):
			return False

		for x in range(len(names)):
			self.__content = self.__content.replace(names[x], base[x])

		return True