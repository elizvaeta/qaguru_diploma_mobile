import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class FavoritePage:
    @property
    def item_titles(self):
        return browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/item_title_container'))

    def open_favorite_list(self):
        with allure.step('Открытие сохранённых статей'):
            self.item_titles.first.click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/buttonView')).click()

    def should_have_article_title(self, title: str):
        with allure.step(f'Проверка наличия статьи с заголовком "{title}"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.text(title))

    def should_be_empty_favorite_list(self):
        with allure.step('Проверка отсутствия статей в Избранном'):
            self.item_titles.should(have.size(0))


favorite_page = FavoritePage()
