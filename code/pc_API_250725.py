import requests
from pprint import pprint

url = 'https://fakestoreapi.com/carts'
data = requests.get(url).json()
# requests.get(url) : 서버 주소에 해당하는 데이터를 요청
pprint(data)