import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class scroll_page():
    def scroll(self):
        scrolldown = self.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(1)
        scrollup = self.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        time.sleep(1)
        scrolldown = self.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)