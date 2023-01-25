import time

import assertpage
import checkPage
import countPage
import koraClick
import main
import polycPage
import scrollPage
import todayField


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
    todayField.today.today_click(browser)
    time.sleep(3)

    # england click
    countPage.engPage.englend_click(browser)

    # assert title
    assertpage.assertP.assert_title(browser)
    time.sleep(2)

    # return to main page
    koraClick.mainClick.main_click(browser)

    # scroll
    scrollPage.scroll_page.scroll(browser)
    time.sleep(2)

    # polyce click
    polycPage.polyPage.polyce(browser)

