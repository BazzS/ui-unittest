from .baseApp import Base
from selenium.webdriver.common.by import By
from random import randint

class Locators:
    LOGIN_STATUS = (By.ID, 'loginstatus')
    USER_NAME = (By.NAME, 'UserName')
    PASSWORD = (By.NAME, 'Password')
    BUTTON = (By.ID, 'login')

class SearchSampleApp(Base):
    def login_status(self):
        return self.find_element(Locators.LOGIN_STATUS, time=2).text

    def click_button(self):
        return self.find_element(Locators.BUTTON, time=2).click()

    def enter_username(self):
        username = randint(10,100)
        self.find_element(Locators.USER_NAME, time=2).send_keys(f'{username}')
        return username

    def enter_password(self):
        return self.find_element(Locators.PASSWORD, time=2).send_keys('pwd')

    def click_login(self):
        return self.find_element(Locators.BUTTON, time=2).click()
