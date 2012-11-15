from processor import Processor
import unittest, os, datetime


class ProcessorTests(unittest.TestCase):

	'''Represents All Processeor Tests'''


	def setUp(self):

		self.processor = Processor()

	
	def test_current_directory(self):
		self.assertEqual(self.processor.current_directory, os.path.join(os.getcwd()+'/reports', datetime.date.today().isoformat()))

	def test_contents_of_files(self):

		
		self.processor.gather_all_files_and_split()
		self.assertTrue(self.processor.business_xlsx)
		self.assertTrue(self.processor.regular_xlsx)

	def test_sorting_order(self):
		self.processor.gather_all_files_and_split()
		self.processor.sort_all_files()
		self.assertEqual(len(self.processor.business_xlsx), 7)
		self.assertEqual(len(self.processor.regular_xlsx), 6)
		
	

	def test_to_create_both_workbooks(self):
		self.processor.gather_all_files_and_split()

		print '****** After gather all files ****\n'
		print self.processor.business_xlsx
		print ' *********\n'

		self.processor.sort_all_files()

		print '****** After sort all files ****\n'
		print self.processor.business_xlsx
		print ' *********\n'


		self.processor.create_both_workbooks()

		print '****** After create work book ****\n'
		print self.processor.business_xlsx
		print ' *********\n'


	def test_to_save_workbooks(self):
		self.processor.gather_all_files_and_split()
		self.processor.sort_all_files()
		self.processor.create_both_workbooks()


		self.processor.clean_workbooks()

		print '****** After clean workbook ****\n'
		print self.processor.business_xlsx
		print ' *********\n'

		self.processor.save_all_workbooks()

		print '****** After save workbook ****\n'
		print self.processor.business_xlsx
		print ' *********\n'

		self.assertTrue(self.processor.business_workbook)
		self.assertTrue(self.processor.regular_workbook)














if __name__ == '__main__':
	unittest.main()
