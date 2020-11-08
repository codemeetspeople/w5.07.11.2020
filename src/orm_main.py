from orm.models import Book

book = Book()
book.title = 'My story'
book.author = 'caiman'
book.save()

print(book.id)
print(book.title)
print(book.author)
print('====')
print()

book2 = Book(book.id)
print(f'{book.id} == {book2.id}')
print(book2.title)
print(book2.author)
print('====')
print()

book2.author = 'anonymous'
book2.save()

book3 = Book(book.id)
print(book3.author)
