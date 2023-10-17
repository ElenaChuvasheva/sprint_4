import pytest

from main import BooksCollector

NEW_BOOK_NAME = "Зелёная краказябра"

PHANTASY_BOOK_NAME = "Космическая ерунда"
HORROR_BOOK_NAME = "Ужос"
CRIME_STORY_BOOK_NAME = "Дарья Донцова и тяжёлая наркомания"
CARTOON_BOOK_NAME = "Детская дребедень"
COMEDY_BOOK_NAME = "Шедевры Петросяна"
ONE_MORE_CRIME_STORY_BOOK_NAME = "Дарья Донцова и тяжёлая наркомания - 2"

BOOK_NAMES = [
    PHANTASY_BOOK_NAME,
    HORROR_BOOK_NAME,
    CRIME_STORY_BOOK_NAME,
    CARTOON_BOOK_NAME,
    COMEDY_BOOK_NAME,
]

BOOKS_FOR_CHILDREN = [PHANTASY_BOOK_NAME, CARTOON_BOOK_NAME, COMEDY_BOOK_NAME]

GENRE_PHANTASY = "Фантастика"
GENRE_HORROR = "Ужасы"
GENRE_CRIME_STORY = "Детективы"
GENRE_CARTOON = "Мультфильмы"
GENRE_COMEDY = "Комедии"

GENRES = [GENRE_PHANTASY, GENRE_HORROR, GENRE_CRIME_STORY, GENRE_CARTOON, GENRE_COMEDY]


@pytest.fixture
def books_collector_one_book_added():
    collector = BooksCollector()
    collector.add_new_book(NEW_BOOK_NAME)
    return collector


@pytest.fixture
def dict_from_names_and_genres():
    return dict(zip(BOOK_NAMES, GENRES))


@pytest.fixture
def books_collector_many_books(dict_from_names_and_genres):
    collector = BooksCollector()
    collector.books_genre = dict_from_names_and_genres
    return collector


@pytest.fixture
def books_collector_two_crime_story_books(books_collector_many_books):
    collector = books_collector_many_books
    collector.books_genre[ONE_MORE_CRIME_STORY_BOOK_NAME] = GENRE_CRIME_STORY
    return collector


@pytest.fixture
def books_collector_empty():
    return BooksCollector()
