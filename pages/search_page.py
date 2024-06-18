import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchPage:

    def open_article_by_title(self, title: str):
        with allure.step(f'Открытие статьи с заголовком {title}'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(title))
            results.first.click()

    def should_have_title(self, title: str):
        with allure.step(f'Проверка содержания значения {title} в заголовке'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(title))


search_page = SearchPage()
