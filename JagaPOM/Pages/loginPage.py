class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.user_name_text_id="txtUsername"
        self.password_text_id ="txtPassword"
        self.login_button_id = "btnLogin"

    def enter_username(self,user):
        self.driver.find_element_by_id(self.user_name_text_id).clear()
        self.driver.find_element_by_id(self.user_name_text_id).send_keys("Admin")

    def enter_password(self,password):
        driver.find_element_by_id(self.password_text_id).clear()
        driver.find_element_by_id(self.password_text_id).send_keys("admin123")

    def click_on_login(self):
        driver.find_element_by_id(self.login_button_id).click()


