class Library:
    def __init__(self, no_of_books, booksList):
        self._no_of_books = no_of_books
        self.booksList = booksList
    
    def validLibrary(self):
        if len(self.booksList) != self._no_of_books:
            print("No of books provided and no of books in the booksList are not same")
            return False
        return True
    
    def getLibraryInfo(self):
        if(self.validLibrary()):
            print(f"books in library are {self.booksList}")
            print(f"Number of books in the library are {self._no_of_books}")
        else:
            print("Invalid Library Object")

    
    
    # @property
    # def no_of_books(self):
    #     return self._no_of_books

    # @no_of_books.setter
    # def setBooks(self, value):
    #     self.no_of_books = value

lib = Library(3, ["first", "second"])
# print(lib.validLibrary())
lib.getLibraryInfo()