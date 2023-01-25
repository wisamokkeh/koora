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