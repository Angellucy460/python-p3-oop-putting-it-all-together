#!/usr/bin/env python3

class Book:
    def __init__(self, title="", page_count=0, author=""):
        self.title = title
        self.page_count = page_count
        self.author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            print("Title must be a non-empty string.")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._author = value
        else:
            print("Author must be a non-empty string.")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        