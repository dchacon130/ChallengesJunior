import pytest
import requests

URL = 'http://127.0.0.1:8000/fizzbuzz'

def test_api_response():
    response = requests.get(URL)
    assert response.status_code == 200

def test_fizz_number():
    response = requests.get(URL+'/3')
    assert response.status_code == 200
    assert response.json()['item_id'] == 3
    assert response.json()['message'] == 'fizz'

def test_buzz_number():
    response = requests.get(URL+'/5')
    assert response.status_code == 200
    assert response.json()['item_id'] == 5
    assert response.json()['message'] == 'buzz'

def test_fizzbuzz_number():
    response = requests.get(URL+'/15')
    assert response.status_code == 200
    assert response.json()['item_id'] == 15
    assert response.json()['message'] == 'fizzbuzz'

def test_fizzbuzz_error():
    response = requests.get(URL+'/asdf/asdf/asdf')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Not Found'

def test_fizz_buzzs_range():
    response = requests.get(URL+'/1/16')
    assert response.status_code == 200
    assert response.json() == [
                                {
                                    "item_id": 1,
                                    "message": "1"
                                },
                                {
                                    "item_id": 2,
                                    "message": "2"
                                },
                                {
                                    "item_id": 3,
                                    "message": "fizz"
                                },
                                {
                                    "item_id": 4,
                                    "message": "4"
                                },
                                {
                                    "item_id": 5,
                                    "message": "buzz"
                                },
                                {
                                    "item_id": 6,
                                    "message": "fizz"
                                },
                                {
                                    "item_id": 7,
                                    "message": "7"
                                },
                                {
                                    "item_id": 8,
                                    "message": "8"
                                },
                                {
                                    "item_id": 9,
                                    "message": "fizz"
                                },
                                {
                                    "item_id": 10,
                                    "message": "buzz"
                                },
                                {
                                    "item_id": 11,
                                    "message": "11"
                                },
                                {
                                    "item_id": 12,
                                    "message": "fizz"
                                },
                                {
                                    "item_id": 13,
                                    "message": "13"
                                },
                                {
                                    "item_id": 14,
                                    "message": "14"
                                },
                                {
                                    "item_id": 15,
                                    "message": "fizzbuzz"
                                }
                            ]

if __name__ == "__main__":
    pytest.main()

# Ejecutar Pytest: python -m pytest --verbose