from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver import ActionChains
import re
import datetime


################
## SETTINGS ##
################

settings = { 'url': 'https://jira.akqa.net',
			'username' : 'Farhan.Syed',
			'password' : 'Red19378246!',
			'date' : datetime.date.today().isoformat(),
			'bussiness_filters' : ['As Designed Bugs Business',],
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


	def select_delta_iphone_dashboard(self):
		home_link_drop = self.webdriver.find_element_by_id('home_link_drop')
		home_link_drop.click()
		delta_iphone_dashboard = self.webdriver.find_element_by_link_text('Delta Iphone')
		delta_iphone_dashboard.click()
		

	def wait(self, time=10):
		'''Calls WebDriverWait calls to wait for a specific event or value'''
		return ui.WebDriverWait(self.webdriver,time)


	def configure(self, settings):
		for key, value in settings.iteritems():
			setattr(self, key, value)


	def download_xsls_files(self):

		for specific_filter in self.bussiness_filters:

			self.webdriver.switch_to_frame('gadget-16534')
			found_element = [x for x in self.webdriver.find_elements_by_tag_name('a') if re.match(specific_filter, x.text)][0]
			found_element.click()
			#self.wait().until(lambda x: x.find_element_by_link_text(specific_filter))
			#self.webdriver.find_element_by_link_text(specific_filter).click()
			self.webdriver.find_element_by_id('viewOptions').click()
			self.webdriver.find_element_by_link_text('Excel (Current fields)').click()








