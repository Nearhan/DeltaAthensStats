from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime


################
## SETTINGS ##
################

settings = { 'url': 'https://jira.akqa.net',
			'username' : 'Farhan.Syed',
			'password' : 'Red19378246!',
			'date' : datetime.date.today().isoformat(),
			'bussines_filters' : [],
			'regular_filters': [],
			'http_elements' : {
				'username' : 'login-form-username',
				'password' : 'login-form-password',
				}, 
			}




class Browser(object):
	global settings

	def __init__(self):
		self.webdriver = webdriver.Firefox()
		self.configure(settings)


	def close(self):
		self.webdriver.close()

	def go(self):	
		self.webdriver.get(self.url)

	def title(self):
		return self.webdriver.title

	def log_into_jira(self):
		self.webdriver.switch_to_frame('gadget-0')
		login = self.webdriver.find_element_by_id(self.http_elements['username'])
		login.send_keys(self.username)
		password = self.webdriver.find_element_by_id(self.http_elements['password'])
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		#username = self.webdriver.find_element_by_link_text('')

	def find_by_link_text(self, text):
		return self.webdriver.find_element_by_link_text(text)


	def configure(self, settings):
		for key, value in settings.iteritems():
			setattr(self, key, value)



