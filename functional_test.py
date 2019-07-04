from selenium import webdriver
import time
import unittest

chrome_driver='C:/Users/xinyue/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe'

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Chrome(executable_path=chrome_driver)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do",self.browser.title)
        self.fail("finish the test")

if __name__=='__main__':
    unittest.main()



#browser=webdriver.Chrome(executable_path=chrome_driver)
#time.sleep(5)

#browser.get("http://localhost:8000")

#assert 'To-Do' in browser.title,"Browser title was "+browser.title



#browser.quit()
