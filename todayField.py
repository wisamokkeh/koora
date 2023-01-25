from selenium.webdriver.common.by import By


class today():
    def today_click(self):
        today_click = self.find_element(By.XPATH, "(//a[@class='nav_li_link'])[7]")
        today_click.click()