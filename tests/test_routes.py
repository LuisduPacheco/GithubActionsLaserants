import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_main(client):
    response = client.get('/')
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data is not None, "Response is not JSON"

    assert json_data['message'] == 'hola'


"""def test_get_book(client):
    response = client.get('/book')

    json_data = response.get_json()

    book_mock = {
        "book_id": 10,
        "title": "Cien años de solidad",
        "author": "Gabriel García",
        "isbn": "9780316769488",
        "genre_id": 1,
        "price": 15.99,
        "quantity": 120
    }

    assert response.status_code == 200
    assert type(json_data) == list
    assert json_data[0]['title'] == book_mock['title']
    assert json_data[0] == book_mock

def test_get_book_by_id(client):
    response = client.get('/book/10')
    json_data = response.get_json()
    book_mock = {
        "book_id": 10,
        "title": "Cien años de solidad",
        "author": "Gabriel García",
        "isbn": "9780316769488",
        "genre_id": 1,
        "price": 15.99,
        "quantity": 120
    }
    assert json_data == book_mock
    assert response.status_code == 200


def test_add_new_book(client):
    new_book = {
        "title": "El Quijote",
        "author": "Miguel de Cervantes",
        "isbn": "060934347",
        "genre_id": 1,
        "price": 12.99,
        "quantity": 75
    }


    response = client.post('/book', json=new_book)
    json_data = response.get_json()
    assert response.status_code == 201


def test_add_new_book_is_not_json(client):
    new_book = {
        "title": "El Quijote",
        "author": "Miguel de Cervantes",
        "isbn": "060934347",
        "genre_id": 99,
        "price": 12.99,
        "quantity": 75
    }

    response = client.post('/book', json=new_book)
    json_data = response.get_json()
    id_genre_test = 1
    assert response.status_code == 400


def test_add_new_book_id_genre_error(client):
    new_book = {
        "title": "El Quijote",
        "author": "Miguel de Cervantes",
        "isbn": "060934347",
        "genre_id": 99,
        "price": 12.99,
        "quantity": 75
    }

    response = client.post('/book', json=new_book)
    json_data = response.get_json()
    assert json_data['error'] == 'Book with id 99 is not found.'


def test_delete_book(client):
    response = client.delete('/book/12')
    assert response.status_code == 200
    message = response.get_json()
    assert message['message'] == 'Book with id 12 deleted.'


def test_delete_book_error_id(client):
    response = client.delete('/book/99')
    assert response.status_code == 400
    error = response.get_json()
    assert error['error'] == 'Book with id 99 is not found.'


def test_get_genre_by_id(client):
    response = client.get('/genre/1')
    json_data = response.get_json()
    assert response.status_code == 200


def test_get_genre_by_id_error(client):
    response = client.get('/genre/100')
    json_data = response.get_json()
    assert response.status_code == 400"""
