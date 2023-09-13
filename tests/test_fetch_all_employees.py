import requests

BASE_URL = 'http://127.0.0.1:5000/employees'
BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.bBQNQ_Sjh0iKyKoY-OpJss9GnxKKQzGbZvgEiehM9Q8'
HEADERS = {'Authorization': f'Bearer {BEARER_TOKEN}'}

# response = requests.get(BASE_URL, headers=HEADERS)
# print(response.status_code)
# print(response.json())


def test_all_employees():
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == [{'employeeId': 1, 'name': 'Mary', 'organization': 'IT', 'role': 'QA'},
                               {'employeeId': 2, 'name': 'Max', 'organization': 'IT', 'role': 'Senior PM'}]