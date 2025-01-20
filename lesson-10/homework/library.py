class Book:
    title = ""
    author = ""
    is_borrowed = False

class Member:
    name = ""
    borrowed_books = []

class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        if title in [book.title for book in self.books]:
            return False
        book = Book()
        book.title = title
        book.author = author
        self.books.append(book)
        return True
    
    def add_member(self, name):
        if name in [member.name for member in self.members]:
            return False
        member = Member()
        member.name = name
        self.members.append(member)
        return True
        
    def borrow_book(self, member_name, book_title):
        for name in self.members:
            if name.name == member_name:
                member = name
                break