from marshmallow import Schema, fields, INCLUDE, EXCLUDE

class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()


incoming_book_data = {
    "title":"Clean Code",
    "author":"Bob Martih",
    "description":"A book about writing cleaner code."
}

book_schema = BookSchema(unknown=INCLUDE)
book = book_schema.load(incoming_book_data)

print(book)