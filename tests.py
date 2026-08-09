from main import BooksCollector
import pytest


class TestBooksCollector:
    def test_add_new_book_add_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Башня")
        assert collector.books_genre.get("Башня") == ""

    @pytest.mark.parametrize("genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"])
    def test_set_book_genre_sets_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Тестовая книга")
        collector.set_book_genre("Тестовая книга", genre)
        assert collector.books_genre["Тестовая книга"] == genre

    @pytest.mark.parametrize("genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"])
    def test_get_book_genre_return_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Когда плачут Чайки")
        collector.set_book_genre("Когда плачут Чайки", genre)
        assert collector.get_book_genre("Когда плачут Чайки") == genre

    @pytest.mark.parametrize("genre, expected_count", [("Детективы", 2), ("Фантастика", 1), ("Ужасы", 0), ("Мультфильмы", 0), ("Комедии", 0)])
    def test_get_books_with_specific_genre_return_books_with_needed_genre(self, genre, expected_count):
        collector = BooksCollector()
        collector.add_new_book("Когда плачут Чайки")
        collector.add_new_book("Когда плачут Цикады")
        collector.add_new_book("Steins;Gate")
        collector.set_book_genre("Когда плачут Чайки", "Детективы")
        collector.set_book_genre("Когда плачут Цикады", "Детективы")
        collector.set_book_genre("Steins;Gate", "Фантастика")
        assert len(collector.get_books_with_specific_genre(genre)) == expected_count

    def test_get_books_genre_return_books_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Когда плачут Чайки")
        collector.add_new_book("Когда плачут Цикады")
        collector.add_new_book("Steins;Gate")
        assert len(collector.get_books_genre()) == 3 and isinstance(collector.get_books_genre(), dict)

    def test_get_books_for_children_return_child_books(self):
        collector = BooksCollector()
        collector.add_new_book("Когда плачут Чайки")
        collector.add_new_book("Когда плачут Цикады")
        collector.add_new_book("Steins;Gate")
        collector.set_book_genre("Когда плачут Чайки", "Детективы")
        collector.set_book_genre("Когда плачут Цикады", "Детективы")
        collector.set_book_genre("Steins;Gate", "Фантастика")
        assert len(collector.get_books_for_children()) == 1 and "Когда плачут Чайки" not in collector.get_books_for_children()

    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        collector.add_new_book("Когда плачут Чайки")
        collector.add_new_book("Когда плачут Цикады")
        collector.add_book_in_favorites("Когда плачут Чайки")
        assert len(collector.favorites) == 1 and "Когда плачут Чайки" in collector.favorites

    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        collector.add_new_book("Когда плачут Чайки")
        collector.add_new_book("Когда плачут Цикады")
        collector.add_book_in_favorites("Когда плачут Чайки")
        collector.delete_book_from_favorites("Когда плачут Чайки")
        assert len(collector.favorites) == 0 and "Когда плачут Чайки" not in collector.favorites

    def test_get_list_of_favorites_books_return_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Когда плачут Чайки")
        collector.add_new_book("Когда плачут Цикады")
        collector.add_book_in_favorites("Когда плачут Чайки")
        result = ["Когда плачут Чайки"]
        assert collector.get_list_of_favorites_books() == result
