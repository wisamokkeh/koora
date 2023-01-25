import time

from selenium.webdriver.common.by import By


class engPage():
    def englend_click(self):
        england_click = self.find_element(By.XPATH, "//img[@alt='الدوري الألماني الدرجة الأولى']")
        england_click.click()
        time.sleep(4)