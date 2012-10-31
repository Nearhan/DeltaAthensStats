import unittest
from browser import Browser

class BrowserTest(unittest.TestCase):
	'''going to test basic Browser Usage'''


	def setUp(self):
		self.browser = Browser()
	'''
	def test_browser_is_true(self):
		self.assertTrue(self.browser)

	def test_check_settings_file(self):
		self.assertTrue(self.browser.settings)


	def test_go_to_jira(self):
		self.browser.go()
		self.assertIn('JIRA', self.browser.title())
	'''
	def test_log_into_jira(self):
		self.browser.go()
		self.browser.log_into_jira()
		link_text = self.browser.webdriver.find_element_by_link_text('Farhan Syed')
		self.assertIn('Farhan', link_text.text)

	def tearDown(self):
		self.browser.close()



if __name__ == '__main__':
	unittest.main()
