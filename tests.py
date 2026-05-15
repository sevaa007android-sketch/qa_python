import pytest
from main import BooksCollector


class TestBooksCollector:

 
    def test_add_new_book_add_two_books_shows_true(self, collector):
        # создаем экземпляр (объект) класса BooksCollector
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2


    def test_add_new_book_add_two_equal_books_shows_true(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['asdasdddddasdasdas asdasdasdasdatryrtysddsad', ''])
    def test_add_new_book_add_incorrect_name_shows_error(self, name, collector):      
        collector.add_new_book(name)
        
        assert not len(collector.get_books_genre()) == 1

    def test_set_book_genre_one_book_one_genre_shows_true(self, collector):
        name = 'Позитивный тест метода установки жанра'

        collector.add_new_book(name)

        collector.set_book_genre(name, 'Фантастика')

        assert collector.get_book_genre(name) == 'Фантастика'

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Несуществующее имя книги', 'Мультфильмы'], 
            ['Негативный тест метода установки жанра', 'Несуществующий жанр']
        ]
    )
    def test_set_book_genre_incorrect_one_book_one_genre_shows_false(self, collector, name, genre):
        collector.add_new_book('Негативный тест метода установки жанра')

        collector.set_book_genre(name, genre)

        assert not collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['1', 'Мультфильмы'], 
            ['4012345678901234567890123456789012345678', 'Детективы']
        ]
    )
    def test_get_book_genre_one_book_shows_true(self, collector, name, genre):    
        collector.add_new_book(name)

        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre
    
    def test_get_book_genre_one_non_existing_book_shows_error(self, collector):

        assert collector.get_book_genre('Несуществующая книга') == None

    @pytest.mark.parametrize(
        'names,genres',
        [
            [['Тестовая книга 1', 'Тестовая книга 2', 'Тестовая книга 3'], ['Мультфильмы', 'Детективы', 'Ужасы']], 
            [['Тестовая книга 1', 'Тестовая книга 2', 'Тестовая книга 3'], ['Мультфильмы', 'Мультфильмы', 'Ужасы']],
            [['Тестовая книга 1', 'Тестовая книга 2', 'Тестовая книга 3'], ['Мультфильмы', 'Мультфильмы', 'Мультфильмы']]
        ]
    )
    def test_get_books_with_specific_genre_three_books_three_genres_shows_true(self, collector, names, genres):
        for name, genre in zip(names, genres):
                    collector.add_new_book(name)

                    collector.set_book_genre(name, genre)

        assert genres.count(genres[0]) == len(collector.get_books_with_specific_genre(genres[0]))

    def test_get_books_genre_one_book_one_genre_shows_true(self, collector):
        collector.add_new_book('Test book 1')

        assert collector.books_genre == collector.get_books_genre()

    @pytest.mark.parametrize(
        'names,genres,count_children_books',
        [
            [['Тестовая книга 1', 'Тестовая книга 2', 'Тестовая книга 3'], ['Мультфильмы', 'Детективы', 'Ужасы'], 1], 
            [['Тестовая книга 1', 'Тестовая книга 2', 'Тестовая книга 3'], ['Мультфильмы', 'Мультфильмы', 'Ужасы'], 2],
            [['Тестовая книга 1', 'Тестовая книга 2', 'Тестовая книга 3'], ['Мультфильмы', 'Мультфильмы', 'Мультфильмы'], 3]
        ]
    )
    def test_get_books_for_children_three_books_three_genre_shows_true(self, collector, names, genres, count_children_books):
        for name, genre in zip(names, genres):
                    collector.add_new_book(name)

                    collector.set_book_genre(name, genre)

        assert len(collector.get_books_for_children()) == count_children_books
         
    def test_add_book_in_favorites_one_book_shows_true(self, collector):
        collector.add_new_book('Test book no genre')

        collector.add_book_in_favorites('Test book no genre')

        assert len(collector.get_books_genre()) == len(collector.favorites)
    

    def test_delete_book_from_favorites_two_favorite_books_shows_true(self, collector):  
        name_book_1 = 'Test book #1 no genre'
        name_book_2 = 'Test book #2 no genre'

        collector.add_new_book(name_book_1)
        collector.add_new_book(name_book_2)

        collector.add_book_in_favorites(name_book_1)                
        collector.add_book_in_favorites(name_book_2)

        collector.delete_book_from_favorites(name_book_1)

        assert name_book_2 == collector.favorites[0]
    
    def test_get_list_of_favorites_books_empty_collector_empty_favotite_list_shows_true(self, collector):
        assert collector.favorites == collector.get_list_of_favorites_books()



