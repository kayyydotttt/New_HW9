# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:56:14 2023

@author: Karis
"""

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        bl = BookLover("Karis", "karis@karis.com", "non-fiction")
        bl.add_book("cats")
        self.assertIn("cats", bl.book_list)
        
    def test_2_add_book(self):
        bl = BookLover()
        bl.add_book("The Hobbit")
        bl.add_book("The Hobbit")
        self.assertEqual(len(bl.book_list), 1)

    def test_3_has_read(self):
        bl = BookLover()
        bl.add_book("Harry Potter and the Philosopher's Stone")
        bl.add_book("The Lord of the Rings")
        self.assertTrue(bl.has_read("The Lord of the Rings"))

    def test_4_has_read(self):
        bl = BookLover()
        bl.add_book("The Hitchhiker's Guide to the Galaxy")
        self.assertFalse(bl.has_read("The Lord of the Rings"))

    def test_5_num_books_read(self):
        bl = BookLover()
        bl.add_book("1984")
        bl.add_book("Animal Farm")
        bl.add_book("Brave New World")
        self.assertEqual(bl.num_books_read(), 0)
        bl.mark_book_as_read("1984")
        self.assertEqual(bl.num_books_read(), 1)
        bl.mark_book_as_read("Animal Farm")
        bl.mark_book_as_read("Brave New World")
        self.assertEqual(bl.num_books_read(), 3)

    def test_6_fav_books(self):
        bl = BookLover()
        bl.add_book_with_rating("The Lord of the Rings", 5)
        bl.add_book_with_rating("Harry Potter and the Goblet of Fire", 4)
        bl.add_book_with_rating("Pride and Prejudice", 3)
        bl.add_book_with_rating("The Catcher in the Rye", 2)
        fav_books = bl.get_fav_books()
        for book in fav_books:
            self.assertGreater(book[1], 3)

if __name__ == '__main__':
    unittest.main(verbosity=3)