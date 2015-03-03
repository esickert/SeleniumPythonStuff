from selenium import webdriver
import unittest, time

class CNNTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
 #       self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.CNN.com')
   #     self.assertIn('CNN', self.browser.title)
 #       time.sleep(30) 

if __name__ == '__main__':
    unittest.main(verbosity=2)
