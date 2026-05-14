import pytest

from main import BooksCollector

@pytest.fixture # фикстура, которая добавляет книгу
def book():
    book = BooksCollector.add_new_book('Тестирование для профи')
    return book

@pytest.fixture # фикстура, которая создает экземпляр класса BooksCollector
def collector():
    collector = BooksCollector()
    return collector