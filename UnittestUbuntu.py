#!/usr/bin/env python
 
import unittest
from selenium import webdriver
import time
 
class TestUbuntuHomepage(unittest.TestCase):
 
    def setUp(self):
        self.browser = webdriver.Firefox()
 
    def testTitle(self):
        self.browser.get('http://www.ubuntu.com/')
        self.assertIn('Ubuntu', self.browser.title)
	time.sleep(15)
 
    def tearDown(self):
        self.browser.quit()
 
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
