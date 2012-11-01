from processor import Processor
import unittest, os, datetime


class ProcessorTests(unittest.TestCase):

	'''Represents All Processeor Tests'''


	def setUp(self):

		self.processor = Processor()


	def test_current_directory(self):
		print self.processor.current_directory
		self.assertEqual(self.processor.current_directory, os.path.join(os.getcwd()+'/reports', datetime.date.today().isoformat()))

	def test_contents_of_files(self):
		'''gather xls files'''
		self.processor.gather_all_files_and_split()
		print self.processor.business_xsls
		print '\n'
		print self.processor.regular_xsls
		self.assertTrue(self.processor.business_xsls)
		self.assertTrue(self.processor.regular_xsls)






if __name__ == '__main__':
	unittest.main()
