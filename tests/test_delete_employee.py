import requests

BASE_URL = 'http://127.0.0.1:5000/employees/3'
BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.bBQNQ_Sjh0iKyKoY-OpJss9GnxKKQzGbZvgEiehM9Q8'
HEADERS = {'Authorization': f'Bearer {BEARER_TOKEN}'}


def test_delete():
    response = requests.delete(BASE_URL, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {'message': 'Employee deleted'}