from app import db
from app.models import Book


def create_books():
    books = list()

    books.append(Book(
        title="Python Crash Course",
        author="Eric Matthes",
        language="python",
        pages=416
    ))
    books.append(Book(
        title="Head First Python 2e",
        author="Paul Barry",
        language="python",
        pages=215
    ))
    books.append(Book(
        title="JavaScript: The Definitive Guide",
        author="David Flanagan ",
        language="javascript",
        pages=812
    ))

    db.session.add_all(books)
    db.session.commit()


def print_books():
    books = Book.query.all()
    for book in books:
        print(book.serialize)


if __name__ == '__main__':
    create_books()
    print_books()
