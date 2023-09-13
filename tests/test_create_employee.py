import requests

BASE_URL = 'http://127.0.0.1:5000/employees'
BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.bBQNQ_Sjh0iKyKoY-OpJss9GnxKKQzGbZvgEiehM9Q8'
HEADERS = {'Authorization': f'Bearer {BEARER_TOKEN}', 'Content-Type': 'application/json'}

data = {
    "name": "Jone",
    "organization": "Account",
    "role": "Junior"
}


def test_create_employee():
    response = requests.post(BASE_URL, headers=HEADERS, json=data)
    assert response.status_code == 200
    assert response.json() == {'employeeId': 4, 'name': 'Jone', 'organization': 'Account', 'role': 'Junior'}