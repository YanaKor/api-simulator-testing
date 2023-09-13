import requests


def get_weather_data(city):
    url = f'https://api.weather.com/{city}'
    response = requests.get(url)
    return response.json()


def test_get_weather_data(mocker):
    mock_get = mocker.patch('requests.get')
    mock_resp = mocker.Mock()
    resp_data = {
        'main': {
            'temperature': 20.0
        },
        'weather': [{
            'description': 'sunny',
            'is_windy': False
        }]
    }
    mock_resp.json.return_value = resp_data
    mock_get.return_value = mock_resp

    weather_data = get_weather_data('London')
    expected_url = 'https://api.weather.com/London'
    mock_get.assert_called_once_with(expected_url)

    assert weather_data['main']['temperature'] == 20.0
    assert weather_data['weather'][0]['is_windy'] is False


    # название - стр ''
    # год - 2000 инт
    # призы - может быть неск массив['', '']
    #  режисер - стр ''
    # актеры - массив - объект [{'': ''}]


 # cursor = db_connection.connection.cursor()
    # cursor.execute('DELETE FROM employees')
    #
    # time.sleep(15)


