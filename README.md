# qa_python
## Список тестов
* ### test_add_new_book_no_genre  
  У добавленной книги нет жанра
* ### test_set_book_genre
  Метод set_book_genre устанавливает жанр книги
* ### test_get_book_genre
  Метод get_book_genre возвращает жанр книги по её имени
* ### test_get_books_with_specific_genre
  Метод get_books_with_specific_genre возвращает список книг с указанным жанром
* ### test_get_books_genre
  Метод get_books_genre возвращает словарь из имён и жанров
* ### test_get_books_for_children_no_rating
  В список книг для детей не попадают книги с рейтингом
* ### test_add_existing_book_to_favorites
  Можно добавить книгу из словаря в избранное
* ### test_delete_existing_book_from_favorites
  Можно удалить книгу из избранного, если она там есть
* ### test_get_list_of_favorites_books
  Метод get_list_of_favorites_books возвращает список избранных книг
