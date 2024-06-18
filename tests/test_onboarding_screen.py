from pages.main_page import main_page
from pages.onboarding_screen_page import onboarding_screen_page


def test_getting_started():
    onboarding_screen_page.should_have_first_window()
    onboarding_screen_page.press_continue_button()

    onboarding_screen_page.should_have_new_way_window()
    onboarding_screen_page.press_continue_button()

    onboarding_screen_page.should_have_reading_lists_window()
    onboarding_screen_page.press_continue_button()

    onboarding_screen_page.should_have_data_and_privacy_window()
    onboarding_screen_page.press_get_started_button()

    main_page.should_be_main_page()
