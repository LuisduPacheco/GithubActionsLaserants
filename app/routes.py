from app import app, db
from flask import jsonify, request
from app.models import Books, Genres


@app.route('/', methods=['GET'])
def main():
    return jsonify({'message': 'hola'}), 200


@app.route('/book', methods=['GET'])
def get_book():
    books = Books.query.all()
    book_list = []
    for book in books:
        book_data = {
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "genre_id": book.genre_id,
            "price": book.price,
            "quantity": book.quantity
        }
        book_list.append(book_data)
    return jsonify(book_list), 200


@app.route('/book/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = Books.query.get(id)

    if book is None:
        return jsonify({"error": f"Book with id {id} is not found."}), 400

    book_data = {
        "book_id": book.book_id,
        "title": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "genre_id": book.genre_id,
        "price": book.price,
        "quantity": book.quantity
    }
    return jsonify(book_data), 200


@app.route('/book', methods=['POST'])
def add_new_book():
    if request.is_json:
        data = request.get_json()

        _, code_return = get_genre_by_id(int(data['genre_id']))

        if code_return == 400:
            return jsonify({"error": f"Book with id {data['genre_id']} is not found."}), 400

        new_book = Books(title=data['title'], author=data['author'], isbn=data['isbn'],
                         genre_id=data['genre_id'], price=data['price'], quantity=data['quantity'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify(data), 201

    return jsonify({"error": "Error to add a new book, the request is not in JSON format"}), 400


@app.route('/book/<int:id>', methods=['DELETE'])
def deleteBook(id):
    book = Books.query.get(id)

    if book is None:
        return jsonify({"error": f"Book with id {id} is not found."}), 400

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": f"Book with id {id} deleted."})

# Routes for Genres
@app.route('/genre', methods=['GET'])
def get_genres():
    genres = Genres.query.all()
    genre_list = []
    for genre in genres:
        genre_data = {
            "genre_id": genre.genre_id,
            "name": genre.name
        }
        genre_list.append(genre_data)
    return jsonify(genre_list), 200


@app.route('/genre/<int:id>', methods=['GET'])
def get_genre_by_id(id):
    genre = Genres.query.get(id)

    if genre is None:
        return jsonify({"error": f"Book with id {id} is not found."}), 400

    genre_data = {
        "genre_id": genre.genre_id,
        "name": genre.name
    }
    return jsonify(genre_data), 200







