class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass




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
                if len(name.borrowed_books) <= 3:
                    for book in self.books:
                        if book.title == book_title:
                            if book.is_borrowed == False:
                                book.is_borrowed = True
                                name.borrowed_books.append(book)
                                return True
                            else:
                                raise BookAlreadyBorrowedException("Book already borrowed")
                        else:
                            raise BookNotFoundException("Book not found")
                    return True
                else:
                    raise MemberLimitExceededException("Member limit exceeded. 3 books maximum")

    def return_book(self, member_name, book_title):
        for name in self.members:
            if name.name == member_name:
                for book in name.borrowed_books:
                    if book.title == book_title:
                        book.is_borrowed = False
                        name.borrowed_books.remove(book)
                        return True
                    else:
                        raise BookNotFoundException(f"The book is not in the borrowed list of {member_name} member")
            else:
                return "No member with this name!"
           