from asyncio.windows_events import NULL


class Book():
    def __init__(self, bookName, bookCode, bookPrice, bookYear, bookAuthor):
        self.bookName=bookName
        self.bookCode=bookCode
        self.bookPrice=bookPrice
        self.bookYear=bookYear
        self.bookAuthor=bookAuthor

    def __repr__(self):
        return f'{self.bookName} {self.bookCode} {self.bookPrice} {self.bookYear} {self.bookAuthor}'

def getBooks():
    books = list()
    book1 = Book("Book1", "BC1", 20, 2015, "Simple author 1")
    book2 = Book("Book2", "BC2", 15, 2016, "Simple author 2")
    book3 = Book("Book3", "BC3", 5, 2017, "Simple author 3")
    book4 = Book("Book4", "BC4", 200, 2018, "Simple author 1")
    books.append(book1)
    books.append(book2)
    books.append(book3)
    books.append(book4)
    return books

def sort_name(books):
    sortedBooks = list()
    for book in books:
        sortedBooks.append(book)
    
    sortedBooks.sort(key=lambda b: b.bookName, reverse=True)
    return sortedBooks

def search_author(books, authorName):
    return [b for b in books if b.bookAuthor == authorName]

def search_bookCode(books, bookcode):
    return [b for b in books if b.bookCode == bookcode]

def Task2():
    books = getBooks()
    print(books)
    sortedBooks = sort_name(books)
    print(sortedBooks)
    print(search_author(books, "Simple author 1"))
    book = search_bookCode(books, "BC20")
    if len(book) == 0:
        print("The book is not found!")
    else:
        print(book[0].bookName)


Task2()