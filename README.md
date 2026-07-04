test_add_new_book_add_two_books_shows_true – проверяет добавление двух разных книг.

test_add_new_book_add_two_equal_books_shows_true – проверяет, что дубликаты книг не добавляются.

test_add_new_book_add_incorrect_name_shows_error – проверяет, что книга с некорректным именем (пустая строка или слишком длинное название) не добавляется.

test_set_book_genre_one_book_one_genre_shows_true – проверяет успешную установку жанра для существующей книги.

test_set_book_genre_incorrect_one_book_one_genre_shows_false – проверяет, что установка жанра для несуществующей книги или несуществующего жанра не работает.

test_get_book_genre_one_book_shows_true – параметризованный тест получения жанра по названию.

test_get_book_genre_one_non_existing_book_shows_error – проверяет, что для несуществующей книги возвращается None.

test_get_books_with_specific_genre_three_books_three_genres_shows_true – параметризованный тест получения списка книг определённого жанра.

test_get_books_genre_one_book_one_genre_shows_true – проверяет, что метод get_books_genre() возвращает корректный словарь.

test_get_books_for_children_three_books_three_genre_shows_true – параметризованный тест получения списка книг для детей (исключаются жанры «Ужасы» и «Детективы»).

test_add_book_in_favorites_one_book_shows_true – проверяет добавление книги в избранное.

test_delete_book_from_favorites_two_favorite_books_shows_true – проверяет удаление книги из избранного.

test_get_list_of_favorites_books_empty_collector_empty_favotite_list_shows_true – проверяет, что метод возвращает пустой список, если избранное пусто.