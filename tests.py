import pytest

from data import (
    CARTOON_BOOK_NAME,
    COMEDY_BOOK_NAME,
    CRIME_STORY_BOOK_NAME,
    GENRE_CRIME_STORY,
    HORROR_BOOK_NAME,
    NEW_BOOK_NAME,
    ONE_MORE_CRIME_STORY_BOOK_NAME,
    PHANTASY_BOOK_NAME,
)
from main import BooksCollector

BOOK_IN_CHILDRENS_LIST = [
    [PHANTASY_BOOK_NAME, True],
    [HORROR_BOOK_NAME, False],
    [CRIME_STORY_BOOK_NAME, False],
    [CARTOON_BOOK_NAME, True],
    [COMEDY_BOOK_NAME, True],
]


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_no_genre(self, books_collector_one_book_added):
        assert books_collector_one_book_added.get_book_genre(NEW_BOOK_NAME) == ""

    def test_set_book_genre(self, books_collector_one_book_added):
        books_collector_one_book_added.set_book_genre(NEW_BOOK_NAME, GENRE_CRIME_STORY)
        assert books_collector_one_book_added.get_book_genre(NEW_BOOK_NAME) == GENRE_CRIME_STORY

    def test_get_book_genre(self, books_collector_many):
        book_genre = books_collector_many.get_book_genre(CRIME_STORY_BOOK_NAME)
        assert book_genre == GENRE_CRIME_STORY

    @pytest.mark.parametrize(
        "crime_story_name",
        [CRIME_STORY_BOOK_NAME, ONE_MORE_CRIME_STORY_BOOK_NAME],
    )
    def test_get_books_with_specific_genre(
        self, books_collector_two_crime_story_books, crime_story_name
    ):
        result = books_collector_two_crime_story_books.get_books_with_specific_genre(
            GENRE_CRIME_STORY
        )

        assert isinstance(result, list)
        assert len(result) == 2
        assert crime_story_name in result

    def test_get_books_genre(self, books_collector_many, dict_from_names_and_genres):
        assert books_collector_many.get_books_genre() == dict_from_names_and_genres

    @pytest.mark.parametrize(
        "name, is_in_list",
        BOOK_IN_CHILDRENS_LIST,
    )
    def test_get_books_for_children_no_rating(self, name, is_in_list, books_collector_many):
        books_for_children = books_collector_many.get_books_for_children()
        assert (name in books_for_children) == is_in_list

    def test_add_existing_book_to_favorites(self, books_collector_many):
        books_collector_many.add_book_in_favorites(CRIME_STORY_BOOK_NAME)

        assert books_collector_many.get_list_of_favorites_books() == [CRIME_STORY_BOOK_NAME]

    def test_delete_existing_book_from_favorites(self, books_collector_many_with_favorite):
        books_collector_many_with_favorite.delete_book_from_favorites(CRIME_STORY_BOOK_NAME)

        assert books_collector_many_with_favorite.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, books_collector_many_with_favorite):
        assert books_collector_many_with_favorite.get_list_of_favorites_books() == [
            CRIME_STORY_BOOK_NAME
        ]
