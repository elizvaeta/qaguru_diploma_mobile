import allure
from pages.main_page import main_page
from pages.onboarding_screen_page import onboarding_screen_page
from pages.search_page import search_page


@allure.epic('Главная страница')
@allure.story('Поиск статей')
class TestSearch:
    @allure.title('Поиск статьи')
    def test_search(self):
        article_title = 'Roman Empire'

        onboarding_screen_page.press_skip_button()
        main_page.search_text(article_title)

        search_page.should_have_title(article_title)

    @allure.title('Открытие статьи')
    def test_search_and_open(self):
        article_title = 'Roman Empire'

        onboarding_screen_page.press_skip_button()
        main_page.search_text(article_title)

        search_page.open_article_by_title(article_title)
