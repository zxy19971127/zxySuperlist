from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time
import unittest
from selenium.common.exceptions import WebDriverException
MAX_WAIT=10


chrome_driver='C:/Users/xinyue/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe'

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Chrome(executable_path=chrome_driver)

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self,row_text):
        start_time=time.time()
        while True:
            try:
                table=self.browser.find_element_by_id('id_list_table')
                rows=table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return
            except(AssertionError,WebDriverException) as e:
                if time.time()-start_time>MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        #打开网站的首页
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: buy peacock feathers')

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

        self.wait_for_row_in_list_table('1: buy peacock feathers')
        self.wait_for_row_in_list_table('2: use peacock feathers to make a fly')

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')

        self.assertIn('1: buy peacock feathers',[row.text for row in rows])
        self.assertIn('2: use peacock feathers to make a fly',[row.text for row in rows])
        #她希望不管她什么时候进入网站，网站都记得她的待办列表
        #并且她希望她能够拥有独一无二的专属url


    def test_mutiple_users_can_starts_lists_at_different_urls(self):
        #艾迪打开了一个新的待办事项列表
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: buy peacock feathers')
        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')#检查字符串是否与正则表达式匹配

        ##现在出现了一个新的用户打开了网站
        ##我们使用了一个新的session来保证该用户不会从cookiesi里面看到属于edith的信息
        self.browser.quit()

        self.browser=webdriver.Chrome(executable_path=chrome_driver)
        #弗兰西进入了主页，她看不见edith的信息

        self.browser.get(self.live_server_url)
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #弗兰西输入了一个新的表项
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy milk')

        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: buy milk')

        #弗兰西获得了属于自己的url
        francis_list_url=self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        #她追溯不到edith的列表
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy peacock feathers')
        self.assertIn('buy milk',page_text)

        #两个人都心满意足
        #self.fail("finish the test")





#browser=webdriver.Chrome(executable_path=chrome_driver)
#time.sleep(5)

#browser.get("http://localhost:8000")

#assert 'To-Do' in browser.title,"Browser title was "+browser.title



#browser.quit()
