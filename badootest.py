import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BadooApp(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()


    def test_badoo_login(self):
        browser = self.browser
        browser.get('https://badoo.com/en/mobile')
        self.assertEqual(browser)


    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()