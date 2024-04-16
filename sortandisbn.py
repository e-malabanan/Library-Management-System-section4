class Library:
    def sirt_books_by_title(self):
        self.bood_collection.sort(key=lambda x: x.title)

    def unique_isbn_check(self, isbn):
        for book in self.book_collection:
            if book.isbn == isbn:
                return False
        return True