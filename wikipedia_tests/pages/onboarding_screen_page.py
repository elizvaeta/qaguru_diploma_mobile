import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class OnboardingScreenPage:
    @property
    def primary_text_view(self):
        return browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))

    @property
    def secondary_text_view(self):
        return browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView'))

    def press_skip_button(self):
        with allure.step('Нажатие на кнопку "Skip"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    def press_continue_button(self):
        with allure.step('Нажатие на кнопку "Continue"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    def press_get_started_button(self):
        with allure.step('Нажатие на кнопку "Get started"'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    def should_have_first_window(self):
        with allure.step('Проверка наличия текста на первом экране'):
            self.primary_text_view.should(have.text('The Free Encyclopedia'))
            self.secondary_text_view.should(have.text('We’ve found the following on your device:'))

    def should_have_new_way_window(self):
        with allure.step('Проверка наличия текста на экране "New way"'):
            self.primary_text_view.should(have.text('New ways to explore'))
            self.secondary_text_view.should(have.text('Dive down the Wikipedia rabbit'))

    def should_have_reading_lists_window(self):
        with allure.step('Проверка наличия текста на экране "Reading lists"'):
            self.primary_text_view.should(have.text('Reading lists with sync'))
            self.secondary_text_view.should(have.text('Join Wikipedia'))

    def should_have_data_and_privacy_window(self):
        with allure.step('Проверка наличия текста на экране "Data and Privacy"'):
            self.primary_text_view.should(have.text('Data & Privacy'))
            self.secondary_text_view.should(have.text('terms of use'))


onboarding_screen_page = OnboardingScreenPage()
