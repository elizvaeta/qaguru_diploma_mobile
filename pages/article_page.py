import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class ArticlePage:
    def save_to_favorite(self):
        with allure.step('Сохранение статьи в Избранное'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_save')).click()

    def remove_from_favorite(self):
        with allure.step('Удаление статьи из Избранного'):
            self.save_to_favorite()
            actions = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/title'))
            actions[2].click()

    def go_to_favorite(self):
        with allure.step('Переход в Избранное из статьи'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()

            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/nav_tab_reading_lists')).click()


article_page = ArticlePage()
