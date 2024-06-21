import allure
from wikipedia_tests.pages.main_page import main_page
from wikipedia_tests.pages.onboarding_screen_page import onboarding_screen_page


@allure.epic('Начальный экран')
@allure.story('Просмотр начального экрана')
class TestOnboardingScreen:
    @allure.title('Наличие страниц на начальном экране')
    def test_getting_started(self):
        onboarding_screen_page.should_have_first_window()
        onboarding_screen_page.press_continue_button()

        onboarding_screen_page.should_have_new_way_window()
        onboarding_screen_page.press_continue_button()

        onboarding_screen_page.should_have_reading_lists_window()
        onboarding_screen_page.press_continue_button()

        onboarding_screen_page.should_have_data_and_privacy_window()
        onboarding_screen_page.press_get_started_button()

        main_page.should_be_main_page()
