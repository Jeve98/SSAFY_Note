import requests
from pprint import pprint

url = 'https://fakestoreapi.com/carts'
data = requests.get(url).json()
# requests.get(url) : 서버 주소에 해당하는 데이터를 요청
pprint(data)

APIKey = '87246d75e1ce26e1392a087b3d1d88c5'
lat = 37.56
lon = 126.97
cityName = 'Seoul,KR'
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKey}'
url2 = f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIKey}'
# 섭씨 온도 = 켈빈 온도 - 273.15