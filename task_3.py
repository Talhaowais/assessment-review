import requests

def test_weather_app_data(url):
     response = requests.get(url)
     response_body = response.json()
     assert response_body['coord']['lon'] == -0.13
     assert response_body['coord']['lat'] == 51.51
     assert response_body['sys']['country'] == "GB"
     assert response.status_code == 200

if __name__ == '__main__':
    url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"
    test_weather_app_data(url)
