import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class OnboardingScreenPage:
    def press_skip_button(self):
        with allure.step('Нажатие на кнопку Skip'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    def press_continue_button(self):
        with allure.step('Нажатие на кнопку Continue'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    def press_get_started_button(self):
        with allure.step('Нажатие на кнопку Get started'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    def should_have_first_window(self):
        with allure.step('Проверка наличия текста на первом экране'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('The Free Encyclopedia'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')).should(
                have.text('We’ve found the following on your device:'))

    def should_have_new_way_window(self):
        with allure.step('Проверка наличия текста на экране "New way"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('New ways to explore'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')).should(
                have.text('Dive down the Wikipedia rabbit'))

    def should_have_reading_lists_window(self):
        with allure.step('Проверка наличия текста на экране "Reading lists"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('Reading lists with sync'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')).should(
                have.text('Join Wikipedia'))

    def should_have_data_and_privacy_window(self):
        with allure.step('Проверка наличия текста на экране "Data and Privacy"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('Data & Privacy'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')).should(
                have.text('terms of use'))


onboarding_screen_page = OnboardingScreenPage()
