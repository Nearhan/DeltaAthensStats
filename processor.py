from openpyxl.workbook import Workbook
import os, datetime, re


#############
## settings ##
#############

settings = { 'current_directory' : os.path.join(os.getcwd()+'/reports', datetime.date.today().isoformat()),

	}


class Processor(object):
	global settings


	def __init__(self):
		self.configure(settings)


	def configure(self, settings):

		for key, value in settings.iteritems():
			setattr(self, key, value)


	def gather_all_files_and_split(self):

		self.all_xslx
		self.business_xslx = []
		self.regular_xslsx= []

		all_files = os.listdir(self.current_directory)

		for single_file in all_files:

			if re.search(r'.xlsx$', single_file):
				self.all_xslx.append(single_file)


		for xlsx in self.all_xslx:

			if re.search(r'Bus', xslx):
				self.business_xslx.append(xsls)
			else:
				self.regular_xslx.append(xslx)

				


