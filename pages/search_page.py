from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPageLocators:
    SEARCH = (By.ID, 'text')
    SUBMIT = (By.CLASS_NAME, 'mini-suggest__button')
    SEARCH_RESULT = (By.CLASS_NAME, 'entity-search')

class SearchPage(BasePage):

    def search(self):
        search = 'земля'
        self.element_is_visible(SearchPageLocators.SEARCH).send_keys(search)
        self.element_is_visible(SearchPageLocators.SUBMIT).click()
        self.element_is_visible(SearchPageLocators.SEARCH_RESULT)

