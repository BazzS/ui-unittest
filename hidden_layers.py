from .baseApp import Base
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

class Locators:
    BUTTON = (By.ID, "greenButton")

class SearchHiddenLayers(Base):
    def click_button(self):
        try:
            self.find_element(Locators.BUTTON, time=2).click()
            answer = True
        except ElementClickInterceptedException:
            answer = False
        return answer
