from pages.search_page import SearchPage


class TestFormPage:

    def test_search(self, driver):
        search_page = SearchPage(driver, 'https://ya.ru/')
        search_page.open()
        search_page.search()