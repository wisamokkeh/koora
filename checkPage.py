from selenium.webdriver.common.by import By


class checkMainPage():
    def check_main_page(self):
        try:
            self.find_element(By.ID, 'featuredNews')
        except:
            return print("no videos")

        try:
            self.find_element(By.ID, 'sidebar')
        except:
            return print("no sidebar")
        try:
            self.find_element(By.CLASS_NAME, 'newsList')
        except:
            return print("no news")