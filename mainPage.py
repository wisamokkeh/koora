import time

import assertpage
import checkPage
import koraClick
import main
import scrollPage


class mainPage():
    # create a new Chrome browser instance
    browser = main.webdriver.Chrome()

    # create an instance of the kora Page
    koora_page = main.KooraPage(browser)

    # load the page
    koora_page.load()
    checkPage.checkMainPage.check_main_page(browser)

    # perform the main
    koraClick.mainClick.main_click(browser)

    # click today
    koora_page.today_click()
    time.sleep(3)

    # england click
    koora_page.englend_click()

    # assert title
    assertpage.assertP.assert_title(browser)
    time.sleep(2)

    # return to main page
    koraClick.mainClick.main_click(browser)

    # scroll
    scrollPage.scroll_page.scroll(browser)
    time.sleep(2)

    # polyce click
    koora_page.polyce()

