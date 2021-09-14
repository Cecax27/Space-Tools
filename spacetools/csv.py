import os

class Csv:

	def __init__(self, file_name):
		self.file_name = file_name
		self.header = []
		self.varNumber = 0
		self.base = [] 

	def read(self):
		#Check if the file is a .csv
		if not self.__isCsvFile():
			raise FileExistsError ("The file is not a .csv file.")

		#Check if the file exist
		if not self.__existFile():
			raise FileNotFoundError ("The file doesn't exist.")
		
		#Read the file
		csv_file = open(self.file_name, "r")
		data = csv_file.readlines()
		csv_file.close()

		#Process the data
		for i in data:
			aux = i.split(",")
			for a in aux:
				aux[aux.index(a)] = a.strip()
			data[data.index(i)]=aux
		
		self.header = data[0]
		data.pop(0)
		self.base = data
		self.varNumber = len(self.header)
		return True

	def __existFile(self):
		try:
			file = open(self.file_name, "r")
			file.close()
			return True
		except FileNotFoundError:
			return False

	def __isCsvFile(self):
		if self.file_name[-4:] == ".csv":
			return True
		else:
			return False

	def export_svg_pdf(self, svg_object, file_name_format):
		for i in self.base:
			tmp_svg = Svg(svg_object.file_name)
			tmp_svg.export_pdf(self.header, i, file_name_format+".pdf")
			del tmp_svg