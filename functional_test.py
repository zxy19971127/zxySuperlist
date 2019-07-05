from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


chrome_driver='C:/Users/xinyue/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe'

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Chrome(executable_path=chrome_driver)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #打开网站的首页
        self.browser.get("http://localhost:8000")

        #看到该页面的标题为to-do lists
        self.assertIn("To-Do",self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #她准备输入一个待办事项
        inputbox=self.browser.find_element_by_id('id_new_item')
        #print(inputbox.get_attribute('placeholder'))
        self.assertEqual(inputbox.get_attribute('placeholder'),'enter a to-do item')

        #她在输入区输入buy peacock feathers
        inputbox.send_keys('buy peacock feathers')

        #点击enter后，页面刷新，待办区出现一条新item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text=='1:Buy peacock feathers' for row in rows),"new to-do item did not appear in table")

        #仍然存在一个输入框等待她输入待办事项

        self.fail("finish the test")

if __name__=='__main__':
    unittest.main()



#browser=webdriver.Chrome(executable_path=chrome_driver)
#time.sleep(5)

#browser.get("http://localhost:8000")

#assert 'To-Do' in browser.title,"Browser title was "+browser.title



#browser.quit()
