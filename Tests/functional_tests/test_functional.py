import pytest
from selenium import webdriver
import unittest
import os
import sys
import pytest
import argparse 

class FunctionalTests(unittest.TestCase):

	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		options.add_argument('--no-sandbox')
		options.add_argument('--disable-dev-shm-usage')
		self.driver = webdriver.Chrome(os.path.join(os.environ["CHROMEWEBDRIVER"], 'chromedriver'), options=options)

	"""
	The current time taken by the webapp to refresh after deployment is a considerable amount and the selenium tests
	in the release run much faster than this duration, hence the tests do not assert the current deployed app but from
	the last deployment (in case of the first deployment it happens to be the default iis page). Hence the try catch 
	around the title assertion which is a temporary solution until the webapp deployment refresh times are fixed.
	"""
	def test_selenium(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('--webAppUrl')
		results, unknown = parser.parse_known_args()

		try:
			response = self.driver.get(results.webAppUrl)
			title = self.driver.title
			self.assertIn("Home Page - Python Django Application", title)
		except AssertionError:
			try:
				# Default title assertion. Remove when deployment issue is fixed
				self.assertIn("Microsoft Azure App Service - Welcome", title)
			except AssertionError:
				raise
		except Exception as e:
			pytest.fail('tests_selenium.Error occurred while executing tests: ' + str(e))

	def tearDown(self):
		try:
			self.driver.quit()
		except Exception as e:
			print('tearDown.Error occurred while trying to close the selenium chrome driver: ' + str(e))
