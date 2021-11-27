import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions


class InstaFollower:
    def __init__(self, page_link, username, password):
        self.user = username
        self.pass_ = password
        self.page = page_link
        self.browser = webdriver.Edge("D:/development/msedgedriver.exe")
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.login()
        self.followers()

    def login(self):
        try:
            time.sleep(3)
            login_button = self.browser.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
            login_button.click()
            time.sleep(2)
        except exceptions.NoSuchElementException:
            pass
        username = self.browser.find_element(By.NAME, "username")
        username.send_keys(self.user)
        password_field = self.browser.find_element(By.NAME, "password")
        password_field.send_keys(self.pass_)
        button = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        button.click()
        time.sleep(3)
        # not_now = self.browser.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        # not_now.click()
        # time.sleep(5)

    def followers(self):
        self.browser.get(self.page)
        followers = self.browser.find_element(By.CSS_SELECTOR, "a.-nal3")
        followers_count = self.browser.find_elements(By.CLASS_NAME, "g47SY")
        try:
            print(int("".join(followers_count[1].text.split(","))))
            value = int("".join(followers_count[1].text.split(",")))
        except ValueError:
            print(int("".join(followers_count[1].text.split("m"))))
            value = int("".join(followers_count[1].text.split("m")))
        all_followers = []
        followers.click()
        time.sleep(5)
        # self.follow()
        end = False
        global list_follow
        list_follow = []
        while not end:
            popup = self.browser.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
            follow_buttons = self.browser.find_elements(By.CSS_SELECTOR, "button.sqdOP.L3NKy.y3zKF")
            print(len(follow_buttons))
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            list_follow.append(len(follow_buttons))
            if len(follow_buttons) > value/3:
                if list_follow[-2] == list_follow[-1]:
                    self.follow()
                    end = True
            time.sleep(5)

    def follow(self):
        all_buttons = self.browser.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except exceptions.ElementClickInterceptedException:
                cancel_button = self.browser.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()
