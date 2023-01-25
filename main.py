import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KooraPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get("https://www.kooora.com")
        self.browser.maximize_window()


    def today_click(self):
        today_click = self.browser.find_element(By.XPATH, "//a[@class='nav_li_link'][contains(text(),'اليوم')]")
        today_click.click()

    def englend_click(self):
        england_click = self.browser.find_element(By.XPATH,"//img[@alt='الدوري الألماني الدرجة الأولى']")
        england_click.click()
        time.sleep(4)



    def polyce(self):
        polyce_click = self.browser.find_element(By.PARTIAL_LINK_TEXT, "سياسة ")
        polyce_click.click()
