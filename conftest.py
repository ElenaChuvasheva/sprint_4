import pytest

from data import (BOOK_NAMES, CRIME_STORY_BOOK_NAME, GENRE_CRIME_STORY, GENRES,
                  NEW_BOOK_NAME, ONE_MORE_CRIME_STORY_BOOK_NAME)
from main import BooksCollector


@pytest.fixture
def books_collector_one_book_added():
    collector = BooksCollector()
    collector.add_new_book(NEW_BOOK_NAME)
    return collector


@pytest.fixture
def dict_from_names_and_genres():
    return dict(zip(BOOK_NAMES, GENRES))


@pytest.fixture
def books_collector_many(dict_from_names_and_genres):
    collector = BooksCollector()
    collector.books_genre = dict_from_names_and_genres
    return collector


@pytest.fixture
def books_collector_two_crime_story_books(books_collector_many):
    collector = books_collector_many
    collector.books_genre[ONE_MORE_CRIME_STORY_BOOK_NAME] = GENRE_CRIME_STORY
    return collector


@pytest.fixture
def books_collector_empty():
    return BooksCollector()


@pytest.fixture
def books_collector_many_with_favorite(books_collector_many):
    collector = books_collector_many
    books_collector_many.favorites.append(CRIME_STORY_BOOK_NAME)
    return collector
