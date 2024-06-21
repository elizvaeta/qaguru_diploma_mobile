import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchPage:

    def open_article_by_title(self, title: str):
        with allure.step(f'Открытие статьи с заголовком "{title}"'):
            article_title = self.should_have_title(title)
            article_title.first.click()

    def should_have_title(self, title: str):
        with allure.step(f'Проверка содержания значения "{title}" в заголовке'):
            article_titles = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            article_titles.should(have.size_greater_than(0))
            article_titles.first.should(have.text(title))

            return article_titles


search_page = SearchPage()
