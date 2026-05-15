import pytest

from main import BooksCollector

@pytest.fixture # фикстура, которая создает экземпляр класса BooksCollector
def collector():
    collector = BooksCollector()
    return collector