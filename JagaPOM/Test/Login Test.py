import os
import sys
import time
import unittest

import HtmlTestRunner
from selenium import webdriver

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from JagaPOM.Pages.loginPage import LoginPage
from JagaPOM.Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def Test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_on_login()
        home = HomePage(driver)
        home.click_welcome_link()
        home.click_on_logout_link()

        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/seleniumwd2/Sample Project/report"))
