from selenium.webdriver.common.by import By

class assertP():
    def assert_title(self):
        title = self.find_element(By.CLASS_NAME, 'pageTitle')
        titlePage = self.title
        try:
            assert title.text == titlePage
            return print('is the same=' + title.text + " , " + titlePage)
        except:
            return print("not same title")
        return title.text