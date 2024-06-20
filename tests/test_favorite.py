import allure
from pages.article_page import article_page
from pages.favorite_page import favorite_page
from pages.main_page import main_page
from pages.onboarding_screen_page import onboarding_screen_page
from pages.search_page import search_page


@allure.epic('Экран "Избранное"')
@allure.story('Добавление и удаление из Избранного')
@allure.title('Добавление статьи в Избранное')
def test_add_to_favorite():
    article_title = 'Roman Empire'

    onboarding_screen_page.press_skip_button()
    main_page.search_text(article_title)
    search_page.open_article_by_title(article_title)

    article_page.save_to_favorite()

    article_page.go_to_favorite()
    favorite_page.open_favorite_list()
    favorite_page.should_have_article_title(article_title)


@allure.epic('Экран "Избранное"')
@allure.story('Добавление и удаление из Избранного')
@allure.title('Удаление статьи из Избранного')
def test_delete_from_favorite():
    article_title = 'Roman Empire'

    onboarding_screen_page.press_skip_button()
    main_page.search_text(article_title)
    search_page.open_article_by_title(article_title)

    article_page.save_to_favorite()
    article_page.remove_from_favorite()

    article_page.go_to_favorite()
    favorite_page.should_be_empty_favorite_list()
