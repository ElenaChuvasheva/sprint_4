import copy

import pytest

import data
from main import BooksCollector


@pytest.fixture
def books_collector_one_book_added():
    collector = BooksCollector()
    collector.add_new_book(data.NEW_BOOK_NAME)
    return collector


@pytest.fixture
def dict_from_names_and_genres():
    book_names = [
        data.PHANTASY_BOOK_NAME,
        data.HORROR_BOOK_NAME,
        data.CRIME_STORY_BOOK_NAME,
        data.CARTOON_BOOK_NAME,
        data.COMEDY_BOOK_NAME,
    ]
    genres = [
        data.GENRE_PHANTASY,
        data.GENRE_HORROR,
        data.GENRE_CRIME_STORY,
        data.GENRE_CARTOON,
        data.GENRE_COMEDY,
    ]

    return dict(zip(book_names, genres))


@pytest.fixture
def books_collector_many(dict_from_names_and_genres):
    collector = BooksCollector()
    for name, genre in dict_from_names_and_genres.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector


@pytest.fixture
def books_collector_two_crime_story_books(books_collector_many):
    collector = copy.deepcopy(books_collector_many)
    collector.add_new_book(data.ONE_MORE_CRIME_STORY_BOOK_NAME)
    collector.set_book_genre(data.ONE_MORE_CRIME_STORY_BOOK_NAME, data.GENRE_CRIME_STORY)
    return collector


@pytest.fixture
def books_collector_many_with_favorite(books_collector_many):
    collector = copy.deepcopy(books_collector_many)
    collector.add_book_in_favorites(data.CRIME_STORY_BOOK_NAME)
    return collector
