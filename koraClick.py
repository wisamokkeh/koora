from selenium.webdriver.common.by import By
import time

class mainClick():
    def main_click(self):
        main_box = self.find_element(By.XPATH, "(//a[@class='nav_li_link'])[1]")
        time.sleep(3)
        main_box.click()
        time.sleep(2)