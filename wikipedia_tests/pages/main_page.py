import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class MainPage:
    def search_text(self, text: str):
        with allure.step(f'Ввод в поисковой строке "{text}"'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)

    def should_be_main_page(self):
        with allure.step('Проверка открытия главного экрана'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_text')).should(
                have.text('Customize your Explore feed'))


main_page = MainPage()
