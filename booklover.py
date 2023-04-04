# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:56:45 2023

@author: Karis
"""

import pandas as pd
import numpy as np
import seaborn

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    
    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].tolist():
            print(f"{self.name} has already read {book_name}.")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            print(f"{book_name} has been added to {self.name}'s book list.")
    
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].tolist()
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("1984", 5)
    test_object.add_book("To Kill a Mockingbird", 4)
    test_object.add_book("To Kill a Mockingbird", 3) # This book has already been added
    print(test_object.book_list)
    print(test_object.has_read("1984"))
    print(test_object.num_books_read())
    print(test_object.fav_books())