import time

from selenium.webdriver.common.by import By


class polyPage():
    def polyce(self):
        polyce_click = self.find_element(By.PARTIAL_LINK_TEXT, "سياسة ")
        polyce_click.click()
