from pages.main_page import main_page
from pages.onboarding_screen_page import onboarding_screen_page
from pages.search_page import search_page


def test_search_appium():
    article_title = 'Roman Empire'

    onboarding_screen_page.press_skip_button()
    main_page.search_text(article_title)

    search_page.should_have_title(article_title)


def test_search_and_open():
    article_title = 'Roman Empire'
    
    onboarding_screen_page.press_skip_button()
    main_page.search_text(article_title)

    search_page.open_article_by_title(article_title)
