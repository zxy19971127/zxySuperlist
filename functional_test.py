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

    def check_for_row_in_list_table(self,row_text):
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

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
        time.sleep(1)
        self.check_for_row_in_list_table('1: buy peacock feather')

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        
        #仍然存在一个输入框等待她输入待办事项

        #她准备输入一个待办事项
        inputbox=self.browser.find_element_by_id('id_new_item')
        #print(inputbox.get_attribute('placeholder'))
        self.assertEqual(inputbox.get_attribute('placeholder'),'enter a to-do item')

        #她在输入区输入buy peacock feathers
        inputbox.send_keys('use peacock feathers to make a fly')

        #点击enter后，页面刷新，待办区出现一条新item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: buy peacock feather')
        self.check_for_row_in_list_table('2: use peacock feathers to make a fly')

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')

        self.assertIn('1: buy peacock feathers',[row.text for row in rows])
        self.assertIn('2: use peacock feathers to make a fly',[row.text for row in rows])
        #她希望不管她什么时候进入网站，网站都记得她的待办列表
        #并且她希望她能够拥有独一无二的专属url

        self.fail("finish the test")

if __name__=='__main__':
    unittest.main()



#browser=webdriver.Chrome(executable_path=chrome_driver)
#time.sleep(5)

#browser.get("http://localhost:8000")

#assert 'To-Do' in browser.title,"Browser title was "+browser.title



#browser.quit()
