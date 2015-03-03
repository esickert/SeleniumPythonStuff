from selenium import webdriver
import unittest, time

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
#        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('google', self.browser.title)
        time.sleep(30) 

if __name__ == '__main__':
    unittest.main(verbosity=2)
