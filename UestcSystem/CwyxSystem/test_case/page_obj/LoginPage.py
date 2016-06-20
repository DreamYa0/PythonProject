# coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class login(Page):
    url = '/'
    CwyxSystem_login_user_loc = (By.XPATH, "")
    CwyxSystem_login_button_loc = (By.ID, "")

    def CwyxSystem_login(self):
        self.find_element(*self.CwyxSystem_login_user_loc).click()
        sleep(1)
        self.find_element(*self.CwyxSystem_login_button_loc).click()

    login_username_loc = (By.ID, "account")
    login_password_loc = (By.ID, "password")
    login_button_loc = (By.ID, "login")
